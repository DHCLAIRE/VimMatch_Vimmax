#!/usr/bin/env python3
# -*- coding:utf-8 -*-

## System Libraries ##
import sys
import os

## Data Analysis Libraries ##
from pprint import pprint
import csv
import json
import random
from random import sample
import pandas as pd
import time
from pathlib import Path

## NLP Libraries ##
import re
#from gtts import gTTS
#import nltk
#from nltk import sent_tokenize
#from nltk import tokenize
#from pyzhuyin import pinyin_to_zhuyin  #, zhuyin_to_pinyin

## Web Crawler Libraries ##
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.select import Select
#import time
#import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager



if __name__ == "__main__":
    """
    # Set up Selenium WebDriver
    options = Options()
    options.add_argument("--headless")  # Run in background
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Open the website
    driver.get("https://ambiente.messefrankfurt.com/frankfurt/en/exhibitor-search.html?location=3.1%2C11.1")
    #("https://directory.nationalrestaurantshow.com/8_0/explore/exhibitor-gallery.cfm?featured=false")
    
    time.sleep(5)  # Wait for the page to load
    
    # Scroll down to load more exhibitors (modify as needed)
    for _ in range(5):  # Adjust range based on number of exhibitors
        print(int(_))
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        print(type(driver))
        print(driver)
        time.sleep(3)

    
    # Extract exhibitor data
    exhibitors = driver.find_elements(By.CLASS_NAME, "exhibitor-card")
    

    #driver = webdriver.Chrome('./chromedriver')
    
    # Set up Selenium WebDriver
    options = Options()
    options.add_argument("--headless")  # Run in background
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    driver.get('https://ambiente.messefrankfurt.com/frankfurt/en/exhibitor-search.html?location=3.1%2C11.1')  # 開啟範例網址
    a = driver.find_element(By.ID, 'a')                # 取得 id 為 a 的網頁元素 ( 按鈕 A )
    b = driver.find_element(By.CLASS_NAME, 'btn')      # 取得 class 為 btn 的網頁元素 ( 按鈕 B )
    c = driver.find_element(By.CSS_SELECTOR, '.test')  # 取得 class 為 test 的網頁元素 ( 按鈕 C )
    d = driver.find_element(By.NAME, 'dog')            # 取得屬性 name 為 dog 的網頁元素 ( 按鈕 D )
    h1 = driver.find_element(By.TAG_NAME, 'h1')        # 取得 tag h1 的網頁元素
    link1 = driver.find_element(By.LINK_TEXT, '我是超連結，點擊會開啟 Google 網站')  # 取得指定超連結文字的網頁元素
    link2 = driver.find_element(By.PARTIAL_LINK_TEXT, 'Google') # 取得超連結文字包含 Google 的網頁元素
    select = Select(driver.find_element(By.XPATH, '/html/body/select'))   # 取得 html > body > select 這個網頁元素
    
    a.click()        # 點擊 a
    print(a.text)    # 印出 a 元素的內容
    time.sleep(0.5)
    b.click()        # 點擊 b
    print(b.text)    # 印出 b 元素的內容
    time.sleep(0.5)
    c.click()        # 點擊 c
    print(c.text)    # 印出 c 元素的內容
    time.sleep(0.5)
    d.click()        # 點擊 d
    print(d.text)    # 印出 d 元素的內容
    time.sleep(0.5)
    select.select_by_index(2)  # 下拉選單選擇第三項 ( 第一項為 0 )
    time.sleep(0.5)
    h1.click()       # 點擊 h1
    time.sleep(0.5)
    link1.click()    # 點擊 link1
    time.sleep(0.5)
    link2.click()    # 點擊 link2
    print(link2.get_attribute('href'))   # 印出 link2 元素的 href 屬性
    
    data = []
    for exhibitor in exhibitors:
        name = exhibitor.find_element(By.TAG_NAME, "h3").text.strip()
        booth = exhibitor.find_element(By.CLASS_NAME, "booth-number").text.strip()
        website = exhibitor.find_element(By.CLASS_NAME, "website-link").get_attribute("href")
    
        data.append({"Name": name, "Booth": booth, "Website": website})
    
    print(data)
    
    # Save to CSV
    df = pd.DataFrame(data)
    
    df.to_csv("frankfurt_exhibitors_selenium.csv", index=False)
    
    print("Data saved to frankfurt_exhibitors_selenium.csv")
    
    # Close the browser
    driver.quit()    
    """
    
    # Set up Selenium WebDriver
    options = Options()
    options.add_argument("--headless")  # Run in the background (no browser window)
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # URL of the exhibitor directory (Change for each site)
    urls = [
        "https://ambiente.messefrankfurt.com/frankfurt/en/exhibitor-search.html?location=3.1%2C11.1",
        #"https://directory.nationalrestaurantshow.com/8_0/explore/exhibitor-gallery.cfm?featured=false"
    ]
    
    all_exhibitors = []
    
    for url in urls:
        driver.get(url)
        time.sleep(5)  # Wait for the page to load
    
        # Scroll down to load more exhibitors (modify if needed)
        for _ in range(5):  # Adjust range based on number of exhibitors >> Test the 200 first(failed) 50(failed)
            driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
            time.sleep(2)
    
        # Extract exhibitor names (modify based on website structure)
        exhibitors = driver.find_elements(By.TAG_NAME, "h3")  # Adjust tag if needed
    
        for exhibitor in exhibitors:
            name = exhibitor.text.strip()
            print(name)
            if name:
                all_exhibitors.append({"Exhibitor Name": name})
    
    # Save data to CSV
    df = pd.DataFrame(all_exhibitors)
    df.to_csv("exhibitors_list.csv", index=False)
    
    print("✅ Data saved to exhibitors_list.csv")
    
    # Close the browser
    driver.quit()
    