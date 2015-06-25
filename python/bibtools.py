import os
import sys

import warnings
warnings.filterwarnings("ignore")

import configparser

import logging
logger = logging.getLogger(__name__)

import citeproc
import bibtexparser


ENTRYTYPE = ['thesis', 'article', 'conference', 'inproceedings']
ENTRYTITLE = ['Thesis', 'Journals', 'Conferences', 'Workshops']


def homogeneize_bibfile(bibfile):
    parser = bibtexparser.bparser.BibTexParser()
    parser.customization = bibtexparser.customization.homogeneize_latex_encoding
    with open(bibfile) as f:
        bibtexparserinfo = bibtexparser.load(f, parser=parser)
    with open(bibfile, 'w') as f:
        bibtexparser.dump(bibtexparserinfo, f)


def read_bibfile(bibfile):
    parser = bibtexparser.bparser.BibTexParser()
    parser.customization = bibtexparser.customization.convert_to_unicode
    with open(bibfile) as f:
        bibtexparserinfo = bibtexparser.load(f, parser=parser)
    return bibtexparserinfo.entries[0]


def add_linkinfo(bibinfo, linkfile):
    config = configparser.ConfigParser()
    config.read(linkfile)
    bibinfo['link'] += config.items('LINK')


def link_to_md(link):
    ext = os.path.splitext(os.path.basename(link[1]))[1][1:]
    html_link = '<a href='
    if link[0] in ['abstract']:
        html_link += '"{}">'.format(link[1])
    else:
        if ext in ['pdf']:
            html_link += '"https://docs.google.com/viewer?url={}"  target="_blank">'.format(link[1])
        else:
            html_link += '"{}" target="_blank">'.format(link[1])

    html_link += '[{}]</a>'.format(link[0])

    return html_link


def all_links_to_md(links):
    md = ''
    for l in links:
        md += link_to_md(l)
        md += ' '
    return md


def bibinfo_to_md(bibinfo, bibfile, stylefile):

    bib_source = citeproc.source.bibtex.BibTeX(bibfile)
    bib_style = citeproc.CitationStylesStyle(stylefile, validate=False)
    bibliography = citeproc.CitationStylesBibliography(bib_style,
                                                       bib_source,
                                                       citeproc.formatter.plain)

    citation = citeproc.Citation([citeproc.CitationItem(bibinfo['id'])])
    bibliography.register(citation)

    md = str(bibliography.bibliography()[0])

    if 'info' in bibinfo:
        md += ' ' + bibinfo['info'] + '.'

    if 'award' in bibinfo:
        md += ' **' + bibinfo['award'] + '**'

    if 'link' in bibinfo:
        md += '<p>'
        md += all_links_to_md(bibinfo['link'])
        md += '</p>'

    return md


def bibinfo_to_paper_page(bibinfo):
    page_md = '---\nstyle: Default\n---'
    page_md += '\n\n'
    page_md += '## ' + bibinfo['title'].replace("{", "").replace("}", "")
    page_md += '\n\n'
    page_md += '**Authors:** ' + bibinfo['author']
    page_md += '\n\n'
    page_md += '**Abstract:** ' + bibinfo['abstract']
    page_md += '\n\n'
    if 'link' in bibinfo:
        page_md += all_links_to_md(bibinfo['link'])

    return page_md


def process_all_pubs(config, source_file, target_file):

    sys.path.append(config['PATH']['python'])

    import filetools
    import ruletools

    stylefile = config['PATH']['bibstyle']
    tmpfile_refpath = config['PATH']['tmp']

    subfolders = [x[0] for x in os.walk(source_file.dirname)]

    bibdatabase = bibtexparser.bibdatabase.BibDatabase()
    pubs = []
    for folder in subfolders:

        bibfile = os.path.join(folder, 'bibtex.bib')
        if not os.path.exists(bibfile):
            continue

        homogeneize_bibfile(bibfile)

        bibinfo = read_bibfile(bibfile)

        bibdatabase.entries.append(bibinfo.copy())

        # adding bib link to bib in .txt to view in browser
        biblinkfile = filetools.File(bibfile, source_file.refpath)
        content = biblinkfile.read()
        biblinkfile.change_ext('txt')
        biblinkfile.change_refpath(target_file.refpath)
        biblinkfile.write(content)
        bibinfo['link'] = [('bib', biblinkfile.abspathfromref)]

        #
        linkfile = os.path.join(folder, 'link.cfg')
        if os.path.exists(linkfile):
            add_linkinfo(bibinfo, linkfile)

        # making paper page
        paper_page_source_file = filetools.File(bibfile, source_file.refpath)
        paper_page_source_file.change_filename('index.md')

        panzer_source_file = paper_page_source_file.duplicate(tmpfile_refpath)

        panzer_source_file.write(bibinfo_to_paper_page(bibinfo))

        paper_page_target_file = paper_page_source_file.duplicate(target_file.refpath)
        paper_page_target_file.change_ext('html')

        panzer_refpath = config['PATH']['panzer']
        panzer_args = ['---panzer-support', panzer_refpath]

        panzer_func = ruletools.apply_panzer(panzer_args)
        panzer_func(panzer_source_file, paper_page_target_file)

        #
        bibinfo['link'].insert(0, ('abstract', config['WEB']['baseUrl'] + paper_page_target_file.absdirnamefromref))

        bibinfo['md'] = bibinfo_to_md(bibinfo, bibfile, stylefile)

        # fixing some type issue for thesis
        if 'thesis' in bibinfo['type']:
            bibinfo['type'] = 'thesis'

        pubs.append(bibinfo)

    return pubs, bibdatabase


def sort_pubs_per_year(pubs):
    def bibyearkey(item):
        return item['year']
    pubs_sorted = sorted(pubs, key=bibyearkey, reverse=True)
    return pubs_sorted


def sort_pubs_per_type(pubs):
    def bibentrytypekey(item):
        for i, entrytype in enumerate(ENTRYTYPE):
            if item['type'] == entrytype:
                return i
        logger.error('Entry {} is not supported'.format(item['type']))
    pubs_sorted = sorted(pubs, key=bibentrytypekey)
    return pubs_sorted


def pubs_to_md_per_year(pubs):

    sorted_pubs = sort_pubs_per_year(sort_pubs_per_type(pubs))

    md = "<div id='peryear'> \n"
    current_year = None
    for pub in sorted_pubs:
        if current_year != pub['year']:
            current_year = pub['year']
            md += '## ' + current_year + '\n\n'

        md += '- ' + pub['md'] + '\n\n'
    md += '</div>'

    return md


def pubs_to_md_per_type(pubs):

    sorted_pubs = sort_pubs_per_type(sort_pubs_per_year(pubs))

    md = "<div id='pertype'> \n"
    current_type = ''
    for pub in sorted_pubs:
        if current_type != pub['type']:
            current_type = pub['type']
            type_index = ENTRYTYPE.index(current_type)
            md += '## ' + ENTRYTITLE[type_index] + '\n\n'

        md += '- ' + pub['md'] + '\n\n'
    md += '</div>'

    return md


def pubs_to_md_selected(pubs, selected_publication_id):

    md = "<div id='selected'> \n"
    md += '## Selected Publications\n\n'
    for pub_id in selected_publication_id:

        func = lambda p: p['id'] == pub_id
        match_pub = list(filter(func, pubs))[0]

        md += '- ' + match_pub['md'] + '\n\n'

    return md
