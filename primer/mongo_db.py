# coding=utf-8
import pymongo

print ('pymongo test')
client = pymongo.MongoClient('localhost', 27017)
db = client.scrapy
connection = db.jobs

# insert
# connection.insert({'company': '北京远特科技股份有限公司',
#                    'link': 'http://jobs.zhaopin.com/383991117251394.htm',
#                    'name': 'Android驱动工程师',
#                    'salary': '15001-20000',
#                    'site': '深圳-南山区',
#                    'time': '15天前'}
#                   )

# query
item_one = connection.find_one()
count = connection.find().count()
item_all = connection.find()
print ('item_one', item_one)
print ('count', count)
for item in item_all:
    print ('item', item)

# remove
connection.remove()