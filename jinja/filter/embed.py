import jinja2

BOOTSTRAP_YOUTUBE_EMBED = """
<div class="jinja-youtube_embed">
<div class="embed-responsive embed-responsive-16by9">
<iframe class="embed-responsive-item" src="https://www.youtube.com/embed/{}" allowfullscreen></iframe>
</div>
</div>
"""


@jinja2.contextfilter
def youtube(context, src):
    return BOOTSTRAP_YOUTUBE_EMBED.format(src)
