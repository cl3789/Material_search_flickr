# Introduction

Search translucent materials from Flickr.

# Requirements

Python 3.7 or later with all of the `pip install -U -r requirements.txt` packages including:
- `flickrapi`

# Install
```bash
$ git clone https://github.com/cl3789/Material_search_flickr.git
$ cd Material_search_flickr
$ pip install -U -r requirements.txt
```

# Run

1. Request a Flickr API key: https://www.flickr.com/services/apps/create/apply

2. Write your API key and secret in `flickr_scraper.py` L11-L12:
```python
key = ''
secret = ''
```

3. Change the path name in `general.py` in `utils` L28:
```python
path_good_img = "/Users/chenxiliao/Dropbox/Projects/Search_Google_img/flickr_scraper/images/soap_refined_batch"
```

4. Search for up to `n` images, and optionally `--download`. URLs are printed to screen and downloaded images are saved in `flickr_scraper/images`. Note that image downloads may be subject to Flickr rate limits and other limitations. See https://www.flickr.com/services/developer/api/ for full information.

```bash
$ python3 flickr_scraper.py --search 'honeybees on flowers' --n 10 --download

0/10 https://live.staticflickr.com/21/38596887_40df118fd9_o.jpg
1/10 https://live.staticflickr.com/4800/40729137901_5dafdc039f_o.jpg
2/10 https://farm8.staticflickr.com/7428/27138770446_6618c10ffb_b.jpg
3/10 https://live.staticflickr.com/925/29647053658_728134f6ca_o.jpg
4/10 https://live.staticflickr.com/1732/27535176747_78b83536af_o.jpg
5/10 https://live.staticflickr.com/7850/47160160332_6b0c88e207_o.jpg
6/10 https://live.staticflickr.com/1919/44312457665_6f7b6c2c42_o.jpg
7/10 https://live.staticflickr.com/7922/46297818725_21c13a3629_o.jpg
8/10 https://live.staticflickr.com/8045/29760999676_e71c938283_o.jpg
9/10 https://live.staticflickr.com/1770/43276172331_e779b8c161_o.jpg
Done. (4.1s)
All images saved to /Users/glennjocher/PycharmProjects/flickr_scraper/images/honeybees_on_flowers/
```

5. To move around the downloaded images, please see `Download Image data preprocess.ipynb` for instructions.



# Reference
It's modified based on [ultralytics's flickr_scraper](https://github.com/ultralytics/flickr_scraper)
