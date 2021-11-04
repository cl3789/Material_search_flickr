# General utilities for use in image-handling operations
# Written by Glenn Jocher (glenn.jocher@ultralytics.com) for https://github.com/ultralytics

import os
from pathlib import Path

from os import listdir,makedirs
from os.path import isfile,join
import fnmatch

import requests
from PIL import Image

current_dir = os.getcwd()
parent_dir = os.path.abspath(os.path.join(current_dir, os.pardir))
f_bad = os.path.join(parent_dir, "flickr_scraper","images", "bad_sample")
bad_files = list(filter(lambda f: isfile(join(f_bad, f)), listdir(f_bad)))

def existing_good_images(refined_img_path):
    # Get the name of good images existing in the final dataset
    refine_img = []
    for root, dirs, files in os.walk(refined_img_path):  # replace the . with your starting directory
        for file in files:
            if fnmatch.fnmatch(file, '*.jpg'):
                refine_img.append(file)
    return refine_img

path_good_img = "/Users/chenxiliao/Dropbox/Projects/Search_Google_img/flickr_scraper/images/soap_refined_batch" ## Change this to the folder where you save the good images
existing_good_images_names = existing_good_images(path_good_img)

print(existing_good_images_names)

def download_uri(uri, dir='./'):
    # Download a file from a given URI, including minimal checks

    # Download
    #f = dir + os.path.basename(uri)  # filename

    # path of bad samples
    img_name = os.path.basename(uri)

    # Skip download if the image exists
    if os.path.exists(dir+img_name):
        print("It's has been downloaded for this keyword")
        pass
    elif (img_name in existing_good_images_names):
        print("It's already in the dataset")
        pass
    elif (img_name in bad_files):
        print("It's a bad image")
        pass
    else:
        f = dir+img_name
        with open(f, 'wb') as file:
            file.write(requests.get(uri, timeout=10).content)


    #with open(f, 'wb') as file:
    #    file.write(requests.get(uri, timeout=10).content)

    # Rename (remove wildcard characters)
    src = f  # original name
    for c in ['%20', '%', '*', '~', '(', ')']:
        f = f.replace(c, '_')
    f = f[:f.index('?')] if '?' in f else f  # new name
    if src != f:
        os.rename(src, f)  # rename

    # Add suffix (if missing)
    if Path(f).suffix == '':
        src = f  # original name
        f += '.' + Image.open(f).format.lower()  # append PIL format
        os.rename(src, f)  # rename
