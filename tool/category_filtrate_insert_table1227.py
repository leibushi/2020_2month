# -*- coding: utf-8 -*-
# @Time    : 2019/11/14 17:56
# @Author  : Mqz
# @FileName: category_filtrate.py

# 对爬取的产品的category进行筛选
# 对总表进行备份
# 存入总表
import sys, os
from os.path import dirname, abspath

# path = dirname(dirname(dirname(abspath(__file__))))
# path = dirname(abspath(__file__))
# sys.path.append('/mnt/d/Spider/spider/12month')
# sys.path.append('/home/muyi2019/.local/lib/python3.7/site-packages')

# curPath = os.path.abspath(os.path.dirname(__file__))
# rootPath = os.path.split(curPath)[0]
# sys.path.append(os.path.split(rootPath)[0])

# sys.path.append("/mnt/d/Spider/spider")
# from 12month import common1
from common.mysqlutils import MysqlUtil
import datetime
from common import mysqlutils


config = {
    # 公司测试机器
    "host": "192.168.31.223",
    "user": "qph_b2c",
    "password": "zhaoyl(1181*%P)",
    # "db": "taobao",
    "db": "taobao_tmp",
    "charset": "utf8",
    "port": 6610
}

config1 = {
  #   阿里云服务器
  "host": "47.110.248.195",
  "user": "zhaoyl_et",
  "password": "Z#p*688%Et",
  "db": "et_crawl_taobao",
  "charset": "utf8",
  "port": 6610
}
# 公司测试机
db_util = mysqlutils.MysqlUtil(config_dict=config, pool_size=10)
# 插入阿里数据库中
db_util1 = mysqlutils.MysqlUtil(config_dict=config1, pool_size=10)


def Get_Categroy_Data():
    '''
    获取categroy_id
    :return:
    '''
    # select_sql = '''SELECT cat_id FROM taobao_category WHERE is_del IS NULL;'''
    select_sql = '''SELECT cat_id FROM taobao_category_copy1 WHERE is_del IS NULL;'''
    try:
        result = db_util1.queryall(select_sql)
        # print(result)
        return result
    except Exception as e:
        print(e)


def Insert_Data(cat_ids):
    '''
    保存数据库
    :return:
    '''
    print(cat_ids)
    print(len(cat_ids))
    for cat_id in cat_ids:
        print(cat_id)
        # 两个表都要改，以免出错
        select_sql = '''INSERT IGNORE INTO taobao_item_20191227_copy2 SELECT * FROM taobao_item_20191227 WHERE category_id=%s;'''
        try:
            result = db_util1.execute(select_sql, cat_id)
            # yield result
            print('存入成功')

        except Exception as e:
            print('获取失败%s' % e)


def insertl_to_all_data():
    sql = '''INSERT IGNORE INTO taobao_item_201906_1218 SELECT * FROM taobao_item_20191219_copy1'''
    try:
        db_util1.execute(sql)
        print('存入成功')
    except Exception as e:
        print('存入失败')

def main():
    cat_data = Get_Categroy_Data()
    Insert_Data(cat_data)
    # 存入到总数据数据库内
    # insertl_to_all_data()



if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now()
    print(end_time - start_time)