from crawlers.vnexpress import helpers
import os
import re
import shutil

dataset_path = os.path.join(os.getcwd(), 'dataset')
if os.path.isdir(dataset_path):
    shutil.rmtree(dataset_path)

os.mkdir(dataset_path)

urls = helpers.extract_urls()
for index, url in enumerate(urls):
    text = helpers.extract_text_from_url(url)
    if text != '':
        filename = os.path.join(dataset_path, str(index))
        with open(filename, mode='w') as f:
            f.write(text)
