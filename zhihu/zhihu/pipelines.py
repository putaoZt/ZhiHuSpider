# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql
from scrapy.utils.project import get_project_settings


class ZhihuPipeline(object):

    def __init__(self):

        self.settings = get_project_settings()
        self.connect = pymysql.connect(
            host=self.settings['MYSQL_HOST'],
            db=self.settings['MYSQL_DBNAME'],
            user=self.settings['MYSQL_USER'],
            passwd=self.settings['MYSQL_PASSWD'],
            charset=self.settings['MYSQL_CHARSET'],
            use_unicode=True
        )
        self.cursor = self.connect.cursor()

    def process_item(self, item, spider):

        sql = 'insert into Scrapy_test.zhihuQuestion(name,url,keywords,answer_count,' \
              'flower_count,comment_count,date_created) values (%s,%s,%s,%s,%s,%s,%s)'
        self.cursor.execute(sql, (item['name'], item['url'], item['keywords'], item['answer_count'],
                                  item['flower_count'], item['comment_count'], item['date_created']))
        self.connect.commit()
        return item

