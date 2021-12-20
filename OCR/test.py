# -*- coding: utf-8 -*-
"""
Created on Sat Dec 11 01:39:16 2021

@author: YJ
"""

import matplotlib.pyplot as plt
import cv2
import pytesseract
import numpy as np

#%% OCR TEST 
path = "sample2.png"

test_img = cv2.imread(path, cv2.IMREAD_COLOR)
plt.figure(figsize=[5,5])
plt.imshow(test_img)

result = pytesseract.image_to_string(test_img, lang = 'kor')

#pillow
from PIL import Image

ptl_img = Image.open(path)
ptl_img

result2 = pytesseract.image_to_string(ptl_img, lang ='kor')
ptl_img_array = np.array(ptl_img)

plt.imshow(ptl_img_array)
plt.axis("off")
plt.show()


#%%image preprocessing 

#openCV = BGR color , matplotlib = RGB color
img_path = "C:/Users/LG/OCR/receipt1.jpg"
receipt = cv2.imread(img_path, cv2.IMREAD_COLOR)
plt.figure(figsize=[5,5])
plt.imshow(receipt)

receipt_gray = cv2.imread(img_path,cv2.IMREAD_GRAYSCALE)
plt.figure(figsize=[5,5])
plt.imshow(receipt_gray)

def img_to_binary(img) :
   result = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV)[1]
   return result

receipt_bin = img_to_binary(receipt_gray)
plt.figure(figsize=[5,5])
plt.imshow(receipt_bin)

img_noise = cv2.medianBlur(receipt,ksize = 7)
plt.subplot(1,2,1)
plt.imshow(receipt)
plt.xlabel("original")
plt.subplot(1,2,2)
plt.imshow(img_noise)
plt.xlabel("remove noise")

img_path2 = "C:/Users/LG/OCR/receipt2.jpg"
receipt = cv2.imread(img_path2, cv2.IMREAD_COLOR)
plt.figure(figsize=[5,5])
plt.imshow(receipt)

receipt_gray = cv2.imread(img_path2,cv2.IMREAD_GRAYSCALE)
plt.figure(figsize=[5,5])
plt.imshow(receipt_gray)

def img_to_binary(img) :
   result = cv2.threshold(img,0,255,cv2.THRESH_BINARY_INV)[1]
   return result

receipt_bin = img_to_binary(receipt_gray)
plt.figure(figsize=[5,5])
plt.imshow(receipt_bin)

img_noise = cv2.medianBlur(receipt,ksize = 7)
plt.subplot(1,2,1)
plt.imshow(receipt)
plt.xlabel("original")
plt.subplot(1,2,2)
plt.imshow(img_noise)
plt.xlabel("remove noise")

#closing : dilation -> erosion
kernel = np.ones((5,5), np.uint8)

closing = cv2.morphologyEx(receipt, cv2.MORPH_CLOSE,kernel)
opening = cv2.morphologyEx(receipt, cv2.MORPH_OPEN, kernel)
erosion = cv2.erode(receipt,kernel,iterations = 1)
dilation = cv2.dilate(receipt,kernel,iterations = 1)

images =[dilation,erosion,opening,closing]
titles=["dilation","erosion","opening","closing"]

for x in range(1,5):
   plt.subplot(2,2,x)
   plt.imshow(images[x-1])
   plt.title(titles[x-1])

plt.show()




#%%OCR 
receipt_ocr = pytesseract.image_to_string(receipt, lang ='kor')
receipt_ocr2 = pytesseract.image_to_string(receipt, lang ='kor+eng')
