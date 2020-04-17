# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 11:20
# @Author  : Mqz
# @FileName: handle_mysql_data_tool.py
import asyncio
import datetime

import aiomysql
from common import mysqlutils

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


async def get_mysql_datas(loop):

    pool = await aiomysql.create_pool(host='47.110.248.195', port=6610,
                           user='zhaoyl_et', password='Z#p*688%Et',
                           db='et_crawl_taobao', loop=loop)
    # 用异步池获得 连接器
    async with pool.acquire() as conn:
        # 异步游标
        async with conn.cursor() as cur:
            sql = '''SELECT id FROM taobao_item_product_delete_state0115;'''
            await cur.execute(sql)
            # await cur.execute('SELECT 42;')
            # (('COUNT(*)', 8, None, 21, 21, 0, False),)
            # 打印游标说明\描述
            print(cur.description)
            # < Future finished result = (150885,) >
            # 出现这种情况是因为没有在cur.fetchone() 前面加await
            # value = await cur.fetchone()
            value = await cur.fetchall()
            for i in value:
            # print(value)
            # print(value)
                print(i[0])

    pool.close()
    await pool.wait_closed()
if __name__ == '__main__':
    start_time = datetime.datetime.now()
    loop = asyncio.get_event_loop()
    loop.run_until_complete(get_mysql_datas(loop))
    end_time = datetime.datetime.now()
    print(end_time - start_time)

"""
def get_mysql_datas(limit):
    sql = '''SELECT resource_id FROM taobao_item_product_delete_state0115 WHERE crawl_state = 99
     limit 0, {};'''.format(limit)
    result = db_util1.queryall(sql)
    print(len(result))
    print(result)
    return result


def update_mysql_id_state(datas):
    for ids in datas:


        update_sql = '''UPDATE taobao_item_201906 SET taobao_state = 99 WHERE id = %s;'''
        try:

            db_util1.execute(update_sql, ids)
            print('更新成功')
            update_mysql_datas(ids)

        except Exception as e:
            print('更新失败', e)


def update_mysql_datas(resource_id):
    update_sql = '''UPDATE taobao_item_product_delete_state0115 SET state = 99 WHERE resource_id = %s;'''
    try:

        db_util1.execute(update_sql, resource_id)
        print('id更新成功')

    except Exception as e:
        print('id更新失败', e)



datas = get_mysql_datas(50000)
update_mysql_id_state(datas)
"""
# 24.6
