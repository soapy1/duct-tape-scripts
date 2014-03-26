import pymongo
import csv
import os

user = os.getenv('USER')
password = os.getenv('PASS')

server = "mongodb://%s:%s@widmore.mongohq.com:10010/mongodat"%(user, password)
con = pymongo.MongoClient(server)
db = con.get_default_database()

proto = {
    '_id':'',
    'cippg':'',
    '2002':'',
    '2003':'',
    '2004':'',
    '2005':'',
    '2006':'',
    '2007':'',
    '2008':'',
    '2009':'',
    '2010':''
    }

reader = csv.DictReader(open('AllPrograms6mosmodfield.csv'))
_id = 0
for row in reader:
    print row
    proto['_id'] = _id 
    proto['cippg'] = row['Institution']
    proto['2002'] = float(row['2002'])
    proto['2003'] = float(row['2003'])
    proto['2004'] = float(row['2004'])
    proto['2005'] = float(row['2005'])
    proto['2006'] = float(row['2006'])
    proto['2007'] = float(row['2007'])
    proto['2008'] = float(row['2008'])
    proto['2009'] = float(row['2009'])
    proto['2010'] = float(row['2010'])
    
    db.sixmonthempldat.insert(proto)
    print proto
    _id += 1
    print 'success ', _id

print 'done'
