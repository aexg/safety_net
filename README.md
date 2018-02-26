# SafetyNet

## Summary
The product is intended for retrieving pages from facebook given a page
name and rating the resulting dataset for toxicity. To access facebook
pages, set environement variables `FB_APP_ID`, `FB_APP_SECRET` to the
app_id and app_secret respectively.

## Prerequisites
Python3
Install requirements by running:
```
pip3 install -r requirements.txt
```

## How to run
Run in console/terminal/shell:
```
FB_APP_ID=XXXXXXXXXX FB_APP_SECRET=XXXXXXXXXXXXXXXXXXXXXXXXXXXXXXXX python3 scrape.py
```

## Inspiration

Page scraping for facebook
http://minimaxir.com/2015/07/facebook-scraper/
https://github.com/minimaxir/facebook-page-post-scraper/blob/master/examples/how_to_build_facebook_scraper.ipynb

Moderation API from another team
https://ca-image-analyzer.herokuapp.com/api/

## ToDo

- pass dataset through api
- provide stats
- make online version
- grab wow etc ...
