import os, sys
from flask import Flask, request
import requests
import datetime
from bs4 import BeautifulSoup
import urllib
import urllib2
from selenium import webdriver

url = 'https://www.supremenewyork.com'
now = datetime.datetime.now()
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

shop = soup.find('a', attrs = {'class':'shop_link'})
shop_suffix = shop['href']
shop_url = url + shop_suffix
shop_data = urllib2.urlopen(shop_url)

chrome_path = "C:\Users\jinwu\Downloads\chromedriver.exe"
driver = webdriver.Chrome()
driver.get('http://www.google.com/xhtml');
#driver.get(driver,url)
#print(shop_data)


