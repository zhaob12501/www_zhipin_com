# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql


class WwwZhipinComPipeline(object):
    def __init__(self):
        self.conn = pymysql.connect(
            host = 'localhost',
            user = 'root',
            passwd = 'qwe123',
            db = 'zhipin_db',
            charset = 'utf8'
        )
        self.cur = self.conn.cursor()

    def process_item(self, item, spider):
        pid = item.get('pid')
        positionName = item.get('positionName')
        workYear = item.get('workYear')
        salary = item.get('salary')
        city = item.get('city')
        education = item.get('education')
        companyShortName = item.get('companyShortName')
        industryField = item.get('industryField')
        financeStage = item.get('financeStage')
        companySize = item.get('companySize')
        positionLables = item.get('positionLables')
        time = item.get('time')
        updated_at = item.get('updated_at')
        introduction = item.get('introduction')

        sql = 'select pid from zhipin_table where pid = "%s";'.format(pid)
        self.cur.execute(sql)
        result = self.cur.fetchone()
        
        if not result:
            sql = 'insert into zhipin_table value("{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}", "{}");'.format(
                pid, positionName, salary, companyShortName, education, workYear,
                positionLables, city, companySize, industryField, financeStage,
                time, introduction, updated_at
            )


            self.cur.execute(sql)
            self.conn.commit()
            return item
        else:
            print('pid is existed. pid: {}'.format(pid))
            return item
        
        

    def __del__(self):
        self.cur.close()
        self.conn.close()
