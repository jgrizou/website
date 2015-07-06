
section_folder = 'sections'

section_ordering = ['header.md',
                    'education.md',
                    'experiences.md',
                    'awards.md',
                    'collaboration.md',
                    'publications.md',
                    'services.md',
                    'skills.md',
                    'languages.md',
                    'personal.md']


def main(config, source_file, target_file):

    import logging
    logger = logging.getLogger(__name__)
    logger.info('Building cv')

    import sys
    sys.path.append(config['PATH']['python'])

    import os
    import filetools

    for section in section_ordering:
        section_file_path = os.path.join(source_file.dirname, section_folder, section)
        section_file = filetools.File(section_file_path, source_file.refpath)
        target_file.append(section_file.read() + '\n\n')



    # write a dummy file at target to confirm good exec
    # target_file.write('<p> done </p>')



# # pandoc $compilingOrder -o cv.pdf --variable=geometry:a4paper
#
# pandoc $compilingOrder -o cv.html --standalone -c style.css
#
# wkhtmltopdf cv.html cv.pdf
#
# ###
#
# # pandoc moocs.md -o moocs.pdf --variable=geometry:a4paper
#
# pandoc moocs.md -o moocs.html --standalone -c style.css
#
# wkhtmltopdf moocs.html moocs.pdf
