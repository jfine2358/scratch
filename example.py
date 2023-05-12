import gzip
import os
import subprocess
import time
from html.parser import HTMLParser
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

    break                       # Already populated.

    file_name = f'{id.dir_name}.{key}'
    file_path = os.path.join(articles.root, id.dir_name, file_name)

    url = getattr(id.urls, key)
    print(f'curl -o {file_path} {url}')

    args = ['curl', '-o', file_path, url]
    print(args)
    completed  = subprocess.run(args)
    results.append(completed)
    time.sleep(10)

key = 'source'
for id in random_ids:
    break                       # Done already.
    tgt_path = os.path.join(articles.root, id.dir_name, key)
    os.mkdir(tgt_path)


key = 'source'
results = []
for id in random_ids:
    break                       # Done already.

    tar_name = f'{id.dir_name}.{key}'
    tar_path = os.path.join(articles.root, id.dir_name, tar_name)
    tgt_path = os.path.join(articles.root, id.dir_name, key)

#    os.mkdir(tgt_path)

    url = getattr(id.urls, key)

    args = ['tar', '-xvzf', tar_path, '-C', tgt_path]
    print(args)
    completed  = subprocess.run(args)
    results.append(completed)

# results[2], results[4] fail with returncode 2.


key = 'source'
results = []
for id in [random_ids[2], random_ids[4]]:
    break                       # Already done.
    tar_name = f'{id.dir_name}.{key}'
    # so-called tar_path is gzip path.
    tar_path = os.path.join(articles.root, id.dir_name, tar_name)
    tgt_dir = os.path.join(articles.root, id.dir_name, key)
    tgt_path = os.path.join(tgt_dir, f'{id.dir_name}.tex')

    url = getattr(id.urls, key)

    args = ['gunzip', '--decompress', '--keep', tar_path, tgt_path]
    print(args)

    import gzip
    with gzip.open(tar_path, 'rb') as src:
        with open(tgt_path, 'wb') as tgt:
            tgt.write(src.read())

key = 'html_log'
results = []
for id in random_ids:

    break                       # Already done.

    class LogParser(HTMLParser):

        def handle_data(self, data):
            data = data.rstrip()
            data = data.lstrip('\n')
            if data:
                append(data)


    html_log_name = f'{id.dir_name}.{key}'
    html_log_path = os.path.join(articles.root, id.dir_name, html_log_name)
    html_log = open(html_log_path).read()


    html_log_txt_name = f'{id.dir_name}.{key}.txt'
    html_log_txt_path = os.path.join(articles.root, id.dir_name,
                                     html_log_txt_name)

    # print(html_log_txt_path)
    # print(len(html_log))

    parser = LogParser()
    tmp = []
    append = tmp.append
    parser.feed(html_log)
    del parser                  # Don't use it again.

    with open(html_log_txt_path, 'w') as fd:
        for line in tmp:
            fd.write(f'{line}\n')
