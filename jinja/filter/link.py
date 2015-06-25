import jinja2


@jinja2.contextfilter
def viewonline(context, src):
    return "https://docs.google.com/viewer?url={}".format(src)
