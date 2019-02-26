import os, sys
from flask import Flask, request
import requests
import datetime
from bs4 import BeautifulSoup
from user import Users
from profile import profile_name
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager

category = "t-shirts" #from config.py
keyword = 'Fronts'
color = "Orange"
user = Users(profile_name)


#set datetime
now = datetime.datetime.now()
root_url = 'https://www.supremenewyork.com'
category_url = 'https://www.supremenewyork.com/shop/all/{}'.format(category)

#start the browser
driver = webdriver.Chrome(ChromeDriverManager().install())
#into the category_url
driver.get(category_url)


#search item with the keyword and color
item_keyword_all_colors = driver.find_elements_by_partial_link_text(keyword)
item_keyword_colors = driver.find_elements_by_partial_link_text(color)
for each_color in item_keyword_all_colors:
    for each_item in item_keyword_colors:
        if each_color.get_attribute('href') == each_item.get_attribute('href'):
            item_true_link = each_color.get_attribute('href')
            partial_true_link = item_true_link[(len(item_true_link)-9):]
            item_ele = driver.find_element_by_xpath("//a[contains(@href, '{}')]".format(partial_true_link)).click()
            #print("partial_true_link is: {}".format(partial_true_link))
            break
        else:
            pass
driver.implicitly_wait(1) # seconds


#add to cart
driver.find_element_by_xpath("//input[@name='commit'][@class='button']").click()
driver.implicitly_wait(1)


#click checkout
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


#click process payment


###########################################################################################


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
#webdriver.get
driver = webdriver.Chrome(ChromeDriverManager().install())
driver.get(url)
driver.find_element_by_link_text('shop').click()

email = driver.find_element_by_id('email')

email.send_keys(my_email)

driver.find_element_by_name("commit").click()
op = soup.find('a', attrs = {'class':'shop_link'})
shop_suffix = shop['href']
shop_url = url + shop_suffix
#shop_data = urllib2.urlopen(shop_url)
"""
#webbrowser.open(shop_url)
