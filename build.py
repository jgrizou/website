#!/usr/bin/env python

import os
refpath = os.path.dirname(os.path.realpath(__file__))

import configparser
config = configparser.ConfigParser()
config.read(os.path.join(refpath, 'config.cfg'))


def process_config(refpath, config):

    for key in config['PATH']:
        config['PATH'][key] = os.path.join(refpath, config['PATH'][key])

    return config

config = process_config(refpath, config)

import sys
sys.path.append(config['PATH']['python'])

#
import shutil
import ruletools
import builder


def clean_include():
    logger.info('##########')
    logger.info('cleaning include')
    logger.info('##########')

    if os.path.exists(config['PATH']['include_target']):
        shutil.rmtree(config['PATH']['include_target'])


def build_include():
    logger.info('##########')
    logger.info('building include')
    logger.info('##########')

    jinja_filter_path = os.path.join(config['PATH']['jinja'], 'filter')

    default_rule = {'make_target_file': ruletools.duplicate_at_target,
                    'compile': ruletools.apply_jinja(jinja_filter_path,
                                                     config['WEB']['baseUrl'])}

    ignore_patterns = ['*.DS_Store', 'styles', 'template']

    ##
    jinja_filter_path = os.path.join(config['PATH']['jinja'], 'filter')
    panzer_args = ['---panzer-support', config['PATH']['include_source']]
    working_directory = config['PATH']['include_source']

    panzer_rule = {
        'file_patterns': '*.md',
        'make_target_file': ruletools.changext('html'),
        'compile': ruletools.apply_jinja_then_panzer(jinja_filter_path,
                                                     config['WEB']['baseUrl'],
                                                     panzer_args,
                                                     config['PATH']['tmp'],
                                                     working_directory)}

    ##
    rules = [panzer_rule]

    builder.build(config['PATH']['include_source'],
                  config['PATH']['include_target'],
                  ignore_patterns,
                  rules,
                  default_rule)


def clean_template():
    logger.info('##########')
    logger.info('cleaning template')
    logger.info('##########')

    if os.path.exists(config['PATH']['template_target']):
        shutil.rmtree(config['PATH']['template_target'])


def build_template():
    logger.info('##########')
    logger.info('building template')
    logger.info('##########')

    default_rule = {'make_target_file': ruletools.duplicate_at_target,
                    'compile': ruletools.copy_to_target}

    ignore_patterns = ['*.DS_Store', 'include', 'styles', 'substyles', 'subtemplate']

    #
    jinja_filter_path = os.path.join(config['PATH']['jinja'], 'filter')
    panzer_args = ['---panzer-support', config['PATH']['template_source']]
    working_directory = config['PATH']['template_source']

    jinjapanzer = {
        'file_patterns': '*.md',
        'make_target_file': ruletools.changext('html'),
        'compile': ruletools.apply_jinja_then_panzer(jinja_filter_path,
                                                     config['WEB']['baseUrl'],
                                                     panzer_args,
                                                     config['PATH']['tmp'],
                                                     working_directory)}

    #
    rules = [jinjapanzer]

    builder.build(config['PATH']['template_source'],
                  config['PATH']['template_target'],
                  ignore_patterns,
                  rules,
                  default_rule)


def clean_site():
    logger.info('##########')
    logger.info('cleaning site')
    logger.info('##########')

    if os.path.exists(config['PATH']['site_target']):
        shutil.rmtree(config['PATH']['site_target'])


def build_site():
    logger.info('##########')
    logger.info('building site')
    logger.info('##########')

    default_rule = {'make_target_file': ruletools.duplicate_at_target,
                    'compile': ruletools.copy_to_target}

    ignore_patterns = ['*.DS_Store', '*__pycache__*', 'thumbnail.md']

    jinja_filter_path = os.path.join(config['PATH']['jinja'], 'filter')
    panzer_args = ['---panzer-support', config['PATH']['panzer']]
    working_directory = config['PATH']['panzer']

    jinjapanzer = {
        'file_patterns': '*.md',
        'make_target_file': ruletools.changext('html'),
        'compile': ruletools.apply_jinja_then_panzer(jinja_filter_path,
                                                     config['WEB']['baseUrl'],
                                                     panzer_args,
                                                     config['PATH']['tmp'],
                                                     working_directory)}

    python = {
        'file_patterns': '*.py',
        'make_target_file': ruletools.changext('html'),
        'compile': ruletools.apply_python(config)}

    rules = [jinjapanzer, python]

    builder.build(config['PATH']['site_source'],
                  config['PATH']['site_target'],
                  ignore_patterns,
                  rules,
                  default_rule)


def clean_tmp():
    logger.info('##########')
    logger.info('cleaning tmp file')
    logger.info('##########')

    if os.path.exists(config['PATH']['tmp']):
        shutil.rmtree(config['PATH']['tmp'])


def build_all():
    build_include()
    build_template()
    build_site()


def clean_all():
    clean_include()
    clean_template()
    clean_site()


if __name__ == "__main__":
    import time
    start_time = time.time()

    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument("-v", "--verbose", help="logging on all", action="store_true")
    parser.add_argument("--clean", help="clean all", action="store_true")
    parser.add_argument("--full", help="build from scrath", action="store_true")
    parser.add_argument("--keeptmp", help="do not delete tmp file", action="store_true")
    parser.add_argument("--local", help="change baseUrl to ''", action="store_true")
    args = parser.parse_args()

    #
    import logging
    log_file = os.path.join(refpath, 'build.log')
    if args.verbose:
        logging.basicConfig(stream=sys.stdout, level=logging.DEBUG)
    else:
        logging.basicConfig(filename=log_file, filemode='w', level=logging.DEBUG)
    logger = logging.getLogger(__name__)

    #
    if args.local:
        config['WEB']['baseUrl'] = ''

    if args.clean:
        clean_all()
    elif args.full:
        clean_all()
        build_all()
    else:
        build_all()

    if not args.keeptmp:
        clean_tmp()

    logger.info('Full building time {}'.format(time.time() - start_time))
