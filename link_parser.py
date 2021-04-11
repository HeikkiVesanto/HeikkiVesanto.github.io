import os
from pathlib import Path
from bs4 import BeautifulSoup as page_soup
import urllib.request
import csv

dir_path = os.path.dirname(os.path.realpath(__file__))

posts = 'docs\\_posts'
media = 'docs\\media'

post_dir = os.path.join(dir_path, posts)

broken_images = 'broken2.csv'

f = open(os.path.join(dir_path, broken_images), 'w')
writer = csv.writer(f)

pathlist = Path(post_dir).glob('*.html')

for path in pathlist:
    path_in_str = str(path)
    print(path_in_str)
    writer.writerow([path_in_str])
    soup = page_soup(open(path_in_str), 'html.parser')
    images = soup.findAll('a')
    post_date = path_in_str.split('\\')[-1][0:10]
    print(post_date)
    for image in images:
        # print image source
        img_name = image['href'].split('/')[-1]
        img_save_name = post_date + '_' + img_name
        if img_name.endswith('png') or img_name.endswith('jpg') or img_name.endswith('jpeg'):
            print(img_name)
            try:
                urllib.request.urlretrieve(image['href'], os.path.join(dir_path, media, img_save_name))
                with open(path_in_str, 'r') as file:
                    filedata = file.read()
                filedata = filedata.replace(image['href'], 'https://gisforthought.com/media/' + img_save_name)
                with open(path_in_str, 'w') as file:
                    file.write(filedata)
            except Exception as ex:
                writer.writerow([image['href'], 'https://gisforthought.com/media/' + img_save_name])
                with open(path_in_str, 'r') as file:
                    filedata = file.read()
                filedata = filedata.replace(image['href'], 'https://gisforthought.com/media/' + img_save_name)
                with open(path_in_str, 'w') as file:
                    file.write(filedata)

f.close()
