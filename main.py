import os, sys
from flask import Flask, request
import requests
import datetime
from bs4 import BeautifulSoup
import urllib
import webbrowser
#import urllib2
from selenium import webdriver
#from selenium.webdriver.common.keys import keys
from webdriver_manager.chrome import ChromeDriverManager
driver = webdriver.Chrome(ChromeDriverManager().install())

url = 'https://www.supremenewyork.com'
now = datetime.datetime.now()
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

driver.get(url)

shop = soup.find('a', attrs = {'class':'shop_link'})
shop_suffix = shop['href']
shop_url = url + shop_suffix
#shop_data = urllib2.urlopen(shop_url)

#webbrowser.open(shop_url)
