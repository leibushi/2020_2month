# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 13:46
# @Author  : Mqz
# @FileName: query_brand_product_quantity_1230.py
"""
查询品牌店铺获取产品的数量可以用最原始的方法进行改写看正确情况怎么样
待完善：
文件名改为 表的名字
查询日志要新建一个文件
查询日志要定期清理
"""
import time
import pymysql
import schedule
from datetime import datetime
from common.configs import SAVE_BRAND_SHOP_TABLE_NAME,\
    db_util_1, SAVE_BRAND_SHOP_TABLE_NAME_PC, SAVE_TAOBAO_LIST_WEB_DATA_TABLE


Num = 5
now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('当前时间【%s】，每【%s】分钟更新一次喲!.请等待..' % (now_time, Num))


def query_product_quantity():
    sql = '''SELECT COUNT(*) FROM {};'''.format(SAVE_BRAND_SHOP_TABLE_NAME)
    result = db_util_1.queryall(sql)
    creat_ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('当前时间【%s】，产品总共【%s】条' % (creat_ts, result[0]))
    # dir_name = 'taobao_item_20191227' + '1226'
    dir_name = 'taobao_item_20191227'
    # a+追加
    with open(dir_name, 'a+') as fp:
        # \n换行
        fp.write('\n当前时间【%s】，产品总共【%s】条' % (creat_ts, result[0]))


def query_product_quantity_test():
    db = pymysql.connect(host="", port=6610, user="",
                         password="", db="")
    cursor = db.cursor()
    sql = '''SELECT COUNT(*) FROM {};'''.format(SAVE_BRAND_SHOP_TABLE_NAME)
    cursor.execute(sql)
    # print(type(cursor.fetchall()))
    result = cursor.fetchall()[0][0]
    creat_ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    creat_time = datetime.now().strftime('%Y-%m-%d')
    # dir_name = '..\tatale_log\brand_product' + creat_time
    dir_name = r'D:\Spider\spider\2020_2month\tool\tatale_log/brand_product' + creat_time
    print('当前时间【%s】，表【%s】，产品总共【%s】条' % (creat_ts, dir_name, result))

    # # a+追加
    with open(dir_name, 'a+') as fp:
        # \n换行
        fp.write('\n当前时间【%s】，表【%s】，产品总共【%s】条' % (creat_ts, dir_name, result))
        # fp.write('\n当前时间【%s】，产品总共【%s】条' % (creat_ts, result))
        db.commit()
        db.close()


def query_product_quantity_test_app():
    db = pymysql.connect(host="", port=6610, user="",
                         password="", db="")
    cursor = db.cursor()
    sql = '''SELECT COUNT(*) FROM {};'''.format(SAVE_BRAND_SHOP_TABLE_NAME)
    cursor.execute(sql)
    # print(type(cursor.fetchall()))
    result = cursor.fetchall()[0][0]
    creat_ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    creat_time = datetime.now().strftime('%Y-%m-%d')
    # dir_name = '..\tatale_log\brand_product' + creat_time
    dir_name = r'D:\Spider\spider\2020_2month\tool\tatale_log\brand_product' + creat_time
    print('当前时间【%s】，表【%s】，产品总共【%s】条' % (creat_ts, SAVE_BRAND_SHOP_TABLE_NAME, result))

    # # a+追加
    with open(dir_name, 'a+') as fp:
        # \n换行
        fp.write('\n当前时间【%s】，表【%s】，产品总共【%s】条' % (creat_ts, dir_name, result))
        # fp.write('\n当前时间【%s】，产品总共【%s】条' % (creat_ts, result))
        db.commit()
        db.close()


def query_product_quantity_test_pc():
    db = pymysql.connect(host="", port=, user="",
                         password="", db="")
    cursor = db.cursor()
    sql = '''SELECT COUNT(*) FROM {};'''.format(SAVE_BRAND_SHOP_TABLE_NAME_PC)
    cursor.execute(sql)
    # print(type(cursor.fetchall()))
    result = cursor.fetchall()[0][0]
    creat_ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    creat_time = datetime.now().strftime('%Y-%m-%d')
    # dir_name = '..\tatale_log\brand_product' + creat_time
    dir_name = r'D:\Spider\spider\2020_2month\tool\tatale_log\brand_product' + creat_time
    print('当前时间【%s】，表【%s】，产品总共【%s】条' % (creat_ts, SAVE_BRAND_SHOP_TABLE_NAME_PC, result))

    # # a+追加
    with open(dir_name, 'a+') as fp:
        # \n换行
        fp.write('\n当前时间【%s】，表【%s】，产品总共【%s】条' % (creat_ts, dir_name, result))
        # fp.write('\n当前时间【%s】，产品总共【%s】条' % (creat_ts, result))
        db.commit()
        db.close()



def query_product_quantity_taobao_list_web():
    db = pymysql.connect(host="", port=6610, user="",
                         password="z", db="")
    cursor = db.cursor()
    sql = '''SELECT COUNT(*) FROM {};'''.format(SAVE_TAOBAO_LIST_WEB_DATA_TABLE)
    cursor.execute(sql)
    # print(type(cursor.fetchall()))
    result = cursor.fetchall()[0][0]
    creat_ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    creat_time = datetime.now().strftime('%Y-%m-%d')
    dir_name = 'brand_product' + creat_time
    print('当前时间【%s】，表【%s】，产品总共【%s】条' % (creat_ts, SAVE_TAOBAO_LIST_WEB_DATA_TABLE, result))

    # # a+追加
    with open(dir_name, 'a+') as fp:
        # \n换行
        fp.write('\n当前时间【%s】，表【%s】，产品总共【%s】条' % (creat_ts, dir_name, result))
        # fp.write('\n当前时间【%s】，产品总共【%s】条' % (creat_ts, result))
        db.commit()
        db.close()


# schedule.every(10).seconds.do(query_product_quantity)  # 10秒执行一次
# schedule.every(1).seconds.do(query_product_quantity_test)  # 10秒执行一次
# schedule.every(Num).minutes.do(query_product_quantity)  # 30分钟执行一次
# schedule.every(Num).minutes.do(query_product_quantity_test)  # 30分钟执行一次
schedule.every(Num).minutes.do(query_product_quantity_test_app)  # 5分钟执行一次
schedule.every(Num).minutes.do(query_product_quantity_test_pc)  # 5分钟执行一次
# schedule.every(1).minutes.do(query_product_quantity_taobao_list_web)  # 30分钟执行一次
schedule.every(Num).minutes.do(query_product_quantity_taobao_list_web)  # 30分钟执行一次
while True:
    # try:
    schedule.run_pending()  # 运行所有可运行的任务
    time.sleep(1)
