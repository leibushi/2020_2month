# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 18:20
# @Author  : Mqz
# @FileName: 四种队列.py
import collections
q = collections.deque([1, 2, 3, 4])
print(5 in q)  # False
print(1 in q)  # True

print('*' * 20)
# 顺时针
q = collections.deque([1, 2, 3, 4])
q.rotate(1)
print(q)  # [4, 1, 2, 3]
# 使旋转的位数
q.rotate(2)
print(q)  # [3, 4, 1, 2]

# 逆时针
q = collections.deque([1, 2, 3, 4])
q.rotate(-1)
print(q)  # [2, 3, 4, 1]
q.rotate(-1)
print(q)  # [3, 4, 1, 2]

print("*" * 20)
import threading
import queue
import random
import time


class Producter(threading.Thread):
    """生产者线程"""
    def __init__(self, t_name, queue):
        self.queue = queue
        threading.Thread.__init__(self, name=t_name)

    def run(self):
        for i in range(10):
            randomnum = random.randint(1, 99)
            self.queue.put(randomnum)
            print('put num in Queue %s' %  randomnum)
            time.sleep(1)

        print('put queue done')


class ConsumeEven(threading.Thread):
    """奇数消费线程"""
    def __init__(self, t_name, queue):
        self.queue = queue
        threading.Thread.__init__(self, name=t_name)

    def run(self):
        while True:
            # 使用了判空处理
            if queue.Empty():
                break
            try:
                queue_val = self.queue.get(1, 3)

            except Exception as e:
                print(e)
                break

            if queue_val % 2 == 0:
                print('Get Even Num %s ' % queue_val)
            else:
                self.queue.put(queue_val)


q = queue.Queue()
pt = Producter('producter', q)
ce = ConsumeEven('consumeeven', q)
ce.start()
pt.start()
pt.join()
ce.join()
