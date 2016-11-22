from urllib.parse import urlparse,urlsplit
import random
import time
from datetime import datetime, timedelta
import socket
from selenium import webdriver
import requests

DEFAULT_AGENT = 'al'
DEFAULT_DELAY = 5
DEFAULT_RETRIES = 1
DEFAULT_TIMEOUT = 120

class Downloader:
    def __init__(self, delay=DEFAULT_DELAY, user_agent=DEFAULT_AGENT, proxies=None, num_retries=DEFAULT_RETRIES,
                 timeout=DEFAULT_TIMEOUT):
        socket.setdefaulttimeout(timeout)
        self.throttle = Throttle(delay)
        self.user_agent = user_agent
        self.proxies = proxies
        self.num_retries = num_retries

    def __call__(self, url):
        result = None
        self.throttle.wait(url)
        proxy = random.choice(self.proxies) if self.proxies else None
        headers = {'User-agent': self.user_agent}
        result = self.download(url)

        return result

    def download(url):
        print('Downloading:', url)


         #   driver1 = webdriver.PhantomJS(
        #    executable_path='/home/henry/jobcrawler/env/bin/phantomjs-2.1.1-linux-x86_64/bin/phantomjs')
        driver1 = webdriver.PhantomJS()
        driver1.get(url)
        response = requests.get(url)
        html1 = driver1.page_source
        return html1


class Throttle:
    """Throttle downloading by sleeping between requests to same domain
    """

    def __init__(self, delay):
        # amount of delay between downloads for each domain
        self.delay = delay
        # timestamp of when a domain was last accessed
        self.domains = {}

    def wait(self, url):
        """Delay if have accessed this domain recently
        """
        domain = urlsplit(url).netloc
        last_accessed = self.domains.get(domain)
        if self.delay > 0 and last_accessed is not None:
            sleep_secs = self.delay - (datetime.now() - last_accessed).seconds
            if sleep_secs > 0:
                time.sleep(sleep_secs)
        self.domains[domain] = datetime.now()