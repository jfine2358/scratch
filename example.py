import os
import subprocess
import time
from tools import get_random_arxiv_id
from tools.arxivid import ArxivId
from tools import Store

old_style_id = 'hep-th/9306093'
new_style_id = '2103.15231'

random_ids = [
    ArxivId('0704.1336'),
    ArxivId('1712.03021'),
    ArxivId('1105.0038'),
    ArxivId('physics/9708005'),
    ArxivId('0910.4716'),
    ArxivId('1912.06234'),
    ArxivId('hep-ph/9807544'),
    ArxivId('hep-ph/0112226'),
    ArxivId('1609.09637'),
    ArxivId('2112.14349'),
]

articles = Store('articles')

for id in random_ids:
    break
    articles.mkdir(id)


results = []

key = 'source'
key = 'html_log'
key = 'pdf'
for id in random_ids:

    file_name = f'{id.dir_name}.{key}'
    file_path = os.path.join(articles.root, id.dir_name, file_name)

    url = getattr(id.urls, key)
    print(f'curl -o {file_path} {url}')

    args = ['curl', '-o', file_path, url]
    print(args)
    completed  = subprocess.run(args)
    results.append(completed)
    time.sleep(10)
