import os
from urllib.request import urlopen as open_url
import requests
from . import ArxivId

class Store:


    def __init__(self, root):

        self.root = root

    def mkdir(self, arxiv_id):

        urls = arxiv_id.urls
        dir_name = arxiv_id.dir_name
        dir_path = os.path.join(self.root, dir_name)

        os.mkdir(dir_path)


if False:


    # The rest of this code has problems. Getting IncompleteRead.

        keys = ['html', 'html_log']
        for key in keys:

            file_name = f'{dir_name}.{key}'
            file_path = os.path.join(dir_path, file_name)

            print(arxiv_id, key)

            #https://requests.readthedocs.io/en/latest/user/quickstart/#raw-response-content
            src = getattr(urls, key)
            conn = requests.get(src, stream=True)
            with open(file_path, 'wb') as fd:
                for chunk in conn.iter_content(chunk_size=128):
                    fd.write(chunk)
