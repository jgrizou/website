

selected_publication_id = [
    'grizou2014learning',
    'iturrate2015exploiting',
    'grizou2014interactive',
    'vollmer2014studying',
    'grizou2013robot']


def main(config, source_file, target_file):

    import logging
    logger = logging.getLogger(__name__)
    logger.info('Building publication')

    import sys
    sys.path.append(config['PATH']['python'])

    tmpfile_refpath = config['PATH']['tmp']

    import bibtools
    import ruletools
    import filetools

    pubs, bibdatabase = bibtools.process_all_pubs(config, source_file, target_file)

    # make per type page
    pertype_source_file = source_file.duplicate()
    pertype_source_file.change_filename('pertype.md')

    pertype_target_file = pertype_source_file.duplicate(target_file.refpath)
    pertype_target_file.change_ext('html')

    panzer_source_file = pertype_source_file.duplicate(tmpfile_refpath)
    panzer_source_file.write(bibtools.pubs_to_md_per_type(pubs))

    panzer_func = ruletools.apply_panzer()
    panzer_func(panzer_source_file, pertype_target_file)

    # make per year page
    peryear_source_file = source_file.duplicate()
    peryear_source_file.change_filename('peryear.md')

    peryear_target_file = peryear_source_file.duplicate(target_file.refpath)
    peryear_target_file.change_ext('html')

    panzer_source_file = peryear_source_file.duplicate(tmpfile_refpath)
    panzer_source_file.write(bibtools.pubs_to_md_per_year(pubs))

    panzer_func = ruletools.apply_panzer()
    panzer_func(panzer_source_file, peryear_target_file)

    # make selected page
    selected_source_file = source_file.duplicate()
    selected_source_file.change_filename('selected.md')

    selected_target_file = selected_source_file.duplicate(target_file.refpath)
    selected_target_file.change_ext('html')

    panzer_source_file = selected_source_file.duplicate(tmpfile_refpath)
    panzer_source_file.write(bibtools.pubs_to_md_selected(pubs, selected_publication_id))

    panzer_func = ruletools.apply_panzer()
    panzer_func(panzer_source_file, selected_target_file)

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
