# (a)

from pymongo import MongoClient

from pprint import pprint

client = MongoClient(
    host="127.0.0.1",
    port = 27017,
    username = "datascientest",
    password = "dst123"
)

def p(l):
    pprint(list(l))

# (b)

print(client.list_database_names())

# (c)

sample = client["sample"]
print(sample.list_collection_names())

# (d)

col = sample.books
pprint(col.find_one())

# (e)

print(col.count_documents({}))

# (a)

print(col.count_documents({'pageCount': {'$gt': 400}}))
print(col.count_documents({'$and':[
    {'pageCount': {'$gt': 400}},
    {'status': 'PUBLISH'}
    ]}))

# (b)

import re
regex = re.compile("Android")
print(col.count_documents(({'$or':[
    {'shortDescription': regex},
    {'longDescription': regex}
    ]})))

# (c)

p(col.aggregate([
    {'$group':
        {'_id': None,
        'c0': {'$addToSet': {'$arrayElemAt': ['$categories',0]}},
        'c1': {'$addToSet': {'$arrayElemAt': ['$categories',1]}}
    }}
]))





# ()


