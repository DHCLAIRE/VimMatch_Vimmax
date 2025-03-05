#!/usr/bin/env python3
# -*- coding:utf-8 -*-


import sys, re

from pprint import pprint
import csv
import json
import random
from random import sample
import os
#from gtts import gTTS
import pandas as pd
import time
from pathlib import Path
#import nltk
import re
#from nltk import sent_tokenize
#from nltk import tokenize
#from pyzhuyin import pinyin_to_zhuyin  #, zhuyin_to_pinyin

if __name__ == "__main__":
    pdf_datapath = Path("/Users/ting-hsin/Downloads/Vimmax/wetransfer_vimmax-catalogue_2025-03-05_0616")
    
    with open (pdf_datapath / "VIMMAX_ TABLEWARE_DOUBLE WALL STAINLESS STEEL SERIES_CATALOGUE_01_V1-3.pdf") as pdf_catlog:
        