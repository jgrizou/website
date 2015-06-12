import os
import time
import fnmatch

import filetools

import logging
logger = logging.getLogger(__name__)


def match_pattern(filename, pattern):
    return fnmatch.fnmatchcase(filename, pattern) or \
        filetools.is_subdir(filename, pattern) or \
        os.path.basename(filename) == pattern


def is_ignored(filename, ignore_patterns):
    for pattern in ignore_patterns:
        if match_pattern(filename, pattern):
            return True
    return False


def require_update(source_file, target_file):
    return not target_file.exists or target_file.is_older(source_file)


def apply_rule(source_file, target_refpath, rule):

    target_file = rule['make_target_file'](source_file, target_refpath)
    logger.info('Target is: ' + target_file.relpath)

    if require_update(source_file, target_file):
        logger.info('Applying ' + rule['compile'].__name__)
        rule['compile'](source_file, target_file)
    else:
        logger.info('Update not required, file already exists and is newer')


def process_file(source_file, target_refpath, ignore_patterns, rules, default_rule=None):

    if not isinstance(rules, list):
        rules = [rules]

    logger.info('#####')
    logger.info('Processing: ' + source_file.relpath)

    if is_ignored(source_file.relpath, ignore_patterns):
        logger.info('Ignored upon user request')
        logger.info('#####')
        return

    found_rule = False
    for rule in rules:
        if match_pattern(source_file.relpath, rule['file_patterns']):
            found_rule = True
            apply_rule(source_file, target_refpath, rule)

    if not found_rule:
        if default_rule:
            logger.info('No rule found, applying default rule')
            apply_rule(source_file, target_refpath, default_rule)
        else:
            logger.info('No rule found, no default rule, do nothing')

    logger.info('#####')


def build(source_refpath, target_refpath, ignore_patterns, compile_rules, default_rule=None):

    start_time = time.time()

    for path, dirs, files in os.walk(source_refpath):
        for filename in files:
            source_file = filetools.File(os.path.join(path, filename), source_refpath)
            process_file(source_file, target_refpath, ignore_patterns, compile_rules, default_rule)

    logger.info('Built in {} seconds'.format(time.time() - start_time))
