### scrapy set-up: general set-up, required changes & customisations

In this document, I describe the process of how I set up scrapy for my thesis work - including accessing the pre-existing spiders created by A. Chai-allah in his repository [Wiki4CES](https://github.com/achaiallah-hub/Wiki4CES) - however, since the Wikiloc website changed since the creation of the Wiki4CES repo, I also provide updated spiders in this repo ([wikiloc_scrapy/wikiloc_scrapy/spiders/](wikiloc_scrapy/wikiloc_scrapy/spiders/)). For more details on the necessary changes to adapt to the new website stucture (including changes to xpath expresssions) see the comments in the spider .py files and in [rq2_step1_data_collection.ipynb](rq2_step1_data_collection.ipynb). Finally, in this document I also describe the customisations I made to avoid permission errors and make the scraping more polite.

This document is intended for use in combination with the information from [rq2_step1_data_collection.ipynb](rq2_step1_data_collection.ipynb)

Steps:
1. Install scrapy
2. Create a scrapy "Project"
3. Download spiders from Wiki4CES repo (OR updated versions from this repo)
4. Adjust scrapy settings: add default request headers 
5. Adjust scrapy settings: add delays between requests 

*Note that these instructions are based on having a conda environment with installations from the conda-forge channel only.*

#### Step 1: Install scrapy
This is simply a matter of activating the conda environment and running: *conda install scrapy*. My defaults are set to install from the conda-forge channel. 


#### Step 2: Create a scrapy "project"
To run scrapy you need to set up a scrapy "project". 

In Anaconda Prompt:

1. cd C:\Users\ninam\Documents\UZH\04_Thesis\code\nm_forest_thesis
2. conda activate C:\Users\ninam\Documents\UZH\04_Thesis\code\nm_forest_thesis\thesis_env_conda 
3. scrapy startproject wikiloc_scrapy

Helpful scrapy information: https://docs.scrapy.org/en/latest/intro/tutorial.html


#### Step 3: Download spiders from Wiki4CES repo
Next you need to add the scrapy "spiders" (the processes which crawl and scrape information from the web) as .py scripts to the directory [wikiloc_scrapy/wikiloc_scrapy/spiders/](wikiloc_scrapy/wikiloc_scrapy/spiders/). Basically, the .py scripts from the achaiallah-hub repo need to be saved in this directory. 

**IMPORTANT** These are the steps I followed initially, however I have since made changes to the original spiders, some of which are specific to my work, and some of which are **necessary to scrape the data properly (namely updates to xpath expressions and to adapt to other changes in the website structure)**. In this case it would perhaps make sense to use the information below, but instead copy/clone the updated spiders from my repo: [extract_link.py](wikiloc_scrapy/wikiloc_scrapy/spiders/extract_link.py), [extract_link_large.py](wikiloc_scrapy/wikiloc_scrapy/spiders/extract_link_large.py) and [wikiloc_track.py](wikiloc_scrapy/wikiloc_scrapy/spiders/wikiloc_track.py).

In Anaconda Prompt:

1. cd wikiloc_scrapy\wikiloc_scrapy\spiders
2. git init
3. git remote add origin git@github.com:achaiallah-hub/Wiki4CES.git
4. git pull origin main
5. Afterwards, delete the git files which are created in wikiloc_scrapy\wikiloc_scrapy\spiders (otherwise you end up working on the achiallah-hub Wiki4CES repo rather than your own repo!)

**NOTE** Instead of Steps 2-4, at first I just tried the simple command git clone https://github.com/achaiallah-hub/Wiki4CES.git This works, but it stores the .py scripts inside a repo directory folder called Wiki4CES, and I think this causes problems when trying to use the spiders later. Steps 2-4 are a work-around: this way the python scripts are directly within the "spiders" directory without being inside another directory. In order to do steps 2-4 an **ssh-key** needs to be set up. 


#### Step 4: Adjust scrapy settings: add default request headers 
The first time I tried to run the spider from extract_link.py I encountered error messages indicating HTTP Status Code 403 - Forbidden / Access Denied. As this could be an anti-scraping measure, I looked into possible solutions. I have documented both here (even though the first solution attempt didn't work), just in case any changes I made in this step had an impact later on that I was unaware of. 

**Solution Attempt 1 (Unsuccessful)**
1. pip install scrapy_cloudflare_middleware
2. edit downloader middleware in settings.py according to: https://github.com/clemfromspace/scrapy-cloudflare-middleware?tab=readme-ov-file

Error message, trying to install an older version of requests/urllib3 as per https://stackoverflow.com/questions/76414514/cannot-import-name-default-ciphers-from-urllib3-util-ssl-on-aws-lambda-us
3. conda install requests==2.28.2
4. Now try scrapy crawl command

I got this to run, but it ended up back with the 403 error messages again. The solution maybe is too old? This source seems to suggest that the cloudflare middleware solution no longer works: https://www.zenrows.com/blog/scrapy-cloudflare#conclusion

I reverted back to original set up by:
1. Commenting out the downloader middlewware in settings.py
2. ~~conda update requests~~ (just left requests as is for now)

**Solution Attempt 2 (Successful)**
Add default request headers according to https://www.zenrows.com/blog/scrapy-headers#most-important-ones . This means adding the following lines to settings.py:
DEFAULT_REQUEST_HEADERS = {
    'Accept-Language': 'en-US,en;q=0.9',
    "Referer": "https://www.google.com/",
    "Accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.7",
    "Accept-Encoding": "gzip, deflate, br",
    "Sec-Ch-Ua": "\"Not A(Brand\";v=\"99\", \"Google Chrome\";v=\"121\", \"Chromium\";v=\"121\"",
    "Sec-Ch-Ua-Platform": "\"Windows\"",
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/121.0.0.0 Safari/537.36',
        }


#### Step 5: Adjust scrapy settings: add delays between requests 
To make the scraping more polite, it is important to add delays to the request so that the website servers are not overwhelmed (which is not nice for them and also could lead to future requests from your IP address being blocked). This website provides using information on adding delays and autothrottle to scrapy spiders: https://scrapeops.io/python-scrapy-playbook/scrapy-delay-between-requests/

In the [settings.py](wikiloc_scrapy/wikiloc_scrapy/settings.py) folder the following lines should be added (these are included in the settings.py folder by default but are commented out - so you just need to uncomment these lines):

DOWNLOAD_DELAY = 2 # ~minimum delay (approximately minimum because of randomisation)
RANDOMIZE_DOWNLOAD_DELAY = True # for 2 second delay this means delay will be between 1-3 sec
AUTOTHROTTLE_ENABLED = True 
AUTOTHROTTLE_START_DELAY = 5 #initial download delay (seconds)
AUTOTHROTTLE_MAX_DELAY = 60 #maximum download delay (seconds)
AUTOTHROTTLE_TARGET_CONCURRENCY = 1.0 # The lower the number the politer your scraper

See the link above for details about how the auto-throttle works.



