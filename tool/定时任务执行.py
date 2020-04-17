
# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 14:34
# @Author  : Mqz
# @FileName: 定时任务执行.py
# 参考文章 https://www.jianshu.com/p/d6f406074401
import time
import schedule

def job():
    print('test')

schedule.every(10).seconds.do(job)  # 每10秒执行一次
schedule.every(10).minutes.do(job)  # 每10分钟执行一次
schedule.every().hour.do(job)  # 每小时执行一次

schedule.every().day.at("10:30").do(job) # 每天十点半执行
schedule.every(5).to(10).minutes.do(job) # 不理解
schedule.every().monday.do(job) # 每周一执行
schedule.every().wednesday.at("13:15").do(job) # 每周三13点15执行
schedule.every().minute.at(":17").do(job)  # 不理解
import schedule
import time

def job():
    print("I'm working...")

schedule.every(10).minutes.do(job)
schedule.every().hour.do(job)
schedule.every().day.at("10:30").do(job)
schedule.every(5).to(10).minutes.do(job)
schedule.every().monday.do(job)
schedule.every().wednesday.at("13:15").do(job)
schedule.every().minute.at(":17").do(job)

while True:
    schedule.run_pending()
    time.sleep(1)
# while True:
#     schedule.run_pending() # 运行所有可运行的任务
#     time.sleep(1)