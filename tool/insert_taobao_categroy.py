# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 16:47
# @Author  : Mqz
# @FileName: insert_taobao_param.py
import datetime
# 存入阿里云数据库mysql的
from common import mysqlutils,get_cookie_1

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
db_util1 = mysqlutils.MysqlUtil(config_dict=config1, pool_size=10)


config = {
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
db_util = mysqlutils.MysqlUtil(config_dict=config, pool_size=10)


def insert_mysql(cat_info):
    '''
    存入mysql的淘宝品类库
    :param
    '''
    cat_id = cat_info['cat_id']
    cat_name = cat_info['cat_name']
    keyword = cat_info['keyword']
    sql = '''INSERT IGNORE INTO taobao_category_20200202(cat_id,cat_name,keyword_filtrate) VALUES (%s,%s,%s)'''
    try:
        # now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        db_util1.insertone(sql, (cat_id, cat_name, keyword))
        print('存入成功')

    except Exception as e:
        print('存入失败', e)


def get_wua():
    # sql_select = '''SELECT x_mini_wua, x_mini_wua_name FROM taobao_wua WHERE x_mini_wua_name="001"'''
    sql_select = '''SELECT x_mini_wua FROM taobao_wua WHERE x_mini_wua_name="001"'''
    result = db_util.queryone(sql_select)
    print(result)


if __name__ == '__main__':
    '''
    化妆/美容工具 50010817
    化妆棉 201169003
    化妆刷 121480026
    假睫毛 121386023
    假睫毛工具 122472001
    双眼皮胶水 121480003
    双眼皮贴 121420006
    121456021 假睫毛辅助工具
    '''

    cat_info = [
        {'cat_id': '50010817', 'cat_name': '化妆/美容工具', 'keyword': ''},
        {'cat_id': '201169003', 'cat_name': '化妆棉', 'keyword': ''},
        {'cat_id': '121480026', 'cat_name': '化妆刷', 'keyword': ''},
        {'cat_id': '121386023', 'cat_name': '假睫毛', 'keyword': ''},
        {'cat_id': '122472001', 'cat_name': '假睫毛工具', 'keyword': ''},
        {'cat_id': '121480003', 'cat_name': '双眼皮胶水', 'keyword': ''},
        {'cat_id': '121420006', 'cat_name': '双眼皮贴', 'keyword': ''},
    ]
    count = 0
    for i in cat_info:
        count += 1
        # print(i)
        insert_mysql(i)
    print('共存入【%s】' % count)



