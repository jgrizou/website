import jinja2

BOOTSTRAP_EMBED = """
<div class="jinja-video">
<div class="embed-responsive embed-responsive-16by9">
<iframe class="embed-responsive-item" src="{}" allowfullscreen></iframe>
</div>
</div>
"""


@jinja2.contextfilter
def video(context, src):
    return BOOTSTRAP_EMBED.format(src)
