import datetime

import jinja2


@jinja2.contextfilter
def date(context, dummy):
    return datetime.datetime.now().strftime("%c")
