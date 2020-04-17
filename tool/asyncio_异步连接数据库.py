# -*- coding: utf-8 -*-
# @Time    : 2020/1/16 14:01
# @Author  : Mqz
# @FileName: asyncio_异步连接数据库.py

# 基本异步连接池connection
import asyncio
from aiomysql import create_pool


# 循环  异步io(并发)获取事件.循环\回路
loop = asyncio.get_event_loop()
async def go():
    # 用异步 创建池
    async with create_pool(host='192.168.31.223', port=6610,
    # pool await aiomysql.create_pool(host='192.168.31.223', port=6610,
                           user='qph_b2c', password='zhaoyl(1181*%P)',
                           db='taobao20190813test', loop=loop) as pool:

        async with pool.get() as conn:
            async with conn.cursor() as cur:
                sql = '''SELECT COUNT(*) FROM taobao_list_web_2020_0113;'''
                await cur.execute(sql)
                value = await cur.fetchone()
                print(value[0])


# loop.run_until_complete(go())

# 改版后的异步连接数据库

# python 断言 https://www.runoob.com/python3/python3-assert.html
import asyncio
import aiomysql

async def test_example(loop):
    pool = await aiomysql.create_pool(host='192.168.31.223', port=6610,
                           user='qph_b2c', password='zhaoyl(1181*%P)',
                           db='taobao20190813test', loop=loop)
    # 用异步池获得 连接器
    async with pool.acquire() as conn:
        # 异步游标
        async with conn.cursor() as cur:
            sql = '''SELECT COUNT(*) FROM taobao_list_web_2020_0113;'''
            await cur.execute(sql)
            # await cur.execute('SELECT 42;')
            # (('COUNT(*)', 8, None, 21, 21, 0, False),)
            # 打印游标说明\描述
            print(cur.description)
            # < Future finished result = (150885,) >
            # 出现这种情况是因为没有在cur.fetchone() 前面加await
            value = await cur.fetchone()
            # print(value)
            print(value[0])
            # (r,) = await cur.fetchone()
            # 断言 r == 42
            # assert r == 42

    pool.close()
    await pool.wait_closed()

loop = asyncio.get_event_loop()
loop.run_until_complete(test_example(loop))


# 对象关系映射SQLAlchemy - Object Relationship Mapping
#
# 可以随意定义表结构，轻松调用查询、插入等操作方法。
import asyncio
import sqlalchemy as sa
from aiomysql.sa import create_engine
metadata = sa.MetaData()
tbl = sa.Table('tbl', metadata,
        sa.Column('id', sa.Integer, primary_key=True),
        sa.Column('val', sa.String(255)))
async def go(loop):
  engine = await create_engine(user='root', db='test_pymysql',
                 host='127.0.0.1', password='', loop=loop)
  async with engine.acquire() as conn:
    await conn.execute(tbl.insert().values(val='abc'))
    await conn.execute(tbl.insert().values(val='xyz'))
    async for row in conn.execute(tbl.select()):
      print(row.id, row.val)
  engine.close()
  await engine.wait_closed()
loop = asyncio.get_event_loop()
loop.run_until_complete(go(loop))