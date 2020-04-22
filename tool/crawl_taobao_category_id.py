# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 16:52
# @Author  : Mqz
# @FileName: crawl_taobao_category_id.py
"""
假睫毛辅助工具
假睫毛工具镊子
假睫毛工具胶水
化妆套刷
美甲工具
美容修剪器
睫毛卷翘器
面扑/粉扑
女用剃毛刀
洗脸刷/化妆刷
洗漱包
化妆包
化妆箱/盒
口红收纳包/盒/袋
面膜收纳盒/袋
桌面收纳盒
化妆品收纳架
洗漱包/化妆包
"""
import json
from urllib import parse
def get_category_data():
    # lists_data = ['化妆/美容工具', '化妆棉', '化妆刷', '假睫毛', '假睫毛工具', '双眼皮胶水', '双眼皮贴']
    # lists_data = ['假睫毛辅助工具', '假睫毛工具镊子', '假睫毛工具胶水', '化妆套刷', '美甲工具', '美容修剪器', '睫毛卷翘器',
    #               '面扑/粉扑', '女用剃毛刀', '洗脸刷/化妆刷', '洗漱包', '化妆包', '化妆箱/盒', '口红收纳包/盒/袋', '面膜收纳盒/袋',
    #               '桌面收纳盒', '化妆品收纳架', '洗漱包/化妆包']
    lists_data = ['假睫毛工具镊子', '假睫毛工具胶水', '化妆套刷', '美甲工具']
    for keyword in lists_data:
    # keyword = '化妆/美容工具'
        keyword1 = parse.quote(keyword)
        # print(keyword1)
        url = 'https://router.publish.taobao.com/router/asyncOpt.htm?optType=categorySearch&keyword={}'.format(keyword1)
        headers = {
            'cookie':'',
            'dnt': '1',
            'referer': 'https://router.publish.taobao.com/router/publish.htm',
            'user-agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/63.0.3239.132 Safari/537.36',
        }
        res = requests.get(url=url, headers=headers)
        print(res.status_code)
        print(res.text)
        # print(type(res.text))
        dicts_data = json.loads(res.text)['data']
        # print(dicts_data)
        # {'id': 50010817, 'name': '化妆/美容工具', 'path': ['彩妆/香水/美妆工具', '美容工具', '化妆/美容工具'],
        #  'idpath': [50010788, 122438001, 50010817], 'publish': True, 'isBrand': False, 'leaf': False, 'submitId': 50010817,
        #  'tips': '请您在发布商品时正确选择类别和品牌、容量等信息，违规发布的商品将不能正常展示，并且会被淘宝网处罚。'}
    
        for i in dicts_data:
            # print(i)
            if keyword in str(i):
                # print(i)
                path = i['path']
                idpath = i['idpath']
                try:
                    path_index = path.index(keyword)
                    # print(path_index)
                    keywords = path[path_index]
                    id_index = idpath[path_index]
                    if keywords == keyword:

                        print(id_index, keywords)
                        print('数据正常')
                    else:
                        print('没有数据')

                except Exception as e:
                    # print('有问题')
                    None
                sleep_times = random.random()
                sleep(sleep_times)
                # path的解析
                # for keywords, ids in path, idpath:
                # keywords = None
                # 这样只会得到最后一个
                # for keywords in path:
                #     # print(keywords)
                #     None
                # ids = None
                # for ids in idpath:
                #     # print(keywords, ids)
                #     None
                # print(keywords, ids)



get_category_data()

# datas = {"success":true,"data":[{"id":50006188,"name":"组合套装","path":["五金/工具","手动工具","工具组合套装","组合套装"],"idpath":[50020485,50020487,50020520,50006188],"publish":true,"isBrand":false,"leaf":false,"submitId":50006188},{"id":50021397,"name":"剥线钳","path":["五金/工具","手动工具","夹持类工具","剥线钳"],"idpath":[50020485,50020487,50020503,50021397],"publish":true,"isBrand":false,"leaf":false,"submitId":50021397},{"id":50014822,"name":"多功能组合工具","path":["户外/登山/野营/旅行用品","刀具/多用工具","多功能组合工具"],"idpath":[50013886,50014759,50014822],"publish":true,"isBrand":false,"leaf":false,"submitId":50014822},{"id":50013469,"name":"五金工具箱","path":["五金/工具","手动工具","工具包/箱/车","五金工具箱"],"idpath":[50020485,50020487,50020521,50013469],"publish":true,"isBrand":false,"leaf":false,"submitId":50013469},{"id":50023169,"name":"化妆包","path":["收纳整理","家庭收纳用具","收纳包","化妆包"],"idpath":[122928002,122964001,122964002,50023169],"publish":true,"isBrand":false,"leaf":false,"submitId":50023169},{"id":50010817,"name":"化妆/美容工具","path":["彩妆/香水/美妆工具","美容工具","化妆/美容工具"],"idpath":[50010788,122438001,50010817],"publish":true,"isBrand":false,"leaf":false,"submitId":50010817,"tips":"请您在发布商品时正确选择类别和品牌、容量等信息，违规发布的商品将不能正常展示，并且会被淘宝网处罚。"},{"id":50020810,"name":"工具车","path":["商业/办公家具","发廊/美容家具","工具车"],"idpath":[50020611,50020677,50020810],"publish":true,"isBrand":false,"leaf":false,"submitId":50020810},{"id":50009202,"name":"随身化妆镜","path":["家庭/个人清洁工具","个人洗护清洁用具","梳子/便携用镜","随身化妆镜"],"idpath":[50016348,50009146,50009201,50009202],"publish":true,"isBrand":false,"leaf":false,"submitId":50009202,"tips":"个人随身便携式用镜"},{"id":50012019,"name":"旅行箱","path":["箱包皮具/热销女包/男包","旅行箱"],"idpath":[50006842,50012019],"publish":true,"isBrand":false,"leaf":false,"submitId":50012019},{"id":50012010,"name":"女士包袋","path":["箱包皮具/热销女包/男包","女士包袋"],"idpath":[50006842,50012010],"publish":true,"isBrand":false,"leaf":false,"submitId":50012010,"tips":""}]}
