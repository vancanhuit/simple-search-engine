import crawlers.vnexpress.crawler as vnexpress_crawler
import crawlers.thanhnien.crawler as thanhnien_crawler
import crawlers.vietnamnet.crawler as vietnamnet_crawler
import crawlers.laodong.crawler as laodong_crawler
import os
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

print('===== Fetching thanhnien data')
thanhnien_dataset = thanhnien_crawler.crawl()
fetch(thanhnien_dataset, dataset_path, 'thanhnien-')
print('Done.')

print('===== Fetching vietnamnet data')
vietnamnet_dataset = vietnamnet_crawler.crawl()
fetch(vietnamnet_dataset, dataset_path, 'vietnamnet-')
print('Done.')

print('===== Fetching laodong data')
laodong_dataset = laodong_crawler.crawl()
fetch(laodong_dataset, dataset_path, 'laodong-')
print('Done.')
