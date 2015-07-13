
section_folder = 'sections'

section_ordering = ['header.md',
                    'education.md',
                    'experiences.md',
                    'awards.md',
                    'grants.md',
                    'collaboration.md',
                    'publications.md',
                    'talks.md',
                    'services.md',
                    'skills.md',
                    'languages.md',
                    'personal.md',
                    'moocs.md']


def main(config, source_file, target_file):

    import logging
    logger = logging.getLogger(__name__)
    logger.info('Building cv')

    import sys
    sys.path.append(config['PATH']['python'])

    import os
    import filetools
    import ruletools

    tmpfile_refpath = config['PATH']['tmp']

    cv_source_file = source_file.duplicate(tmpfile_refpath)
    cv_source_file.change_filename('cv.md')

    for section in section_ordering:
        section_file_path = os.path.join(source_file.dirname, section_folder, section)
        section_source_file = filetools.File(section_file_path, source_file.refpath)

        jinja_filter_path = os.path.join(config['PATH']['jinja'], 'filter')
        baseUrl = config['WEB']['baseUrl']
        jinja_func = ruletools.apply_jinja(jinja_filter_path, baseUrl)

        section_target_file = section_source_file.duplicate(tmpfile_refpath)
        jinja_func(section_source_file, section_target_file)

        cv_source_file.append(section_target_file.read() + '\n\n')

    # cv html
    cv_target_file = cv_source_file.duplicate(target_file.refpath)
    cv_target_file.change_ext('html')

    panzer_args = ['---panzer-support', config['PATH']['panzer']]
    working_directory = config['PATH']['panzer']

    panzer_func = ruletools.apply_panzer(panzer_args, working_directory)
    panzer_func(cv_source_file, cv_target_file)

    # cv standalone html
    data = '---\nstyle: CVstandalone\n---\n'
    data += cv_source_file.read()
    cv_source_file.write(data)

    cv_target_file = cv_source_file.duplicate(target_file.refpath)
    cv_target_file.change_filename('cv_standalone.html')

    panzer_args = ['---panzer-support', config['PATH']['panzer']]
    working_directory = config['PATH']['panzer']

    panzer_func = ruletools.apply_panzer(panzer_args, working_directory)
    panzer_func(cv_source_file, cv_target_file)

    # cv pdf
    pdf_target_file = cv_target_file.duplicate()
    pdf_target_file.change_filename('cv.pdf')

    wkhtmltopdf_func = ruletools.apply_wkhtmltopdf()
    wkhtmltopdf_func(cv_target_file, pdf_target_file)

    # write a dummy file at target to confirm good exec
    target_file.write('<p> done </p>')

    panzer_args = ['---panzer-support', config['PATH']['panzer']]
    working_directory = config['PATH']['panzer']

    jinjapanzer_func = ruletools.apply_jinja_then_panzer(
        jinja_filter_path,
        config['WEB']['baseUrl'],
        panzer_args,
        config['PATH']['tmp'],
        working_directory)
    jinjapanzer_func(cv_source_file, cv_target_file)
