import jinja2


@jinja2.contextfilter
def view_online(context, src):
    return "https://docs.google.com/viewer?url={}".format(src)


@jinja2.contextfilter
def pub(context, key):
    return context.parent['baseUrl'] + '/publications/' + key


@jinja2.contextfilter
def pub_list(context, keys):
    html = '<div>'
    for k in keys:
        html += '<a href="' + context.parent['baseUrl'] + '/publications/' + k + '" class="btn btn-default" role="button">' + k + '</a>'
    html += '</div>'
    return html
