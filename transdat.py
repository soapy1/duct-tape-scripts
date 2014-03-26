import pymongo
import os

user = os.getenv('USER')
password = os.getenv('PASS')

server = "mongodb://%s:%s@widmore.mongohq.com:10010/mongodat"%(user, password)
con = pymongo.MongoClient(server)
db = con.get_default_database()

val = db.avgpaydat.aggregate([{'$group':{'_id':{'cippg':"$cippg", 'date':"$date"}, 'value':{'$avg':"$value"}}}]) 

tar = {
    '_id':'',
    'cippg':'',
    'date':'',
    'value':''
}

cnt = 0
for i in val['result']:
    tar['_id'] = cnt
    tar['cippg'] = i['_id']['cippg']
    tar['date'] = i['_id']['date']
    tar['value'] = i['value']
    cnt += 1
    db.paydat.insert(tar)
    print 'success ', cnt
    
        
