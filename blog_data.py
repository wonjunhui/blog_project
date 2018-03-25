# import selenium
import os
import time
from selenium import webdriver
from bs4 import BeautifulSoup as bs
import requests
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.keys import Keys


class start_blog:
    def __init__(self):
        self.data = []
        self.driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver')
        self.driver.implicitly_wait(3)
        self.keywords = []
        # self.keyword_mining()
        self.keyword_mining()


    def keyword_mining(self):
        self.driver.get('https://datalab.naver.com/keyword/realtimeList.naver?where=main')
        # time.sleep(10)
        keyword_list = self.driver.find_element_by_xpath('//*[@id="content"]/div/div[3]/div/div/div[4]/div/div/ul')
        # keyword_list = keyword_list.find_elements_by_css_selector('ul.rank_list')
        keyword_list_1 = keyword_list.find_elements_by_css_selector('li.list')
        # print(keyword_list_1[0].text)
        for count in range(0, len(keyword_list_1)):
            # print(content)
            # count = str(count)
            print(keyword_list_1[count].text)
            self.keywords.append(keyword_list_1[count].text)
        # self.driver.close()
        time.sleep(1)
        # self.login()
        self.news_scraping()
            # // *[ @ id = "content"] / div / div[3] / div / div / div[4] / div / div / ul / li[2]
            # print(keyword_list.find_elements_by_css_selector('span.title'))
        # driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()

    def parse_blog(self):
        req = requests.get('https://datalab.naver.com/keyword/realtimeList.naver')
        html = req.text
        soup = bs(html, 'html.parser')
        my_titles = soup.find_all(class_='keyword_rank select_date')
        # print(soup.find_all(
        #     class_='sister'))  # [<a class="sister" href="http://example.com/elsie" id="link1">Elsie</a>, <a class="sister" href="http://example.com/lacie" id="link2">Lacie</a>, <a class="sister brother" href="http://example.com/tillie" id="link3">Tillie</a>]
        print(soup)
        # data = {}
        # for title in my_titles:
        #     data[title.text] = title.get('href')
        #     print(title.text)




    def login(self):
        self.driver.get('https://nid.naver.com/nidlogin.login')
        self.driver.find_element_by_name('id').send_keys('wnwjqpower')
        self.driver.find_element_by_name('pw').send_keys('wnsgml!59')
        # 로그인 버튼을 눌러주자.
        self.driver.find_element_by_xpath('//*[@id="frmNIDLogin"]/fieldset/input').click()
        self.driver.get('https://section.blog.naver.com/BlogHome.nhn?directoryNo=0&currentPage=1&groupId=0')

        self.driver.switch_to.window(self.driver.window_handles[0]) #새창떴을때 제거하는 로직
        # self.driver.close(self.driver.window_handles[1])
        # self.driver.close()

        # self.driver.find_element_by_xpath('//*[@id="container"]/div/aside/div/div[1]/nav/a[2]').click()
        self.driver.get('https://blog.naver.com/wnwjqpower')
        time.sleep(2)
        self.driver.switch_to.frame("mainFrame")  # iframe 으로 되어있음.
        self.driver.find_element_by_xpath('//*[@id="post-admin"]/a[1]').click()
        self.driver.switch_to.frame("mainFrame")  # iframe 으로 되어있음.

        title = self.driver.find_element_by_name('post.title')
        title.click()
        title.send_keys(" - 타이틀 -")
        self.driver.find_element_by_xpath('//*[@id="se2_tool"]/div[2]/ul[3]/li[2]/button').click()
        self.driver.switch_to.frame('se2_iframe')
        index = self.driver.find_element_by_class_name('se2_inputarea')
        for count in self.keywords:
            index.send_keys(count+'\n')
        time.sleep(100)

        print("성공")
        # time.sleep(5)

    def news_scraping(self):
        self.driver.get('https://search.naver.com/search.naver?where=nexearch&query=%EB%B6%80%EC%9E%A3%EC%A7%91%20%EC%95%84%EB%93%A4')
        news_list = self.driver.find_element_by_css_selector('div.news.section')
        news = news_list.find_elements_by_class_name('type01')
        # news= self.driver.find_element_by_xpath('//*[@id="main_pack"]/div[3]/ul')
        # li = news.find_elements_by_tag_name("li")
        # print(str(len(li)))
        # print(news)
        i=0
        for te in news:
            # dl = te.find_element_by_css_selector('dl')
            dt = te.find_elements_by_css_selector('dt')
            for title in dt:
                print(title.text+'\n')
            i=i+1

        # req = requests.get('https://search.naver.com/search.naver?where=nexearch&query=%EB%B6%80%EC%9E%A3%EC%A7%91%20%EC%95%84%EB%93%A4')
        # html = req.text
        # soup = bs(html, 'html.parser')
        # my_titles = soup.find_all(class_='news section')
        # print(soup)


start_blog()