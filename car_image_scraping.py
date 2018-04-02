# -*- coding: utf-8 -*-
from selenium import webdriver
from bs4 import BeautifulSoup
import time
import csv
import pandas as pd
from selenium.common.exceptions import UnexpectedAlertPresentException
from urllib.request import urlopen

class start:
    def __init__(self, interval=60):
        self.car_brand = ""
        options = webdriver.ChromeOptions()
        options.add_argument('headless')
        options.add_argument('window-size=1920x1080')
        options.add_argument("disable-gpu")
        options.add_argument("user-agent=Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_6) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/61.0.3163.100 Safari/537.36")
        self.list_out = []
        self.driver = webdriver.Chrome('/Users/wonjunhui/Downloads/chromedriver',chrome_options=options)
        self.driver.implicitly_wait(3)
        self.car_brand_click()

    def car_brand_click(self):
        self.driver.get('https://auto.naver.com/car/mainList.nhn?isMnfcoAll=Y')

        # self.driver.find_element_by_xpath('//*[@id="_vendor_select_layer"]/div/div[1]/div[6]/button[2]').click() # 두번째 제조사 페이지 이동시 사용
        #
        # self.driver.find_element_by_xpath('//*[@id="_vendor_select_layer"]/div/div[1]/div[6]/button[2]').click()
        # // *[ @ id = "_vendor_select_layer"] / div / div[1] / div[2] / ul / li[1] / a
        # // *[ @ id = "content"] / div[1] / ul / li[2] / a

        # time.sleep(2)
        ul = self.driver.find_element_by_xpath('//*[@id="_vendor_select_layer"]/div/div[1]/div[2]/ul') # 첫번째 제조사 리스트
        # // *[ @ id = "_vendor_select_layer"] / div / div[1] / div[2] / ul
        # // *[ @ id = "_vendor_select_layer"] / div / div[1] / div[3] / ul
        # // *[ @ id = "_vendor_select_layer"] / div / div[1] / div[4] / ul
        lists = ul.find_elements_by_css_selector('li')
        print(str(len(lists))+"개")
        for i in range(1,len(lists)):
            # print("hi"+str(i))
            self.car_brand = ""
            self.car_brand = self.driver.find_element_by_xpath(
                '//*[@id="_vendor_select_layer"]/div/div[1]/div[2]/ul/li['+str(i)+']/a/span').text
            # // *[ @ id = "_vendor_select_layer"] / div / div[1] / div[2] / ul / li[1] / a / span
            # print(self.car_brand)
            # // *[ @ id = "_vendor_select_layer"] / div / div[1] / div[3] / ul / li[2] / a
            self.driver.find_element_by_xpath('//*[@id="_vendor_select_layer"]/div/div[1]/div[2]/ul/li['+str(i)+']/a').click()
            self.driver.find_element_by_xpath('//*[@id="content"]/div[1]/ul/li[2]/a').click()
            # // *[ @ id = "_vendor_select_layer"] / div / div[1] / div[3] / ul / li[1] / a
            # // *[ @ id = "_vendor_select_layer"] / div / div[1] / div[3] / ul / li[1]ㅇ
            # // *[ @ id = "_vendor_select_layer"] / div / div[1] / div[3] / ul / li[2] / a
            self.car_image_scrap()
            time.sleep(2)
            self.driver.back()
            self.driver.get('https://auto.naver.com/car/mainList.nhn?isMnfcoAll=Y')
            # self.driver.find_element_by_xpath(
            #     '//*[@id="_vendor_select_layer"]/div/div[1]/div[6]/button[2]').click()  # 두번째 제조사 페이지 이동시 사용
            # self.driver.find_element_by_xpath(
            #     '//*[@id="_vendor_select_layer"]/div/div[1]/div[6]/button[2]').click()  # 두번째 제조사 페이지 이동시 사용

            # self.driver.find_element_by_xpath('//*[@id="_vendor_select_layer"]/div/div[1]/div[6]/button[2]').click()
            # self.driver.find_element_by_xpath('//*[@id="_vendor_select_layer"]/div/div[1]/div[6]/button[2]').click()

    def car_image_scrap(self):
        # print(self.driver.current_url)
        # // *[ @ id = "modelListArea"] / ul / li[1] / div / div / span / a
        # // *[ @ id = "modelListArea"] / ul / li[2] / div / div / span / a
        page_url = self.driver.current_url
        try:

            for page in range(1,21):
                self.driver.get(page_url+"&page="+str(page))
                html = urlopen(page_url+"&page="+str(page))
                time.sleep(5)
                source = BeautifulSoup(html.read(), "html.parser")
                ul = source.find("ul", class_="model_lst")
                lists = ul.findAll("div",class_="model_ct")
                # print(lists)
                # for car in lists:
                #     try:
                #         span = car.find("span", class_="thmb")
                #         # print(car)
                #         img = span.find("img")
                #         # img = a_tag.find('img')
                #         print(img['alt'] + ":" +img['src'])
                #         f = open('car_img_1.txt', 'a')
                #         # f.write(name_detail.text.split(' ')[1:].join + '\n')
                #         f.write(self.car_brand + "|" + img['alt'] + "|" + img['src'] +'\n')
                #         f.close()
                #     except Exception as e:
                #         print(str(e))

                for count in range(1,len(lists)+1):
                    # print("lists:"+str(len(lists)))
                    try:
                        self.driver.find_element_by_xpath('//*[@id="modelListArea"]/ul/li['+str(count)+']/div/div/span/a').click()
                        # // *[ @ id = "modelListArea"] / ul / li[1] / div / div / span / a
                        # // *[ @ id = "modelListArea"] / ul / li[1] / div / div / span / a
                        car_name_detail = self.driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/div[1]/h3')
                        print(car_name_detail.text)

                        html_2 = urlopen(self.driver.current_url)
                        source_2 = BeautifulSoup(html_2.read(),"html.parser")
                        div = source_2.find("div",class_="main_img")
                        img = div.find('img')['src']
                        car_brand = self.driver.find_element_by_xpath('//*[@id="container"]/div[2]/div[1]/span/a[1]').text
                        print("브랜드:"+car_brand)
                        self.list_out.append(
                            {'car_brand_name': car_brand, 'car_name': car_name_detail.text, 'img_src': img})
                        pandasFrame = pd.DataFrame(self.list_out)
                        pandasFrame.to_csv('car_images_3.csv')

                        # img = self.driver.find_element_by_xpath('//*[@id="carMainImgArea"]/div/img')
                        print(img)

                    except Exception as e:
                        print("이미지 크롤링 실패 : "+str(e))

                    self.driver.back()
                    print(count)

        except Exception as e:
            print("페이지 없음:"+str(e))

            time.sleep(5)

start(interval=10)

# //*[@id="_vendor_select_layer"]/div/div[1]/div[2]/ul/li[1]/a
# //*[@id="_vendor_select_layer"]/div/div[1]/div[2]/ul/li[2]/a
# //*[@id="modelListArea"]/ul/li[1]/div/div/span/a/img
# //*[@id="modelListArea"]/ul/li[2]/div/div/span/a/img
