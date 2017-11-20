import redis
from pymongo import MongoClient
import json

# 链接redis
redis_cli= redis.Redis(host='127.0.0.1',port=6379,db=0)

# 链接到mongodb中
mongo_cli = MongoClient(host='127.0.0.1',port=27017)

# 在mongodb中创建数据库,或者链接到对应的数据库中

db= mongo_cli.book

# 创建集合对象

col = db['zhaopin']


while True:
    source,data = redis_cli.blpop(['zl:items'])
    str_data =data.decode()
    dict_data = json.loads(str_data)
    print(dict_data)
    # 写入mongodb数据库
    col.insert(dict_data)
