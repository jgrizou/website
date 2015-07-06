import os
import logging

import shutil
import subprocess

import jinja2

import filetools
import portfoliotools

logger = logging.getLogger(__name__)


def duplicate_at_target(source_file, target_refpath):
    return source_file.duplicate(target_refpath)


def changext(ext):
    def rename_to_ext(source_file, target_refpath):
        target_file = duplicate_at_target(source_file, target_refpath)
        target_file.change_ext(ext)
        return target_file
    return rename_to_ext


def copy_to_target(source_file, target_file):
    logger.info('Copying to: ' + target_file.relpath)
    filetools.ensure_dir(target_file)
    shutil.copy(source_file.path, target_file.path)


# panzer
def apply_panzer(additional_args=[], working_directory=None):
    def panzer(source_file, target_file):

        filetools.ensure_dir(target_file)

        default_command = ['panzer', source_file.path, '-o', target_file.path]

        proc = subprocess.Popen(default_command + additional_args,
                                stderr=subprocess.PIPE, cwd=working_directory)

        logger.info("\n" + proc.stderr.read().decode())
        # \n is just to make log nicer
    return panzer


# jinja
def apply_jinja(jinja_filter_refpath, baseUrl):

    def jinja(source_file, target_file):

        jinja_loader = jinja2.FileSystemLoader(source_file.dirname)
        jinja_env = jinja2.Environment(loader=jinja_loader)

        load_jinja_filters(jinja_env, jinja_filter_refpath)

        template = jinja_env.get_template(source_file.filename)

        target_file.write(template.render(baseUrl=baseUrl,
                                          filepath=os.path.join(os.sep, source_file.reldirname)))

    return jinja


def load_jinja_filters(jinja_env, jinja_filter_refpath):

    import sys
    sys.path.append(jinja_filter_refpath)

    import glob
    filter_modules = glob.glob(os.path.join(jinja_filter_refpath, '*.py'))

    import importlib
    import inspect

    for module_filename in filter_modules:
        module_file = filetools.File(module_filename, jinja_filter_refpath)
        module_name = module_file.filebasename
        module = importlib.import_module(module_name)
        module_functions = inspect.getmembers(module, inspect.isfunction)
        for func in module_functions:
            logger.info('Adding jinja filter: {}'.format(func[0]))
            jinja_env.filters[func[0]] = func[1]


# combined rules
def apply_jinja_then_panzer(jinja_filter_refpath, baseUrl, panzer_additional_args, tmpfile_refpath, working_directory=None):

    def jinja_then_panzer(source_file, target_file):

        panzer_source_file = source_file.duplicate(tmpfile_refpath)

        jinja_func = apply_jinja(jinja_filter_refpath, baseUrl)
        jinja_func(source_file, panzer_source_file)

        panzer_func = apply_panzer(panzer_additional_args, working_directory)
        panzer_func(panzer_source_file, target_file)

    return jinja_then_panzer


# portfolio
def apply_portfolio(jinja_template_refpath):

    def portfolio(source_file, target_file):

        import configparser
        config = configparser.ConfigParser()
        config.read(source_file.path)

        thumbnails = config['PORTFOLIO']['thumbnails_relative_path']
        thumbnails = thumbnails.split('\n')
        thumbnails = [x for x in thumbnails if x]

        processed = portfoliotools.build_portfolio(
            config['PORTFOLIO']['path_from_ref'],
            thumbnails,
            jinja_template_refpath,
            config['PORTFOLIO']['portfolio_templatename'])

        filetools.ensure_dir(target_file)
        with open(target_file.path, 'w') as f:
            f.write(processed)

    return portfolio


# python
def apply_python(config):

    def python(source_file, target_file):

        import sys
        sys.path.append(source_file.dirname)

        import importlib
        module_name = source_file.filebasename
        module = importlib.import_module(module_name)
        module.main(config, source_file, target_file)

    return python


# wkhtmltopdf
def apply_wkhtmltopdf():

    def wkhtmltopdf(source_file, target_file):

        command = ['wkhtmltopdf', source_file.path, target_file.path]
        proc = subprocess.Popen(command, stderr=subprocess.PIPE)

        logger.info("\n" + proc.stderr.read().decode())

    return wkhtmltopdf
