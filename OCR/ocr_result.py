# -*- coding: utf-8 -*-
"""
Created on Tue Dec 21 00:29:26 2021

@author: YJ
"""

import matplotlib.pyplot as plt
import cv2
import pytesseract
import glob

result = []

def read_receipt(filename) : 
   files = glob.glob(filename)

   for i in range(len(files)) :
      re_title = files[i].strip('.jpg')
      #draw receipts image 
      receipt_img = cv2.imread(files[i], cv2.IMREAD_COLOR)
      plt.imshow(receipt_img)
      plt.title(re_title)
      plt.show()
      
      #tesseract text dection and store the result
      receipt_txt = pytesseract.image_to_string(receipt_img, lang=('kor+eng'))
      result.append(receipt_txt)
      f = open(re_title+'.txt','w',encoding='utf-8')
      f.write(receipt_txt+'\n')
      f.close()
   return receipt_txt
       
if __name__ == '__main__':
   
   filename = 'receipt/*.jpg'
   txts = read_receipt(filename)
   


