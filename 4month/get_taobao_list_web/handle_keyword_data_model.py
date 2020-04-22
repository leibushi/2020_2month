# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 14:16
# @Author  : Mqz
# @FileName: handle_keyword_data.py
# 对收货人数进进行处理
from common.mysqlutils import MysqlUtil
from common.configs import db_util_3, TAOBAO_DE_WEIGHT_TOTAL_DATA

# PARAMETER = 'Null'
# PARAMETER = '人收货'
# PARAMETER2 = ''
# 2092个
# PARAMETER = '+'
# PARAMETER2 = ''

# 616
# PARAMETER = '.0万'
# PARAMETER2 = '0000'

# 385
# PARAMETER = '.5万'
# PARAMETER2 = '5000'

# 19
# PARAMETER = '0万'
# PARAMETER2 = '00000'
#
# field_table1 = ['人收货', '+', '.0万', '.5万', '0万']
# field_table2 = ['', '', '0000', '5000', '00000']

def query_data(PARAMETER):
    """
    查询包含的人数，收货，万，0.5w等
    :return
    """
    sql = 'SELECT COUNT(*) FROM {0} WHERE view_sales LIKE "%{1}%"'.format(TAOBAO_DE_WEIGHT_TOTAL_DATA, PARAMETER)
    # sql = 'SELECT COUNT(*) FROM {0} WHERE view_sales IS NULL'.format(KEYWORD)
    result = db_util_3.queryall(sql)[0]
    print(result)


def update_consignee(PARAMETER, PARAMETER2):
    """
    更新收货人数
    :return
    """
    # upd_sql = 'UPDATE {0} SET crawl_page={1}'.format(KEYWORD, crawl_page)
    upd_sql = "UPDATE {0} SET view_sales=replace(view_sales,'{1}','{2}')".format(TAOBAO_DE_WEIGHT_TOTAL_DATA,
                                                                                 PARAMETER, PARAMETER2)
    try:
        db_util_3.execute(upd_sql)
        print('【{0}】更新成功'.format(TAOBAO_DE_WEIGHT_TOTAL_DATA))

    except Exception as e:
        print('【{0}】更新失败'.format(TAOBAO_DE_WEIGHT_TOTAL_DATA))


def more_table_query():
     # 和原数据进行对比 内连接进行查询 15w+数据挺快的

    sql = '''SELECT taobao_list_web_2020_0406.nid,taobao_list_web_2020_0406.view_sales,
    taobao_list_web_2020_0406_copy1.nid,taobao_list_web_2020_0406_copy1.view_sales FROM 
    taobao_list_web_2020_0406 INNER JOIN taobao_list_web_2020_0406_copy1 ON 
    taobao_list_web_2020_0406.nid = taobao_list_web_2020_0406_copy1.nid;'''
    result = db_util_3.queryall(sql)
    print(result)


def change_table_field_type():
    """
    更改表字段类型
    :return
    """

    # sql = 'ALTER TABLE {0} USER {1} CHANGE {2} {3} varchar(225)'.format(TAOBAO_DE_WEIGHT_TOTAL_DATA, 'resource_id',
    sql = 'ALTER TABLE {0} MODIFY {1} bigint(16)'.format(TAOBAO_DE_WEIGHT_TOTAL_DATA, 'view_sales')
    try:
        db_util_3.execute(sql)
        print('成功')
    except Exception as e:
        print('操作失败', e)
# alter table user modify court_id char(16);

def main():
    # PARAMETER = '0万'
    # PARAMETER2 = '00000'

    field_table1 = ['人收货', '+', '.0万', '.5万', '0万']
    field_table2 = ['', '', '0000', '5000', '00000']
    for PARAMETER, PARAMETER2 in zip(field_table1, field_table2):
        query_data(PARAMETER)
        update_consignee(PARAMETER, PARAMETER2)
        query_data(PARAMETER)
        # more_table_query()
        # change_table_field_type()
        pass


if __name__ == '__main__':
    main()

