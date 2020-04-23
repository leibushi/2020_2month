"""
把公司淘宝mysql数据库里的数据插入mongodb数据库taobao_shop中
"""
import datetime

import pymongo
# 方法一
from dateutil import parser
# 方法二不行
import urllib.parse
from common import mysqlutils


config1 = {

    "host": "",
    "user": "",
    "password": "",
    "db": "",
    "charset": "utf8",
    "port": 
}
db_util1 = mysqlutils.MysqlUtil(config_dict=config1, pool_size=10)

config = {
    # 测试机
    "host": "",
    "user": "",
    "password": "",
    # "db": "",
    "db": "",
    "charset": "utf8",
    "port": 
}

db_util = mysqlutils.MysqlUtil(config_dict=config, pool_size=10)

# mongodb 数据库
client = pymongo.MongoClient('mongodb://:27017/')
db = client['taobao']
db.authenticate("taobao", "")

def get_datas(limit):
# def get_data():
    # 查询得到370的数据
    sql = "select shop_id from taobao_item_201906_copy1 WHERE create_ts >= '2019-09-27 01:17:25' limit {}".format(limit)
    # result = db_util1.queryall(sql)
    result = db_util.queryall(sql)
    print("nid %s" % result)
    return result


def get_data2(nids):
    count = 0
    for nid in nids:
        count += 1
        print(nid)
    # for
    # 查询得240k的数据
        sql = "SELECT * From taobao_item WHERE id = {}".format(nid)
        # reslult = db_util1.execute(sql)
        reslult = db_util1.queryall(sql)
        yield reslult



def get_shop_ids(limit):
    "获取mysql里的产品数据shop_id"
    sql = '''SELECT shop_id FROM taobao_item_201906_copy1 WHERE create_ts >= '2019-09-27 09:00:01' AND state = 0 limit
     {};'''.format(limit)
    result = db_util1.queryall(sql)
    print(result)
    return result


def handle_data_update(ids):
    # 对数据状态进行更新
    # print(resuorce)
    # for id in resuorce:
        # print(id)
        # ids = id['nid']
        # print(ids)
    update_sql = 'UPDATE taobao_shop_20200323 SET state=1 WHERE shop_id=%s'
    try:
        # db_utils.execute(update_sql, (ids))
        db_util1.execute(update_sql, (ids))
        print('更新成功')
    except Exception as e:
        print('更新失败')
        print(e)



# def get_shop_datas(shop_ids):
def get_shop_datas():
    """获取mysql里的taobao_shop数据"""
    # sql = '''SELECT * FROM taobao_shop_0927 WHERE shop_id = {} and state = 1;'''.format(ids)
    # sql = '''SELECT * FROM taobao_shop_copy1 WHERE state = 0;'''
    sql = '''SELECT * FROM taobao_shop_20200323;'''
    result = db_util1.queryall(sql)
    # result = db_util1.queryone(sql)
    # print(count)
    # print(result)
    # print(len(result))
    return result
    # yield result


def query_data(nids):
    "查询mongodb里的数据"
    count = 0
    for nid in nids:
        count += 1
        print(nid)
        # for x in db.taobao_seller.find():
        #     print(x)

        # mydoc = {"createTime": {"$gt": "2019-08-07 10:00:01"}}
        '''pymongo需要将一条记录从一个Mongo同步到另一个mongo中去，其中doc中有时间字段，
        为ISODate格式，python无法识别该格式，需要做下处理，为了简单这里仅写一个测试脚本，用来将ISODate格式的数据插入mongo中。'''
        dataStr = "2019-08-07 10:00:01"

        # myDatetime = parser.parse(dataStr)
        myDatetime = nid

        # 进行编码quote  unquote进行解码 这个不行
        # myDatetime = urllib.parse.unquote(dataStr)
        # mydoc = {"createTime": {"$gte": ISODate("2019-08-07 10:00:01")}}
        # mydoc = {"createTime": {"$gte": myDatetime}}
        # mydoc = {"itemId": {"$gte": myDatetime}}
        # mydoc = {"itemId": {"$e": myDatetime}}

        # result = db.taobao_item.find({itemId:nid})
        # result = db.taobao_item.find({},{'itemId':nid})
        result = db.taobao_item.find({'itemId': nid})
        for res in result:
            print(res)
        # print(result)
        # for x in db.taobao_seller.find(mydoc):
        # for x in db.taobao_item.find(mydoc):
        #     count += 1
        #     print(x)
        #     print(type(x))

    print("总共多少%d个" % count)
'''
    # query_dt = ""
'''


def insert_data(data):
    count = 0
    print(data)
    for dt in data:
        count += 1
        print(dt)
        # print(type(dt))
        # shop_url = dt.get_brand_product_id('shop_url')
        print('第%d个' % count)

        db = client['taobao']
        db.authenticate("taobao", "et78%20Aytb")
        # datas = {'shopId': dt.get_brand_product_id('shop_id'), 'userId': dt.get_brand_product_id('user_id', ), 'shopName': dt.get_brand_product_id('shop_name'),
        datas = {'shopId': dt.get('shop_id'), 'userId': dt.get('user_id',), 'shopName': dt.get('shop_name'),
                 'shopUrl': dt.get('shop_url'), 'taoShopUrl': dt.get('tao_shop_url'), 'shopIcon': dt.get('shop_icon'),
                 'fans': dt.get('fans'), 'allItemCount': dt.get('all_item_count'), 'sellerType': dt.get('seller_type'),
                 'shopType': dt.get('shop_type'), 'seller_nick': dt.get('sellerNick'), 'starts': dt.get('starts'),
                 'createTime': dt.get('create_ts')}
        print(datas)
        now = datetime.datetime.now()
        try:
            # 参考地址 https://www.cnblogs.com/knighterrant/p/10920308.html
            db.taobao_seller.insert_one(datas)
            # db.taobao_seller.update({'shopId': dt.get_brand_product_id('shop_id')},{'$set':datas},True)
            # db.taobao_seller1.update_one({'shopId': dt.get_brand_product_id('shopId')},
            # db.taobao_seller.insert_one({'shopId': dt.get_brand_product_id('shopId')},
            #                             {'$set': dt, '$setOnInsert': {'createTime': now}},
            #                             upsert=True)
            # result = db_util.execute(insert_db, (nid1, raw_title, category, url, cat_name))
            # result = db_util.execute(insert_db, (sell_count, nid1))
            # result = db_util.execute(insert_db)
            print("存入成功")
            handle_data_update(dt.get('shop_id'))
        except Exception as e:
            # print(type(e))
            # for x in e:
            #     print(x)

            # if 'taobao.taobao_seller index: shopId_1 dup key' in e:
            #     print('数据库存在')
            #     handle_data_update(dt.get_brand_product_id('shop_id'))

            print("存入失败%s" % e)
            # print(e)

        # except 'error collection: taobao.taobao_seller index' as e:
        # except DuplicateKeyError as e:
        #     print('重复',e)
        #     handle_data_update(dt.get_brand_product_id('shop_id'))
"""        """

    # sql = ""

def main():
    # nids = get_datas(20)

    # get_data(20)
    # data = get_data(20000000)
    # 查询mongodb的数据
    # query_data(nids)
    # insert_data(data)
    # data = get_data(200000)
    # insert_data(data)
    # shop_ids = get_shop_ids(20000)
    # datas = get_shop_datas(shop_ids)
    datas = get_shop_datas()
    insert_data(datas)
    # handle_data_update(resuorce)

if __name__ == '__main__':
    main()
