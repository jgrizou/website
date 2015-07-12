

selected_publication_id = [
    'grizou2014learning',
    'iturrate2015exploiting',
    'grizou2014interactive',
    'vollmer2014studying',
    'grizou2013robot']


def make_special_pages(config, source_file, target_file, page_name, content, title):

    import sys
    sys.path.append(config['PATH']['python'])

    tmpfile_refpath = config['PATH']['tmp']

    import ruletools

    # make page html
    page_source_file = source_file.duplicate()
    page_source_file.change_filename(page_name + '.md')

    peryear_target_file = page_source_file.duplicate(target_file.refpath)
    peryear_target_file.change_ext('html')

    panzer_source_file = page_source_file.duplicate(tmpfile_refpath)
    panzer_source_file.write(content)

    panzer_func = ruletools.apply_panzer()
    panzer_func(panzer_source_file, peryear_target_file)

    # make standalone html
    page_standalone_source_file = panzer_source_file.duplicate()
    page_standalone_source_file.change_filename(page_name + '_standalone.md')

    data = '---\nstyle: Publications\n---\n\n'
    if title:
        data += '#' + title + '\n\n'

    data += panzer_source_file.read()
    page_standalone_source_file.write(data)

    page_standalone_target_file = page_standalone_source_file.duplicate(target_file.refpath)
    page_standalone_target_file.change_ext('html')

    panzer_args = ['---panzer-support', config['PATH']['panzer']]
    working_directory = config['PATH']['panzer']

    panzer_func = ruletools.apply_panzer(panzer_args, working_directory)
    panzer_func(page_standalone_source_file, page_standalone_target_file)

    # make pdf
    pdf_target_file = page_standalone_target_file.duplicate()
    pdf_target_file.change_filename('publications_' + page_name + '.pdf')

    wkhtmltopdf_func = ruletools.apply_wkhtmltopdf()
    wkhtmltopdf_func(page_standalone_target_file, pdf_target_file)


def main(config, source_file, target_file):

    import logging
    logger = logging.getLogger(__name__)
    logger.info('Building publication')

    import sys
    sys.path.append(config['PATH']['python'])

    import bibtools
    import filetools

    pubs, bibdatabase = bibtools.process_all_pubs(config, source_file, target_file)

    # make per type page
    page_name = 'pertype'
    content = bibtools.pubs_to_md_per_type(pubs)
    title = 'Publications Per Type'
    make_special_pages(config, source_file, target_file, page_name, content, title)

    # make per year page
    page_name = 'peryear'
    content = bibtools.pubs_to_md_per_year(pubs)
    title = 'Publications Per Year'
    make_special_pages(config, source_file, target_file, page_name, content, title)

    # make selected page
    page_name = 'selected'
    content = bibtools.pubs_to_md_selected(pubs, selected_publication_id)
    title = None
    make_special_pages(config, source_file, target_file, page_name, content, title)

    # write full bibfile
    import bibtexparser
    fullbib_target_file = target_file.duplicate()
    fullbib_target_file.change_filename('jgrizou.bib')
    filetools.ensure_dir(fullbib_target_file)
    with open(fullbib_target_file.path, 'w') as f:
        bibtexparser.dump(bibdatabase, f)
    bibtools.homogeneize_bibfile(fullbib_target_file.path)

    # write a dummy file at target to confirm good exec
    target_file.write('<p> done </p>')
