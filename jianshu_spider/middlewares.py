# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html

from scrapy import signals
from selenium import webdriver
import time
from scrapy.http.response.html import HtmlResponse

class SeleniumDownloadMiddleware(object):
    def __init__(self):
        self.driver = webdriver.Firefox(executable_path="C:\geckodriver\geckodriver.exe")

    def process_request(self, request, spider):
        self.driver.get(request.url)
        time.sleep(1)
        try:
            while True:
                showMore = self.driver.find_element_by_class_name("show-more")
                showMore.click()
                time.sleep(2)
                if not showMore:
                    break
        except:
            pass
        source = self.driver.page_source
        response = HtmlResponse(url=self.driver.current_url,body=source,request=request)
        return response
