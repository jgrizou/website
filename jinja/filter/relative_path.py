import os

import jinja2


@jinja2.contextfilter
def relative_path(context, path):
    return os.path.join(context.parent['filepath'], path)
