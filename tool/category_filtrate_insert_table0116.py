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
import pymysql
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

config2 = {
    # 公司测试机器
    "host": "192.168.31.223",
    "user": "qph_b2c",
    "password": "zhaoyl(1181*%P)",
    # "db": "taobao",
    # "db": "taobao_tmp",
    "db": "taobao20190813test",
    "charset": "utf8",
    "port": 6610
}


# 公司测试机
db_util = mysqlutils.MysqlUtil(config_dict=config, pool_size=10)
# 插入阿里数据库中
db_util1 = mysqlutils.MysqlUtil(config_dict=config1, pool_size=10)
db_util2 = mysqlutils.MysqlUtil(config_dict=config2, pool_size=10)


def Get_Categroy_Data():
    '''
    从阿里Mysql数库
    获取categroy_id
    :return:
    '''
    # 剔除了特殊的品类单独进行处理
    # select_sql = '''SELECT id FROM taobao_item_20200110;'''
    # 全部品类
    select_sql = '''SELECT cat_id FROM taobao_category WHERE is_del IS NULL AND cat_id != '216505' AND cat_id != '127848002';'''

    # select_sql = '''SELECT cat_id FROM taobao_category_20200102 WHERE is_del IS NULL;'''
    # select_sql = '''SELECT cat_id FROM taobao_category_copy1 WHERE is_del IS NULL;'''
    try:
        # result = db_util2.queryall(select_sql)
        # 阿里云测试机
        result = db_util1.queryall(select_sql)
        # print(result)
        print(len(result))
        return result

    except pymysql.err.OperationalError as e:
        print(e)

    except Exception as e:
        print(e)


def Insert_Data(cat_ids):
    '''
    保存数据库
    :return:
    '''
    # print(cat_ids)
    print(len(cat_ids))
    count = 0
    for cat_id in cat_ids:
        count += 1
        print(cat_id)
        # 两个表都要改，以免出错
        select_sql = '''INSERT IGNORE INTO taobao_item_20200116_copy1 SELECT * FROM taobao_item_20200116 WHERE category_id=%s;'''
        # update = '''UPDATE taobao_list_web_2020_0110 SET state=14.7 WHERE id=%s'''
        # update = '''UPDATE filtrate_id_20200110 SET crawl_state =1 WHERE resource_id=%s'''
        try:
            # result = db_util2.execute(select_sql, cat_id)
            result = db_util1.execute(select_sql, cat_id)
            # result = db_util2.execute(update, cat_id)
            # yield result
            print('存入成功')

        except Exception as e:
            print('获取失败%s' % e)
    print(count)

# def insertl_to_all_data():
# #     sql = '''INSERT IGNORE INTO taobao_item_201906_1218 SELECT * FROM taobao_item_20191219_copy1'''
# #     try:
# #         db_util1.execute(sql)
# #         print('存入成功')
# #     except Exception as e:
# #         print('存入失败')

def teshu_insert_data():
    '''
    特殊品类处理保存数据库
    :return:
    '''
    # print(cat_ids)
    # print(len(cat_ids))
    # 伤口辅料
    cat_ids = ['127848002']
    # cat_id = '127848002'
    cat_ids = ['216505']
    cat_id = '216505'
    # cat_ids = ['127848002', '216505']
    # count = 0
    # 第一个
    keywords = ['面膜', '敏感肌', '护肤品', '械字号', '敷尔佳', '芙清', '可复美', '创福康']
    # 第二个
    keywords1 = ['固体香水', '止汗露']
    # for cat_id in cat_ids:
    #     # count +=1
    #     print(cat_id)
    # for keyword in keywords:
    #     print(keyword)

        # 两个表都要改，以免出错
    select_sql = '''INSERT IGNORE INTO taobao_item_20200116_copy1 SELECT * FROM taobao_item_20200116 WHERE
     category_id=%s AND goods_name LIKE '%%止汗露%%';'''
     # category=%s AND title LIKE '%%固体香水%%';'''
     # category_id=%s AND goods_name LIKE '%%固体香水%%';'''
     # category_id=%s AND goods_name LIKE '%%%%%s%%%%';'''
     # category_id=%s AND goods_name LIKE '%%%s%%';'''
    try:
        # result = db_util1.execute(select_sql, cat_id, keyword)
        result = db_util1.execute(select_sql, (cat_id))

        # yield result
        print('存入成功')

    except pymysql.err.OperationalError as e:
        print('连接超时', e)

    except Exception as e:
        print('获取失败%s' % e)
    # print(count)

def insert_datas():
    """
    插入正常数据不需要进行其他处理
    :return
    """
    view_sales = 30
    # select_sql = '''INSERT IGNORE INTO taobao_list_web_2020_0111 SELECT * FROM taobao_list_web_2020_0110_copy1 WHERE view_sales >= %s;'''
    select_sql = '''INSERT IGNORE INTO filtrate_id_20200110 SELECT id,state FROM taobao_list_web_2020_0111;'''
    # update = '''UPDATE taobao_list_web_2020_0110 SET state=14.7 WHERE id=%s'''
    try:
        # result = db_util2.execute(select_sql, view_sales)
        result = db_util2.execute(select_sql)
        # result = db_util2.execute(update, cat_id)
        # yield result
        print('存入成功')

    except Exception as e:
        print('获取失败%s' % e)



def main():
    # insert_datas()
    # 处理筛选品类
    # cat_data = Get_Categroy_Data()
    # Insert_Data(cat_data)
    # 存入到总数据数据库内
    # insertl_to_all_data()
    teshu_insert_data()



if __name__ == '__main__':
    start_time = datetime.datetime.now()
    main()
    end_time = datetime.datetime.now()
    print(end_time - start_time)