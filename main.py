import os, sys
from flask import Flask, request
import requests
import datetime
from bs4 import BeautifulSoup
from user import Users
from profile import profile_name
from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

category = "skate" #from config.py
keyword = 'Fruit'
user = Users(profile_name)

#set datetime
now = datetime.datetime.now()
root_url = 'https://www.supremenewyork.com'
category_url = 'https://www.supremenewyork.com/shop/all/{}'.format(category)

#start the browser
driver = webdriver.Chrome(ChromeDriverManager().install())

#into the category_url
driver.get(category_url)
#search keywork
driver.find_element_by_partial_link_text(keyword).click()
driver.implicitly_wait(1) # seconds

#add to cart
driver.find_element_by_xpath("//input[@name='commit'][@class='button']").click()
driver.implicitly_wait(1)
driver.find_element_by_xpath("//a[@class='button checkout']").click()

#autofill checkout page
name = driver.find_element_by_id('order_billing_name')
email = driver.find_element_by_id('order_email')
tel = driver.find_element_by_id('order_tel')
address = driver.find_element_by_id('bo')
oba3 = driver.find_element_by_id('oba3')
zip = driver.find_element_by_id('order_billing_zip')
city = driver.find_element_by_id('order_billing_city')
card_number = driver.find_element_by_name('credit_card[nlb]')

name.send_keys(user.name)
email.send_keys(user.email)
tel.send_keys(user.tel)
address.send_keys(user.address[0])
oba3.send_keys(user.address[1])
zip.send_keys(user.address[2])
city.send_keys(user.address[3])
card_number.send_keys(user.card[0])

#driver.find_element_by_xpath("//ins[@name='order[terms]']").click()
#atc = soup.find('a', attrs = {'class':'shop_link'})
#atc = driver.find_element_by_xpath("htme/body/div/div/div[2]/div/form/fieldset[2]//input/@type='submit']")
#atc = item.find_element_by_xpath("//input[@class='button']").click()


"""
category_item = soup.findAll('a', attrs = {'class':'name-link'})
#for each_item in category_item:
    item_name = each_item.getText()
    link_suffix = each_item['href']
    item_link = root_url +link_suffix
    #print(item_link)
    driver = webdriver.Chrome(ChromeDriverManager().install())
    driver.get(category_url)
    driver.find_element_by_partial__text(keyword).click()
"""


"""
#webdriver.get
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.find_element_by_link_text('shop').click()

email = driver.find_element_by_id('email')

email.send_keys(my_email)

driver.find_element_by_name("commit").click()
"""

"""
shop = soup.find('a', attrs = {'class':'shop_link'})
shop_suffix = shop['href']
shop_url = url + shop_suffix
#shop_data = urllib2.urlopen(shop_url)
"""
#webbrowser.open(shop_url)
