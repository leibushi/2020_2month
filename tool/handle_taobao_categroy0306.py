
# -*- coding: utf-8 -*-
# @Time    : 2019/12/13 16:47
# @Author  : Mqz
# @FileName: insert_taobao_param.py
import datetime
from common import mysqlutils

config1 = {

  "host": "",
  "user": "",
  "password": "",
  "db": "",
  "charset": "utf8",
  "port": 6610
}
db_util1 = mysqlutils.MysqlUtil(config_dict=config1, pool_size=10)



def insert_mysql(cat_info):
    '''
    存入mysql的淘宝品类库
    :param
    '''
    cat_id = cat_info['cat_id']
    cat_name = cat_info['cat_name']
    keyword = cat_info['keyword']
    sql = '''SELECT COUNT(*) FROM taobao_item_201906 WHERE category_id = %s'''
    # sql = '''INSERT IGNO、‘RE INTO taobao_category_20200202(cat_id,cat_name,keyword_filtrate) VALUES (%s,%s,%s)'''
    try:
        # now_time = datetime.datetime.now().strftime('%Y-%m-%d %H:%M:%S')
        # db_util1.insertone(sql, (cat_id, cat_name, keyword))
        result = db_util1.queryall(sql, cat_id)
        # print('存入成功')
        print('品类【%s】,id【%s】, 数量【%s】个' % (cat_name, cat_id, result[0]))

    except Exception as e:
        print('存入失败', e)


def get_category():

    """
    获取catgory 共有308个品类要进行特殊处理 先处理多的数据
    :return:
    """
    # select_sql = '''SELECT  cat_id FROM taobao_category WHERE is_del IS NULL'''
    select_sql = '''SELECT cat_id FROM taobao_category WHERE is_del IS NULL AND cat_id != '216505' 
    AND cat_id != '127848002';'''
    # result = db_util.queryall(select_sql)
    result = db_util1.queryall(select_sql)
    # print('原数据336个筛选后:%s个' % result)
    print('原数据352个筛选后:%s个' % result)
    count = 0
    for cat_id in result:
        print(cat_id)
        count += 1
    print(count)
    return result


def handle_tatle(category_id):
    """处理总表要去除的品类包含的商品进行更新为美业下架状态
    """
    update_sql = '''UPDATE taobao_item_201906 SET state =77 WHERE category_id = {}'''.format(category_id)
    try:
        db_util1.execute(update_sql)
        print("更新成功")
    except Exception as e:
        print("更新失败", e)


if __name__ == '__main__':
    '''
    '''

    cat_info = []
    count = 0
    get_category()
    # for i in cat_info:
    #     count += 1
    #     # print(i)
    #     insert_mysql(i)
    # print('共存入【%s】' % count)



