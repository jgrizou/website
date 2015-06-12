

ordered_subfoldername_to_thumbnail = [
    'p1',
    'p2']


def main(config, source_file, target_file):

    import os

    import logging
    logger = logging.getLogger(__name__)
    logger.info('Building project page')

    import sys
    sys.path.append(config['PATH']['python'])

    #
    import ruletools
    import portfoliotools

    portfolio_relative_path = config['WEB']['baseUrl'] + '/projects'

    jinja_path = config['PATH']['jinja']
    jinja_template_path = os.path.join(jinja_path, 'template')

    portfolio_templatename = 'portfolio.html'

    button_text = 'View Project'

    portfolio_html = portfoliotools.build_portfolio(portfolio_relative_path, ordered_subfoldername_to_thumbnail, jinja_template_path, portfolio_templatename, button_text)

    # removing all indentation for pandoc
    stripped_html = ''
    for line in portfolio_html.splitlines():
        unindented = line.strip()
        if unindented:
            stripped_html += unindented + '\n'

    #
    content = '---\nstyle: Empty\n---'
    content += '\n\n'
    content += stripped_html

    # make per type page
    tmpfile_refpath = config['PATH']['tmp']

    panzer_source_file = source_file.duplicate(tmpfile_refpath)
    panzer_source_file.change_ext('md')

    panzer_source_file.write(content)

    panzer_refpath = config['PATH']['panzer']
    panzer_args = ['---panzer-support', panzer_refpath]

    panzer_func = ruletools.apply_panzer(panzer_args)
    panzer_func(panzer_source_file, target_file)
