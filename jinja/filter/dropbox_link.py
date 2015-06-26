import os

import jinja2

import dropbox
import webbrowser

app_key = '1jl40nzuuj8wtg7'
app_secret = '27j5k2im578dgpk'
access_token_file = '/tmp/website/dropbox_token.txt'


@jinja2.contextfilter
def dropbox_link(context, path):

    if not os.path.exists(os.path.dirname(access_token_file)):
        os.makedirs(os.path.dirname(access_token_file))

    if not os.path.exists(access_token_file):
        # Have the user sign in and authorize this token
        flow = dropbox.client.DropboxOAuth2FlowNoRedirect(app_key, app_secret)
        authorize_url = flow.start()
        webbrowser.open(authorize_url, new=2)
        code = input("Enter the authorization code here: ").strip()
        access_token, user_id = flow.finish(code)
        with open(access_token_file, 'w') as f:
            f.write(access_token)

    with open(access_token_file, 'r') as f:
        access_token = f.read()

    client = dropbox.client.DropboxClient(access_token)

    shareable_link = client.share(path)

    return shareable_link['url']

    # client.disable_access_token()
