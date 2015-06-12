import os

import jinja2


def build_portfolio(portfolio_relative_path, ordered_subfoldername_to_thumbnail, template_path, portfolio_templatename, button_text):

    env = jinja2.Environment(loader=jinja2.FileSystemLoader(template_path))

    template = env.get_template(portfolio_templatename)

    thumbnails = []
    for subdir in ordered_subfoldername_to_thumbnail:
        baselink = os.path.join(portfolio_relative_path, subdir)

        info = {'image': os.path.join(baselink, 'thumbnail.png'),
                'content': os.path.join(baselink, 'thumbnail.html'),
                'page': baselink,
                'button': button_text}

        thumbnails.append(info)

    return template.render(thumbnails=thumbnails)
