# -*- coding: utf-8 -*-
# @Time    : 2020/4/17 11:31
# @Author  : Mqz
# @FileName: 监控python，脚本的状态.py

import subprocess, time, sys
import os
TIME = 10
CMD = 'D:\Spider\spider\2020_2month\4month\get_product_id_new\Get_Product_id.py'
x = (CMD[-3:]).lower()
print(x)
class Auto_Run():
    def __init__(self, sleep_time, cmd):
        self.sleep_time = sleep_time
        self.cmd = cmd
        self.ext = (cmd[-3:]).lower()  # 判断文件的后缀名，全部换成小写
        self.p = None                  #self.p为subprocess.Popen()的返回值，初始化为None
        self.run()                     #启动时先执行一次程序

        try:
            while 1:
                time.sleep(sleep_time * 6) # #休息10分钟，判断程序状态
                self.poll = self.p.poll()   # #判断程序进程是否存在，None：表示程序正在运行 其他值：表示程序已退出
                if self.poll is None:
                    print("运行正常")
                else:
                    print('未检测到程序运行状态，准备启动程序')
                    self.run()
        except KeyboardInterrupt as e:
            print("未检测到CTRL+C, 准备启动程序")

#       self.p.kill()                   #检测到CTRL+C时，kill掉CMD中启动的exe或者jar程序


    def run(self):
        if self.ext == ".py":
            print("start OK!")
            self.p = subprocess.Popen(['python','%s' % self.cmd], stdin = sys.stdin,\
                    stdout = sys.stdout, stderr = sys.stderr, shell = False)

        else:
            pass


# app = Auto_Run(TIME, CMD)
# 不准确
# import win32com.client
#
#
# def check_exsit(process_name):
#     WMI = win32com.client.GetObject('winmgmts:')
#     processCodeCov = WMI.ExecQuery('select * from Win32_Process where Name like "%{}%"'.format(process_name))
#     if len(processCodeCov) > 0:
#         return True
#     else:
#         return False
#
#
# if __name__ == '__main__':
#     res = check_exsit('Get_Product_id.py')
#     print(res)

# import psutil
#
#
# # pl = psutil.pids()
# # for pid in pl:
# #     if psutil.Process(pid).name() == 'notepad++.exe':
# #         print(pid)
#
#
# def checkprocess(processname):
#     pl = psutil.pids()
#     for pid in pl:
#         if psutil.Process(pid).name() == processname:
#             return pid
#
#
# # print(isinstance(checkprocess("notepad++.exe"),int))
#
# if isinstance(checkprocess("notepad++.exe"), int):
#     print("进程存在")
# else:
#     print("进程不存在")

print(os.getpid())  # 获取当前进程id
print(os.getppid())  # 获取父进程id