import jinja2


@jinja2.contextfilter
def quote(context, quote_info):

    html = '<div class="grid-item ' + quote_info['filter'] +'">'
    html += '<blockquote class="blockquote-reverse">'
    html += '<p>' + quote_info['quote'] + '</p>'
    html += '<footer>' + quote_info['author']
    html += '<cite title="Source Title">'
    if 'source' in quote_info:
        html += ' in ' + quote_info['source']
    if 'year' in quote_info:
        html += ', ' + quote_info['year']
    html += '</cite>'
    html += '</footer>'
    html += '</blockquote>'
    html += '</div>'

    return html
