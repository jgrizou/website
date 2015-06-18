
key_filter_list = [
    ('All', '*'),
    ('Research', '.research'),
    ('Robots', '.robot')]


def main(config, source_file, target_file):

    import logging
    logger = logging.getLogger(__name__)
    logger.info('Building project page')

    import sys
    sys.path.append(config['PATH']['python'])

    #
    import ruletools
    import isotope

    import os
    folder_path = os.path.dirname(os.path.realpath(__file__))

    # config['WEB']['baseUrl'] + '/projects'

    body_html = isotope.build_isotope_filter_button(key_filter_list)
    body_html += '\n\n'
    body_html += isotope.build_isotope_grid(config, folder_path)
    body_html += '\n\n'
    body_html += isotope.get_isotope_js()

    # removing all indentation for pandoc
    stripped_html = ''
    for line in body_html.splitlines():
        unindented = line.strip()
        if unindented:
            stripped_html += unindented + '\n'

    #
    content = '---\nstyle: FullPage\nnavbar:\n  projects: true\n---'
    content += '\n\n'
    content += stripped_html

    # make page
    tmpfile_refpath = config['PATH']['tmp']

    panzer_source_file = source_file.duplicate(tmpfile_refpath)
    panzer_source_file.change_ext('md')

    panzer_source_file.write(content)

    panzer_refpath = config['PATH']['panzer']
    panzer_args = ['---panzer-support', panzer_refpath]

    panzer_func = ruletools.apply_panzer(panzer_args)
    panzer_func(panzer_source_file, target_file)
