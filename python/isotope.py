import os

import ruletools
import filetools


def build_isotope_grid(config, folder_path):

    content = '<div class="grid">'
    for subdir in os.listdir(folder_path):

        grid_item = os.path.join(folder_path, subdir, 'thumbnail.md')

        if not os.path.exists(grid_item):
            continue

        source_file = filetools.File(grid_item, config['PATH']['site_source'])
        target_file = ruletools.duplicate_at_target(source_file, config['PATH']['tmp'])
        target_file.change_ext('html')

        jinja_filter_path = os.path.join(config['PATH']['jinja'], 'filter')
        panzer_args = ['---panzer-support', config['PATH']['panzer']]
        working_directory = config['PATH']['panzer']

        process_func = ruletools.apply_jinja_then_panzer(
            jinja_filter_path,
            config['WEB']['baseUrl'],
            panzer_args,
            config['PATH']['tmp'],
            working_directory)

        process_func(source_file, target_file)

        content += target_file.read()

    content += '</div>'

    return content


def build_isotope_filter_button(key_filter_list):

    button = '<div class="btn-group btn-group-justified filters-button-group" role="group" aria-label="...">'

    for k, f in key_filter_list:
        button += '<div class="btn-group" role="group">'
        button += '<button type="button" class="btn btn-default" data-filter="{}">{}</button>'.format(f, k)
        button += '</div>'

    button += '</div>'

    return button


def get_isotope_js():

    isotope_js = """
    <script>
    $(document).ready( function() {

        // init Isotope
        var $grid = $('.grid').isotope({
            layoutMode: 'packery',
            itemSelector: '.grid-item',
            packery: {
              gutter: 10
            }
        });

        $('.filters-button-group').on( 'click', 'button', function() {
        var filterValue = $( this ).attr('data-filter');
        $grid.isotope({ filter: filterValue });
        });

    });
    </script>
    """

    return isotope_js
