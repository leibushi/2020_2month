# -*- coding: utf-8 -*-
# @Time    : 2020/1/15 16:52
# @Author  : Mqz
# @FileName: crawl_taobao_category_id.py
import random

from selenium import webdriver
from time import sleep
import requests
# drvier = webdriver.Chrome()
# urll = 'https://router.publish.taobao.com/router/publish.htm'
# url = 'https://router.publish.taobao.com/router/publish.htm'
# drvier.get(url)
# sleep(10)
# keyword = '化妆/美容工具'
# # btn = drvier.find_element_by_link_text('地图').click()
# btn = drvier.find_element_by_class_name('next-input next-medium').send_keys(keyword)
#
# # drvier.find_element_by_id('sole-input').send_keys('太和')
# drvier.find_element_by_class_name('next-btn next-medium next-btn-normal search-btn').click()
# ditu = drvier.page_source
# print(ditu)

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
            'cookie':'x-gpf-render-trace-id=0b51065815821622397525894e827e; thw=cn; hng=CN%7Czh-CN%7CCNY%7C156; UM_distinctid=16cd81a2da22d4-0eedc85ef194ac-3c604504-1fa400-16cd81a2da36e9; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; enc=sXepPGx%2FjtSO63pLy0PAdksR%2FOzGUjuXt%2Fpf40ncBliuSFokBD9T3rkMrOiLWdL%2FfqBR0eOfpx76IHpuIWWTLw%3D%3D; t=bf223012d750fd4b1402b855cc70cd42; cookie2=1c549e45db0beb6bcf9b13f789e5ec90; _tb_token_=566efb8b3e836; _samesite_flag_=true; mt=ci=0_0; v=0; cna=LBDYFaEiqmwCAXFvyEmGEP09; sgcookie=DHPNvG%2FMfGLkAfUtQcdGA; unb=832104100; uc3=nk2=szPk9ZOHgyHJa2HK&lg2=VFC%2FuZ9ayeYq2g%3D%3D&id2=W8rqJfpgT7WX&vt3=F8dBxdz3pAYZMpHQAw4%3D; csg=a6117b3e; lgc=%5Cu8C22%5Cu654F20112683; cookie17=W8rqJfpgT7WX; dnk=%5Cu8C22%5Cu654F20112683; skt=7e327ecd354a238d; existShop=MTU4MjE2MjIwNw%3D%3D; uc4=nk4=0%40sUy0Hukam%2Fk2WByhDo9L3%2BFkol8Gjrk%3D&id4=0%40Wengf3FS0MQ4ZcGrV4RjUN%2B%2Bj%2Fk%3D; tracknick=%5Cu8C22%5Cu654F20112683; _cc_=W5iHLLyFfA%3D%3D; tg=0; _l_g_=Ug%3D%3D; sg=30a; _nk_=%5Cu8C22%5Cu654F20112683; cookie1=VWhaxEGo6XgRXh8JWd6KjpGPwo8KJ26c%2BJnDEP5zWuQ%3D; tfstk=b#EmVBj2/gnK2AHZb5kEa1CIDkjDAZkMmIgyQo240lCuR684cMulOMgOBCZg5W; _m_h5_tk=5aadfeed5f8dc115817f89881b07191b_1582171931197; _m_h5_tk_enc=8b3eed9ae6a812e92291c762b0434ac8; XSRF-TOKEN=a72df0db-919a-4301-b7e2-7a9e54baa1ce; uc1=cookie14=UoTUOLIsp9j6QA%3D%3D&lng=zh_CN&cookie16=WqG3DMC9UpAPBHGz5QBErFxlCA%3D%3D&existShop=true&cookie21=VT5L2FSpccLuJBreKQgf&tag=8&cookie15=U%2BGCWk%2F75gdr5Q%3D%3D&pas=0; l=cBTw5kYIQEoF9xFWBOCgquI81I_tkIRVguPRwG7wi_5I51L6zuQOoWspLep6cjWFGJL94IFj7TyTQFZ0-y8fEtmjSxnN6l1..; isg=BLCw6pg-mv6HnkapluVLpBqEgX4C-ZRDC1zxwqoBBIveZVIPVwtB0gETvW0FdUwb',
            # 'cookie':'x-gpf-render-trace-id=0b5114ad15790782688741727e36b5; thw=cn; t=4b607ccbf9ca482d28dd5643b67b8b6f; hng=CN%7Czh-CN%7CCNY%7C156; UM_distinctid=16cd81a2da22d4-0eedc85ef194ac-3c604504-1fa400-16cd81a2da36e9; x=e%3D1%26p%3D*%26s%3D0%26c%3D0%26f%3D0%26g%3D0%26t%3D0%26__ll%3D-1%26_ato%3D0; enc=sXepPGx%2FjtSO63pLy0PAdksR%2FOzGUjuXt%2Fpf40ncBliuSFokBD9T3rkMrOiLWdL%2FfqBR0eOfpx76IHpuIWWTLw%3D%3D; cna=LBDYFaEiqmwCAXFvyEmGEP09; lgc=%5Cu8C22%5Cu654F20112683; tracknick=%5Cu8C22%5Cu654F20112683; _cc_=URm48syIZQ%3D%3D; tg=0; cookie2=14a893f66efcda4d7a5fa3703226a491; _tb_token_=55bb38ebba555; v=0; mt=ci=-1_0; _m_h5_tk=35cbb3044fb6a994c270728d7164bf0f_1579083820820; _m_h5_tk_enc=16ec238c2441979b90a87cf7d8ccb78a; unb=832104100; uc3=vt3=F8dBxdkIpO%2BeRe%2BELhE%3D&nk2=szPk9ZOHgyHJa2HK&lg2=UIHiLt3xD8xYTw%3D%3D&id2=W8rqJfpgT7WX; csg=209ec0cc; cookie17=W8rqJfpgT7WX; dnk=%5Cu8C22%5Cu654F20112683; skt=f5aabde7df7603b8; existShop=MTU3OTA3ODIyMA%3D%3D; uc4=nk4=0%40sUy0Hukam%2Fk2WByhDo9L0ITEn%2FwcA%2Fk%3D&id4=0%40Wengf3FS0MQ4ZcGrWBceAmfsSqQ%3D; _l_g_=Ug%3D%3D; sg=30a; _nk_=%5Cu8C22%5Cu654F20112683; cookie1=VWhaxEGo6XgRXh8JWd6KjpGPwo8KJ26c%2BJnDEP5zWuQ%3D; XSRF-TOKEN=7ec95705-8d32-4cb5-bab3-b8ed1d7102ee; uc1=cookie14=UoTblAcDPrPBTg%3D%3D&lng=zh_CN&cookie16=V32FPkk%2FxXMk5UvIbNtImtMfJQ%3D%3D&existShop=true&cookie21=V32FPkk%2FgihF%2FS5nrepr&tag=8&cookie15=WqG3DMC9VAQiUQ%3D%3D&pas=0; l=cBTw5kYIQEoF9-sUBOfwiuI81n_TapdfBsPzw4swEICPOzID5oBlWZDe-lJkCnGVLsKMb3RYGVWzBuY_my4UlTXmcVDxb1E1.; isg=BBcXC8ywBXBUh4H8lWBEyakZpothXOu-eLF2t2lL6ubbmATaZi5jD9B--jiGcMM2',
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
