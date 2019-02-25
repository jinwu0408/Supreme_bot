import os, sys
from flask import Flask, request
import requests
import datetime
from bs4 import BeautifulSoup
import urllib
import webbrowser
#import urllib2
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

#set datetime
now = datetime.datetime.now()
url = 'https://www.supremenewyork.com'
my_email = 'jinwuewrew@gmail.com'

#BeautifulSoup.get
page = requests.get(url)
soup = BeautifulSoup(page.content, 'html.parser')

#webdriver.get
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.find_element_by_link_text('shop').click()

email = driver.find_element_by_id('email')

email.send_keys(my_email)

driver.find_element_by_name("commit").click()


"""
shop = soup.find('a', attrs = {'class':'shop_link'})
shop_suffix = shop['href']
shop_url = url + shop_suffix
#shop_data = urllib2.urlopen(shop_url)
"""
#webbrowser.open(shop_url)
