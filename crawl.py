import crawlers.vnexpress.crawler as vnexpress_crawler
import crawlers.soha.crawler as soha_crawler
import os
import re
import shutil
import sys


def fetch(dataset, dataset_path, prefix):
    for index, data in enumerate(dataset):
        filename = os.path.join(dataset_path, prefix + str(index))
        url, text = data
        if text != '':
            with open(filename, mode='w', encoding='utf-8') as f:
                print('=====')
                print('Fetching url: {}'.format(url))
                print('Writing to file: {}'.format(filename))
                f.write(text)


dataset_path = os.path.expanduser(sys.argv[1])
if os.path.isdir(dataset_path):
    shutil.rmtree(dataset_path)

os.mkdir(dataset_path)

print('===== Fetching vnexpress data =====')
vnexpress_dataset = vnexpress_crawler.crawl()
fetch(vnexpress_dataset, dataset_path, 'vnexpress-')
print('Done.')

print('===== Fetching soha data =====')
soha_dataset = soha_crawler.crawl()
fetch(soha_dataset, dataset_path, 'soha-')
print('Done.')
