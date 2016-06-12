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


BOOTSTRAP_VIMEO_EMBED = """
<div class="jinja-vimeo_embed">
<div class="embed-responsive embed-responsive-16by9">
<iframe class="embed-responsive-item" src="https://player.vimeo.com/video/{}" allowfullscreen></iframe>
</div>
</div>
"""


@jinja2.contextfilter
def vimeo(context, src):
    return BOOTSTRAP_VIMEO_EMBED.format(src)


BOOTSTRAP_VIDEO_EMBED = """
<div class="jinja-vimeo_embed">
<div class="embed-responsive embed-responsive-16by9">
<iframe class="embed-responsive-item" src="{}" allowfullscreen></iframe>
</div>
</div>
"""


@jinja2.contextfilter
def video(context, src):
    return BOOTSTRAP_VIDEO_EMBED.format(src)
