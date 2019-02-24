import os, sys
from flask import Flask, request
import requests
import datetime
from bs4 import BeautifulSoup
import urllib
#import urllib2
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
"""
url = 'https://www.supremenewyork.com'
now = datetime.datetime.now()
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

shop = soup.find('a', attrs = {'class':'shop_link'})
shop_suffix = shop['href']
shop_url = url + shop_suffix
shop_data = urllib2.urlopen(shop_url)
"""
#chrome_path = "\usr\local\bin\chromedriver"
chrome_options = Options()
chrome_options.add_argument("__headless")
chrome_options.add_argument('--no-sanbox')
chrome_options.add_argument('--disable-dev-shm-usage')
driver_new = webdriver.Chrome(chrome_options= chrome_options, executable_path=r'/usr/local/bin/chromedriver')


