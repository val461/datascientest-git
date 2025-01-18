import re

print('Question (a).')

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

print('\nQuestion (b).\n')

print(client.list_database_names())

print('\nQuestion (c).\n')

sample = client["sample"]
print(sample.list_collection_names())

print('\nQuestion (d).\n')

col = sample.books
pprint(col.find_one())

print('\nQuestion (e).\n')

print(col.count_documents({}))

print('\nQuestion (a).\n')

print(col.count_documents({'pageCount': {'$gt': 400}}))
print(col.count_documents({'$and':[
    {'pageCount': {'$gt': 400}},
    {'status': 'PUBLISH'}
    ]}))

print('\nQuestion (b).\n')

regex = re.compile("Android")
print(col.count_documents(({'$or':[
    {'shortDescription': regex},
    {'longDescription': regex}
    ]})))

print('\nQuestion (c).\n')

p(col.aggregate([
    {'$group':
        {'_id': None,
        'c0': {'$addToSet': {'$arrayElemAt': ['$categories',0]}},
        'c1': {'$addToSet': {'$arrayElemAt': ['$categories',1]}}
    }}
]))

print('\nQuestion (d).\n')

print(col.count_documents(({'$or':
    [{'longDescription': re.compile(s)} for s in ['Python', 'Java', 'C\+\+', 'Scala']]
    })))

print('\nQuestion (e).\n')

p(col.aggregate([
    {'$unwind':'$categories'},
    {'$group':
        {'_id':'$categories',
        'max':{'$max':'$pageCount'},
        'min':{'$min':'$pageCount'},
        'moy':{'$avg':'$pageCount'},
        }
    }
]))

print('\nQuestion (f).\n')

p(col.aggregate([
    {'$project':{
        'year':{'$year': '$publishedDate'},
        'month':{'$month': '$publishedDate'},
        'dayOfMonth':{'$dayOfMonth': '$publishedDate'},
    }},
    {'$match':{
        'year':{'$gt':2009}
    }},
    {'$limit':20}
]))

print('\nQuestion (g).\n')

n = 7
print(f'Pour n={n}.\n')

d = {**{f'author_{k+1}':{'$arrayElemAt': ['$authors',k]} for k in range(n)},
     **{'publishedDate':'$publishedDate'}}

p(col.aggregate([
    {'$project': d},
    {'$sort': {'publishedDate':1}},
    {'$limit':20}
]))

print("\nCes documents n'avaient pas de publishedDate. Un tri décroissant (spécifier -1 au lieu de 1) montrerait des documents ayant une publishedDate, triés.\n")

print('\nQuestion (h).\n')

p(col.aggregate([
    {'$project': {'author':{'$arrayElemAt': ['$authors',0]}}},
    {'$group':{'_id':'$author', 'nb':{'$sum':1}}},
    {'$sort': {'nb':-1}},
    {'$limit':10}
]))


print('\nQuestion (i).\n')

p(col.aggregate([
    {'$project': {'nb':{'$size': '$authors'}}},
    {'$group': {'_id':'$nb', 'd':{'$sum':1}}}
]))

print('\nQuestion (j).\n')

p(col.aggregate([
    {'$unwind': '$authors'},
    {'$group': {'_id':'$authors', 'nb':{'$sum':1}}},
    {'$sort': {'nb':-1}},
    {'$match': {'_id':{'$ne': ''}}},
    {'$limit':20}
]))
