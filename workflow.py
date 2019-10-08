# -*- coding: utf-8 -*-
"""
Created on Thu Feb 28 05:21:50 2019
@author: fuzy
"""
import numpy as np
import csv
import os
import json
#from tkinter import *
from selenium import webdriver
from selenium.webdriver.common.keys import Keys

if __name__ == "__main__":
    workpath = "D:\\LAMDA\\组内服务\\文献整理\\2月27日\\2-付朝阳\\任务6（各国院士）\\fuzy.csv"
    savepath ='D:\\LAMDA\\组内服务\\文献整理\\2月27日\\2-付朝阳\\任务6（各国院士）\\res.csv'
    pdfpath = "D:\\LAMDA\\组内服务\\文献整理\\2月27日\\2-付朝阳\\任务6（各国院士）\\pdf\\"
    finalpath = "D:\\LAMDA\\组内服务\\文献整理\\2月27日\\2-付朝阳\\任务6（各国院士）\\final\\"
    name = "fuzy"
    res = []
    driver = webdriver.Chrome()
    start_urls = "https://scholar.google.com/"
    driver.get(start_urls)

    header = ""
    f = open(savepath, "wt")
    if isinstance(header, dict):
        header = '# {} \n'.format(json.dumps(header))
    f.write(header)
    logger = csv.DictWriter(f, fieldnames=('num', 'authorname', 'department','yuanji','year','title',
        'information','beiyin_title','beiyin_information','yinwen_path','proveurl','fuzeren'))
    logger.writeheader()
    f.flush()
    
    # window = Tk()
    # window.title('my window')
    # window.geometry('1000x600')
    # Label(window, text="userName").grid(row=0)
    # Label(window, text="password").grid(row=1)
    # Entry(window).grid(row=0, column=1)
    # Entry(window).grid(row=1, column=1)

    # window.mainloop()
    #b1 = tk.Button(window,text="insert point",width=15,height=2,command=insert_point)
    #b1.pack()
    
    with open(workpath, 'r',encoding='ISO-8859-1') as f:
        csv_reader = csv.reader(f)
        for step,row in enumerate(csv_reader,1):
            if step < 34:
                continue
            #print(step)
            title = row[1]
            authorname = row[2]
            year = row[5]
            proveurl = row[6]

            element = driver.find_element_by_name("q")
            element.clear()
            element.send_keys(title)
            element.send_keys(Keys.RETURN)

            ok = input("isDownload: ")
            if ok.lower() in ["y", "yes"]:
                ismodifyname = input("authorname {}  :".format(authorname))
                if ismodifyname.lower() in ['n','no']:
                    authorname = input("please input authorname: ")
                department = input("please input department: ")
                # yuanji = input("please input yuanji: ")
                yuanji = "其他院士/美国艺术与科学院 AAAS"
                #ismodifyyear = input("year: {}  ".format(year))
                #if ismodifyyear.lower() in ['n','no']:
                paperyear = input("please input paperyear: ")
                yinwen_information = input("information: ")
                yinwen_path = "任务6(各国院士)\其他国家院士\\"
                pdf_new_name = "{} - {}_{}.pdf".format(title,paperyear,name)
                beiyin_title = input("beiyin title: ")
                beiyin_information = input("beiyin information: ")

                rowinfo = {'num':step, 'authorname':authorname, 'department':department,'yuanji':yuanji,
                    'year':year,'title':title,'information':yinwen_information,'beiyin_title':beiyin_title,
                    'beiyin_information':beiyin_information,'yinwen_path':yinwen_path + pdf_new_name,
                    'proveurl':proveurl,'fuzeren':name}
                print(rowinfo)
                logger.writerow(rowinfo)
                f.flush()
                done = input("is done:  ")
                if done.lower() in ["y", "yes"]:
                    filenames = os.listdir(pdfpath)
                    for i in range(len(filenames)):
                        filename = pdfpath + '\"' + filenames[i] + '\"'
                        cmdstr = "move {} {}".format(filename,finalpath + '\"' + pdf_new_name + '\"')
                        print(cmdstr)
                        os.system(cmdstr)

