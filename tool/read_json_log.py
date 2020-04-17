# -*- coding: utf-8 -*-
# @Time    : 2019/12/25 14:10
# @Author  : Mqz
# @FileName: read_json_log.py
import json
# import 

# with open(r'D:\Spider\11月25日\1\taobao-master\20191225\taobao_item_trace_20191225095358.json', 'r', encoding='utf-8') as fp:
with open(r'D:\Spider\11月25日\1\taobao-master\20191225\taobao_item_trace_20191225135340.json', 'r', encoding='utf-8') as fp:
    count = 0
    for line in fp.readlines():
        count += 1
        # unicode转成中文.decode('unicode_escape')
        # print(type(json.loads(line)))
        if "'category': None," in str(json.loads(line)) or "'props': None," in str(json.loads(line)):
            print('没有数据')
            # break
            text1 = json.loads(line)
            with open('log', 'w') as fp:
                try:
                    # fp.write(text1)
                    fp.write(json.dumps(text1))
                    print('写入成功')
                except Exception as e:
                    print('写入失败')
        else:
            print('有数据')
            print(json.loads(line))
    print(count)


