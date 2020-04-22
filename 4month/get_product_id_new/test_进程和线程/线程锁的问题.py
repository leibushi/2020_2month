# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 18:48
# @Author  : Mqz
# @FileName: 线程锁的问题.py
import threading
g_count = 0

# def func(str_val):
#     global g_count
#     lock = threading.Lock()
#     lock.acquire()
#     try:
#         for i in range(1000000):
#             g_count += 1
#
#             print(':g_count=%s' % g_count)
#
#     finally:
#         lock.release()
#

def func(str_val):
    global g_count
    # lock = threading.Lock()
    # lock.acquire()

    for i in range(1000000):
        g_count += 1

        print(':g_count=%s' % g_count)




def test_func_lock():

    t1 = threading.Thread(target=func,args=['func1'])

    t2 = threading.Thread(target=func,args=['func2'])

    t1.start()

    t2.start()

    t1.join()

    t2.join()


test_func_lock()