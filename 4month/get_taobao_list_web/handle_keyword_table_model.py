# -*- coding: utf-8 -*-
# @Time    : 2020/4/13 10:08
# @Author  : Mqz
# @FileName: handle_keyword_table_model.py
import datetime
from common.configs import db_util_4



KEYWORD = 'taobao_list_web_keyword_20204'

def update_crawl_page(crawl_page):
    """
    update crawl_page page num
    :return
    """
    upd_sql = 'UPDATE {0} SET crawl_page={1}'.format(KEYWORD, crawl_page)
    try:
        db_util_4.execute(upd_sql)
        print('【{0}】更新成功'.format(KEYWORD))

    except Exception as e:
        print('【{0}】更新失败'.format(KEYWORD))


def update_tmall_crawl_page(crawl_page):
    """
    update tmall_crawl_page page num
    :return
    """
    upd_sql = 'UPDATE {0} SET tmall_crawl_page = {1}'.format(KEYWORD, crawl_page)
    try:
        db_util_4.execute(upd_sql)
        print('【{0}】更新成功'.format(KEYWORD))

    except Exception as e:
        print('【{0}】更新失败'.format(KEYWORD))


def update_category_crawl_page(crawl_page):
    """
    update category_crawl_page page num
    :return
    """
    upd_sql = 'UPDATE {0} SET category_crawl_page = {1}'.format(KEYWORD, crawl_page)
    try:
        db_util_4.execute(upd_sql)
        print('【{0}】更新成功'.format(KEYWORD))

    except Exception as e:
        print('【{0}】更新失败'.format(KEYWORD))


def update_category_tmall_crawl_page(crawl_page):
    """
    update category_tmall_crawl_page page num
    :return
    """
    upd_sql = 'UPDATE {0} SET category_tmall_crawl_page = {1}'.format(KEYWORD, crawl_page)
    try:
        db_util_4.execute(upd_sql)
        print('【{0}】更新成功'.format(KEYWORD))

    except Exception as e:
        print('【{0}】更新失败'.format(KEYWORD))


def update_all_crawl_page(num):
    state_list = ['crawl_page', 'tmall_crawl_page', 'category_crawl_page', 'category_tmall_crawl_page']
    for state_name in state_list:
        Null = 'Null'
        upd_sql = 'UPDATE {0} SET {1} = {2}'.format(KEYWORD, state_name, num)
        try:
            db_util_4.execute(upd_sql)
            print('【{0}】更新成功'.format(KEYWORD))

        except Exception as e:
            print('【{0}】更新失败'.format(KEYWORD))


def update_all_crawl_state():
    state_list = ['crawl_state', 'tmall_crawl_state', 'category_crawl_state', 'category_tmall_crawl_state']
    for state_name in state_list:
        Null = 'Null'
        upd_sql = 'UPDATE {0} SET {1} = {2}'.format(KEYWORD, state_name, Null)
        try:
            db_util_4.execute(upd_sql)
            print('【{0}】更新成功'.format(KEYWORD))

        except Exception as e:
            print('【{0}】更新失败'.format(KEYWORD))


if __name__ == '__main__':

    # update_crawl_page(0)
    # update_tmall_crawl_page(0)
    # update_category_crawl_page(0)
    # update_category_tmall_crawl_page(0)
    # update_all_crawl_page(0)
    # update_all_crawl_state()
    pass