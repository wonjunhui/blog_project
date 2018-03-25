# import selenium
import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests

class start_kakao:
    def __init__(self):
        self.data = []
        self.driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver')
        self.driver.implicitly_wait(3)
        self.keywords = []
        self.login()
        # self.keyword_mining()
        # self.keyword_mining()

    def login(self):
        self.driver.get('https://accounts.kakao.com/login?continue=https%3A%2F%2Fpage.kakao.com%2Fstore%2Flogin%3FreturnUrl%3Dhttps%3A%2F%2Fpage.kakao.com')
        time.sleep(2)
        self.driver.find_element_by_name('email').send_keys('wnwjqpower@naver.com')
        self.driver.find_element_by_name('password').send_keys('wns159')
        self.driver.find_element_by_xpath('//*[@id="btn_login"]').click()
        time.sleep(10)

start_kakao()

# https://accounts.kakao.com/login?continue=https%3A%2F%2Fpage.kakao.com%2Fstore%2Flogin%3FreturnUrl%3Dhttps%3A%2F%2Fpage.kakao.com