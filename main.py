import os, sys
from flask import Flask, request
import requests
import datetime
#from bs4 import BeautifulSoup
from user import Users
from profile import profile_name
from setup import Setup
from config import config
from selenium import webdriver
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


user = Users(profile_name)
setup = Setup(config)
category = setup.category
keyword = setup.keyword
color = setup.color
size = setup.size

options = webdriver.ChromeOptions()
options.add_argument('user-data-dir=C:\\Users\\jinwu\\AppData\\Local\\Google\\Chrome\\User Data')

#set searching url
category_url = 'https://www.supremenewyork.com/shop/all/{}'.format(category)
chrome_path = "C:\\Users\\jinwu\\.wdm\\chromedriver\\2.46\\win32/chromedriver.exe"

#start the browser
#running on new Chrome instance
driver = webdriver.Chrome(ChromeDriverManager().install())
#running on main_profile chrome
#driver = webdriver.Chrome(executable_path = chrome_path, chrome_options=options)

#open the category_url
driver.get(category_url)
start = datetime.datetime.now()

#search item with the keyword and color
item_keyword_all_colors = driver.find_elements_by_partial_link_text(keyword)
item_keyword_colors = driver.find_elements_by_partial_link_text(color)
for each_color in item_keyword_all_colors:
    for each_item in item_keyword_colors:
        if each_color.get_attribute('href') == each_item.get_attribute('href'):
            item_true_link = each_color.get_attribute('href')
            partial_true_link = item_true_link[(len(item_true_link)-9):]
            #select the item with corret color
            item_ele = driver.find_element_by_xpath("//a[contains(@href, '{}')]".format(partial_true_link)).click()
            break
        else:
            pass
driver.implicitly_wait(2) # seconds

#select sizes
size = Select(driver.find_element_by_name('s'))
size.select_by_visible_text("Large")

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
cvv= driver.find_element_by_name('credit_card[rvv]')

name.send_keys(user.name)
email.send_keys(user.email)
tel.send_keys(user.tel)
address.send_keys(user.address[0])
oba3.send_keys(user.address[1])
zip.send_keys(user.address[2])
city.send_keys(user.address[3])
card_number.send_keys(user.card[0])
month = Select(driver.find_element_by_name('credit_card[month]'))
month.select_by_value(user.card[1])
year = Select(driver.find_element_by_name('credit_card[year]'))
year.select_by_value(user.card[2])
cvv.send_keys(user.card[3])

#checkbox: term
driver.find_element_by_xpath('//*[@id="cart-cc"]/fieldset/p[2]/label/div/ins').click()

#click process payment
driver.find_element_by_xpath('//*[@id="pay"]/input').click()
finish = datetime.datetime.now()
print (finish-start)


#####################################################
