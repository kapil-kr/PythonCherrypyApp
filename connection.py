import redis
import json
import CSVReader
#from CSVReader import *

rconn = redis.Redis('localhost',decode_responses=True)
#redis.StrictRedis(decode_responses=True)


def SaveData():
    rows,fields = CSVReader.fileReader()
    reqIndex = [0,1,4,5,6,7]   # for the requested fields
    #creating dictionary from the retrieved data 
    for row in rows[:5]:
        str ={}
        for i in reqIndex:
            str[fields[i]] = row[i]
        
        rconn.hmset(row[0],str)

Keys = rconn.keys()

def VisibleFields():
    #vFields=[]
    tempd = rconn.hgetall(Keys[0])
    vFields = dictolistutil(tempd,key=True)
    return vFields
 
def VisibleData():
    vData=[]
    try:
        Keys.remove('name')
        Keys.remove('Sachin')
    except ValueError:
        pass
    for key in Keys[:5]:
        tempd = rconn.hgetall(key)
        val = dictolistutil(tempd,value=True)
        str = " ".join(x for x in val)
        vData.append(str)
    return vData

def dictolistutil(dic, key=None, value = None):
    lKey = []
    lValue =[]
    
    if key:
        lKey = list(dic.keys())
        return lKey
    else:
        lValue = list(dic.values())
        return lValue

def getResultbyName(name):
    vData=[]
    for key in Keys[:5]:
        tempd = rconn.hgetall(key)
        print(tempd)
        if (tempd['SC_NAME']).strip() == name.strip():
            val = dictolistutil(tempd,value=True)
            str = " ".join(x for x in val)
            vData.append(str)
    return vData


#print(rconn.hgetall("500002"))
SaveData()
#print(VisibleData())
#print(VisibleFields())