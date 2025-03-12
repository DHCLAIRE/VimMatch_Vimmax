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
#import time
#import pandas as pd
from webdriver_manager.chrome import ChromeDriverManager

if __name__ == "__main__":
    # Set up Selenium WebDriver
    options = Options()
    options.add_argument("--headless")  # Run in background
    options.add_argument("--disable-blink-features=AutomationControlled")
    
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()), options=options)
    
    # Open the website
    driver.get("https://directory.nationalrestaurantshow.com/8_0/explore/exhibitor-gallery.cfm?featured=false")
    
    time.sleep(5)  # Wait for the page to load
    
    # Scroll down to load more exhibitors (modify as needed)
    for _ in range(10):  # Adjust range based on number of exhibitors
        driver.find_element(By.TAG_NAME, "body").send_keys(Keys.END)
        time.sleep(3)
        print(int(_))
    
    # Extract exhibitor data
    exhibitors = driver.find_elements(By.CLASS_NAME, "exhibitor-card")
    
    data = []
    for exhibitor in exhibitors:
        name = exhibitor.find_element(By.TAG_NAME, "h3").text.strip()
        booth = exhibitor.find_element(By.CLASS_NAME, "booth-number").text.strip()
        website = exhibitor.find_element(By.CLASS_NAME, "website-link").get_attribute("href")
    
        data.append({"Name": name, "Booth": booth, "Website": website})
    
    # Save to CSV
    df = pd.DataFrame(data)
    df.to_csv("exhibitors_selenium.csv", index=False)
    
    print("Data saved to exhibitors_selenium.csv")
    
    # Close the browser
    driver.quit()