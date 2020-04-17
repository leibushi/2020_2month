# -*- coding: utf-8 -*-
# @Time    : 2019/12/26 13:46
# @Author  : Mqz
# @FileName: query_brand_product_quantity_1230.py
"""查询品牌店铺获取产品的数量"""
import time

import schedule
from datetime import datetime
from common.mysqlutils import MysqlUtil

config1 = {
  #   阿里云服务器
  "host": "47.110.248.195",
  "user": "zhaoyl_et",
  "password": "Z#p*688%Et",
  "db": "et_crawl_taobao",
  "charset": "utf8",
  "port": 6610
}
# db_util1 = mysqlutils.MysqlUtil(config_dict=config1, pool_size=10)
db_util1 = MysqlUtil(config_dict=config1, pool_size=10)

config = {
    # 公司测试机器
    "host": "192.168.31.223",
    "user": "qph_b2c",
    "password": "zhaoyl(1181*%P)",
    "db": "taobao",
    # "db": "taobao_tmp",
    "charset": "utf8",
    "port": 6610
}
config2 = {
    # 公司测试机器
    "host": "192.168.31.223",
    "user": "qph_b2c",
    "password": "zhaoyl(1181*%P)",
    # "db": "taobao",
    "db": "taobao20190813test",
    "charset": "utf8",
    "port": 6610
}
# 本地数据库
# db_util = mysqlutils.MysqlUtil(config_dict=config, pool_size=10)
db_util = MysqlUtil(config_dict=config, pool_size=10)
db_util2 = MysqlUtil(config_dict=config2, pool_size=10)
Num = 5
now_time = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
print('当前时间【%s】，每【%s】分钟更新一次喲!.请等待..' % (now_time, Num))


def query_product_quantity():
    sql = '''SELECT COUNT(*) FROM taobao_item_20191227;'''
    result = db_util1.queryall(sql)
    creat_ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    print('当前时间【%s】，产品总共【%s】条' % (creat_ts, result[0]))
    # dir_name = 'taobao_item_20191227' + '1226'
    dir_name = 'taobao_item_20191227'
    # a+追加
    with open(dir_name, 'a+') as fp:
        # \n换行
        fp.write('\n当前时间【%s】，产品总共【%s】条' % (creat_ts, result[0]))

def query_product_quantity_test():
    file_name = 'taobao_brand_productid_20200106'
    sql = '''SELECT COUNT(*) FROM %s;''' % file_name
    result = db_util.queryall(sql)
    creat_ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    dir_name = file_name
    print('当前时间【%s】，表【%s】，产品总共【%s】条' % (creat_ts, dir_name, result[0]))
    # print('当前时间【%s】，产品总共【%s】条' % (creat_ts, result[0]))
    # a+追加
    with open(dir_name, 'a+') as fp:
        # \n换行
        fp.write('\n当前时间【%s】，表【%s】，产品总共【%s】条' % (creat_ts, dir_name, result[0]))
        # fp.write('\n当前时间【%s】，产品总共【%s】条' % (creat_ts, result[0]))

def query_product_quantity_taobao_list_web():
    sql = '''SELECT COUNT(*) FROM taobao_list_web_1230'''
    result = db_util2.queryall(sql)
    creat_ts = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    dir_name = 'taobao_list_web_1230'
    print('当前时间【%s】，表【%s】，产品总共【%s】条' % (creat_ts, dir_name, result[0]))
    # a+追加
    with open(dir_name, 'a+') as fp:
        # \n换行
        fp.write('\n当前时间【%s】，表【%s】，产品总共【%s】条' % (creat_ts, dir_name, result[0]))


# schedule.every(10).seconds.do(query_product_quantity)  # 10秒执行一次
# schedule.every(10).seconds.do(query_product_quantity_test)  # 10秒执行一次
# schedule.every(Num).minutes.do(query_product_quantity)  # 30分钟执行一次
schedule.every(Num).minutes.do(query_product_quantity_test)  # 30分钟执行一次
# schedule.every(1).minutes.do(query_product_quantity_taobao_list_web)  # 30分钟执行一次
# schedule.every(Num).minutes.do(query_product_quantity_taobao_list_web)  # 30分钟执行一次
while True:
    # try:
    schedule.run_pending()  # 运行所有可运行的任务
    time.sleep(1)