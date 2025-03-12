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

## Web/App Libraries ##
from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello Flask!"

if __name__ == "__main__":
    app.run()