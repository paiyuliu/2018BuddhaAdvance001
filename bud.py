# -*- coding: utf-8 -*-
"""
Created on Mon Mar  9 10:31:06 2020
@author: paiyuliu
"""
import re
#import sys
#import codecs
from selenium import webdriver

print("program start")




#voice="75a"

voiceFile = [
 "51a","51b"
]

for fileName in voiceFile:
    print(fileName)
    txtFileName = fileName+".json"
    driver = webdriver.Chrome()
    driver.implicitly_wait(5) # seconds
    # 避免看程式的人知道從哪裡爬的
    # 所以url清空
    # 這是為了不讓有心人士攻擊該網站
    # 不過爬蟲算不算攻擊算不算盜也不知道
    url= ""+fileName
    driver.get(url)
    body = driver.find_element_by_id("script-body")
    p = body.find_elements_by_xpath(".//p")
    
    str = ""
    count = 0;
    print("{",file = open(txtFileName, 'w',encoding='utf-8'))
    for abc in p:
        str = ""
        r1 = re.findall("\d{2}:\d{2}",abc.text)
        b1 = False
        timeStr = ""
        for ccc in r1:
            timeStr = ccc
            ddd = re.split(':', ccc)
            if count == 0 :
                print('\"', end='',file = open(txtFileName, 'a',encoding='utf-8'))
                print(int(ddd[0])*60 + int(ddd[1]),end='',file = open(txtFileName, 'a',encoding='utf-8'))
                print('\":', end='',file = open(txtFileName, 'a',encoding='utf-8'))
                count = 1
            else:
                print('\",\"', end='',file = open(txtFileName, 'a',encoding='utf-8'))
                print(int(ddd[0])*60 + int(ddd[1]),end='',file = open(txtFileName, 'a',encoding='utf-8'))
                print('\":',end='',file = open(txtFileName, 'a',encoding='utf-8'))
            b1=True
            break
            
        if b1 == True:
            str  = str + "\"["+timeStr+"]"
            #print("["+timeStr+":00"+"]")
        else:
            if len(abc.text) > 0 :
                str = str + abc.text
                #print(abc.text)
        print(str.replace('\n',''),end='',file = open(txtFileName, 'a',encoding='utf-8'))
    
    # element2 = driver.find_element_by_id("script-body")
    #for items2 in element:
    #    print (items2.text)
    print("\"}",file = open(txtFileName, 'a',encoding='utf-8'))
    driver.close()

print("program pause")
driver.quit()
print("program end")
