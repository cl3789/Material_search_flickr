import os
from pathlib import Path
from PIL import Image
import requests
import matplotlib.pyplot as plt

from os import listdir,makedirs
from os.path import isfile,join
import fnmatch


img = Image.open('../images/soap_bar_yellow/2761684_cddcf04a9b_b.jpg')
save_path = '../images/soap_bar/2761684_cddcf04a9b_b.jpg.jpg'
#bad_path = '../images/bad_sample/2761684_cddcf04a9b_b.jpg'

url = "https://live.staticflickr.com/3048/3071076037_2acf5bcd16_o.jpg"

dir = "/Users/chenxiliao/Dropbox/Projects/Search_Google_img/flickr_scraper/images/soap_translucent/"
bad_img_name = "2761684_cddcf04a9b_b.jpg"
current_dir = os.getcwd()
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
f_bad = os.path.join(parent_dir, "images", "bad_sample", bad_img_name)

path_bad = os.path.join(parent_dir, "images", "bad_sample")
files = list(filter(lambda f: isfile(join(path_bad,f)), listdir(path_bad)))
#print(files)



def existing_good_images(refined_img_path):
    refine_img = []
    for root, dirs, files in os.walk(refined_img_path):  # replace the . with your starting directory
        for file in files:
            if fnmatch.fnmatch(file, '*.jpg'):
                refine_img.append(file)
    return refine_img

refined_img_name = existing_good_images("/Users/chenxiliao/Dropbox/Projects/Search_Google_img/flickr_scraper/images/soap_refined_batch")
print(len(refined_img_name))

# if bad_img_name in files:
#     print("In the bad folder")
#
# #print(os.pardir)
#
# if os.path.exists(save_path):
#     print("it exists")
#     pass
# if os.path.exists(f_bad):
#     print("it's a bad pic")
#     pass
# else:
#     with open(save_path, 'wb') as file:
#         file.write(requests.get(url, timeout=10).content)

