import crawlers.vnexpress.crawler as vnexpress_crawler
import os
import re
import shutil
import sys


dataset_path = sys.argv[1]
if os.path.isdir(dataset_path):
    shutil.rmtree(dataset_path)

os.mkdir(dataset_path)

dataset = vnexpress_crawler.crawl()
for index, data in enumerate(dataset):
    filename = os.path.join(dataset_path, str(index))
    url, text = data
    if text != '':
        with open(filename, mode='w') as f:
            print('=====')
            print('Fetching url: {}'.format(url))
            print('File: {}'.format(filename))
            f.write(text)
            print('Write file done.')
