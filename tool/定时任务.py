# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 14:22
# @Author  : Mqz
# @FileName: 定时任务.py
# 参考文章 https://www.jianshu.com/p/d6f406074401
import sched, time

# 生成调度器
s = sched.scheduler(time.time, time.sleep)

def print_time(a='default'):
    print("From print_time", time.time(), a)


def print_some_times():
    print('时间%s' % time.time())
    # 加入调度事件
    # s.enter(10, 1, print_time) #default
    # 四个参数分别是:
    # 间隔时间(具体值决定与delayfunc, 这里为秒);
    # 优先级(两个事件在同一时间到达的情况);
    # 触发的函数;
    # 函数参数
    # 在同一时间内
    s.enter(5, 2, print_time, argument=('positional',))#positional
    s.enter(10, 1, print_time, kwargs={'a': 'keyword'})#keyword
    # 运行调度
    s.run()
    print(time.time())

print_some_times()

import time
import sched
import datetime

schedule = sched.scheduler(time.time, time.sleep)


def event_fun1():
    print("func1 Time:", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def event_fun2():
    print("func2 Time:", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def event_fun3():
    print("func3 Time:", datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S'))


def func1(sec):
    schedule.enter(sec, 0, func1, (sec,))
    event_fun1()


def func2(sec):
    schedule.enter(sec, 0, func2, (sec,))
    event_fun2()


def func3(sec):
    schedule.enter(sec, 0, func3, (sec,))
    event_fun3()


print("start")
while True:
    nt = datetime.datetime.now()
    if nt.second == 0:
        break
    time.sleep(1)

schedule.enter(10, 0, func1, (10,))
schedule.enter(30, 0, func2, (30,))
schedule.enter(60, 0, func3, (60,))
schedule.run()
print("end")