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
import numpy as np

## NLP Libraries ##
import re
import string
#from gtts import gTTS
#import nltk
#from nltk import sent_tokenize
#from nltk import tokenize
#from pyzhuyin import pinyin_to_zhuyin  #, zhuyin_to_pinyin

# pdf
import pdfplumber
import fitz  # PyMuPDF
from pdf2image import convert_from_path
import cv2
import pytesseract

if __name__ == "__main__":
    pdf_datapath = Path("/Users/ting-hsin/Downloads/Vimmax/wetransfer_vimmax-catalogue_2025-03-05_0616")
    
    with open (pdf_datapath / "VIMMAX_ TABLEWARE_DOUBLE WALL STAINLESS STEEL SERIES_CATALOGUE_01_V1-3.pdf") as pdf_catlog:
        

        
        # Function to extract text from PDF
        def extract_text(pdf_path):
            doc = fitz.open(pdf_path)
            text = ""
            for page in doc:
                text += page.get_text("text") + "\n"
            return text
        
        # Function to extract graphs (images) from PDF
        def extract_graphs(pdf_path, output_folder="graphs"):
            images = convert_from_path(pdf_path)
            os.makedirs(output_folder, exist_ok=True)
        
            for i, image in enumerate(images):
                img_path = os.path.join(output_folder, f"page_{i+1}.png")
                image.save(img_path, "PNG")
        
                # Read image using OpenCV
                img = cv2.imread(img_path, cv2.IMREAD_GRAYSCALE)
        
                # Apply edge detection
                edges = cv2.Canny(img, 50, 150)
        
                # Find contours (potential graphs)
                contours, _ = cv2.findContours(edges, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
        
                for j, cnt in enumerate(contours):
                    x, y, w, h = cv2.boundingRect(cnt)
                    if w > 100 and h > 100:  # Filter small contours
                        graph = img[y:y+h, x:x+w]
                        cv2.imwrite(os.path.join(output_folder, f"graph_{i+1}_{j+1}.png"), graph)
        
            print(f"Graphs saved in {output_folder}")
        
        # Example Usage
        pdf_file = "sample.pdf"
        text = extract_text(pdf_file)
        print("Extracted Text:\n", text)
        
        extract_graphs(pdf_file)
    
    
    
    
    
    """   OLD Command >> Trying new ones(above)
    ### Step-by-Step: Easiest Ways to Extract Everything
    
    #### 1. Extracting Text (Selectable Text in PDFs)
    #If the PDF has native text (not scanned or image-based), this is the simplest method.
    
    #- **Using `pdfplumber` (Recommended):**
        #```python

    
        # Open the PDF file
        with pdfplumber.open("example.pdf") as pdf:
            # Loop through each page
            for page in pdf.pages:
                text = page.extract_text()
                print(f"Page {page.page_number}: {text}")
        
        #- **Why it’s easy:** `pdfplumber` handles text extraction well, preserves layout, and is beginner-friendly.
        #- **Bonus:** It can also extract tables with `page.extract_tables()`.
        
    
    #- **Alternative with `PyPDF2`:**
        #```python
        from PyPDF2 import PdfReader
    
        reader = PdfReader("example.pdf")
        for page_num in range(len(reader.pages)):
            page = reader.pages[page_num]
            text = page.extract_text()
            print(f"Page {page_num + 1}: {text}")
        #```
        #- **Why it’s easy:** `PyPDF2` is lightweight, but it’s less accurate with complex layouts compared to `pdfplumber`.
    
    #*Limitation:* These methods fail if the text is embedded in images (e.g., scanned PDFs). See OCR below for that.
    
    #---
    
    #### 2. Extracting Graphs and Images
    #PDFs often store graphs as images. The easiest way is to convert pages to images and save or process them.
    
    #- **Using `pdf2image`:**
        #```python
        from pdf2image import convert_from_path
    
        # Convert PDF pages to images
        images = convert_from_path("example.pdf", dpi=200)  # Adjust DPI for quality
    
        # Save each page as an image
        for i, image in enumerate(images):
            image.save(f"page_{i + 1}.png", "PNG")
            print(f"Saved page_{i + 1}.png")
        #```
        #- **Why it’s easy:** Converts the entire page to an image, capturing graphs, diagrams, and anything visual without needing to parse the PDF structure.
        #- **Next step:** Use these images for OCR (text extraction) or manual inspection.
    
    #---
    
    #### 3. Extracting Text from Images (Including Graphs or Scanned PDFs)
    #If text is embedded in images or graphs, use OCR with `pytesseract`.
    
    #- **Basic OCR Setup:**
        #```python
        from pdf2image import convert_from_path
        import pytesseract
        from PIL import Image
    
        # Convert PDF to images
        images = convert_from_path("example.pdf", dpi=200)
    
        # Extract text from each image
        for i, image in enumerate(images):
            text = pytesseract.image_to_string(image)
            print(f"Page {i + 1} Text: {text}")
            image.save(f"page_{i + 1}.png", "PNG")  # Optional: save the image
        #```
        #- **Why it’s easy:** `pytesseract` integrates with Python seamlessly, and `pdf2image` handles the PDF-to-image step.
        #- **Tip:** Install Tesseract OCR (`apt-get install tesseract-ocr` on Linux, `brew install tesseract` on macOS, or download for Windows) and ensure it’s in your PATH.
    
    #- **Improving OCR Accuracy:** Preprocess images (e.g., convert to grayscale) with `Pillow` or `opencv-python`:
        #```python
        import cv2
        import pytesseract
        from PIL import Image
    
        # Load image (from pdf2image output)
        image = cv2.imread("page_1.png")
        gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)  # Convert to grayscale
        text = pytesseract.image_to_string(gray)
        print(text)
        #```
    
    #---
    
    #### 4. Extracting Everything Else (Tables, Metadata, etc.)
    #- **Tables with `pdfplumber`:**
        #```python
        import pdfplumber
    
        with pdfplumber.open("example.pdf") as pdf:
            for page in pdf.pages:
                tables = page.extract_tables()
                for table in tables:
                    print(table)  # List of rows
        #```
        #- **Why it’s easy:** Automatically detects and extracts tabular data.
    
    #- **Metadata with `PyPDF2`:**
        #```python
        from PyPDF2 import PdfReader
    
        reader = PdfReader("example.pdf")
        metadata = reader.metadata
        print(metadata)  # e.g., author, creation date
        #```
        #- **Why it’s easy:** Directly accesses PDF properties.
    
    #- **Embedded Files or Annotations:** Less common, but `PyPDF2` can extract attachments if present:
        #```python
        reader = PdfReader("example.pdf")
        if reader.attachments:
            for filename, data in reader.attachments.items():
                with open(filename, "wb") as f:
                    f.write(data)
        #```
    
    #---
    
    ### Simplest Workflow for All Content
    #Here’s a combined script to extract text, graphs, and more from any PDF:
    #```python
    import pdfplumber
    from pdf2image import convert_from_path
    import pytesseract
    from PIL import Image
    
    # Step 1: Try extracting native text
    with pdfplumber.open("example.pdf") as pdf:
        for page in pdf.pages:
            text = page.extract_text()
            if text:
                print(f"Native text (Page {page.page_number}): {text}")
            else:
                print(f"No native text on Page {page.page_number}, switching to OCR...")
    
    # Step 2: Convert to images and extract everything else
    images = convert_from_path("example.pdf", dpi=200)
    for i, image in enumerate(images):
        # Save image (includes graphs)
        image.save(f"page_{i + 1}.png", "PNG")
        # OCR for text in images
        text = pytesseract.image_to_string(image)
        print(f"OCR text (Page {i + 1}): {text}")
    #```
    """