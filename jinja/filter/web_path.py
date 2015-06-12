import os

import jinja2


@jinja2.contextfilter
def web_path(context, path):
    if os.path.isabs(path):
        path = context.parent['baseUrl'] + path
    return path
