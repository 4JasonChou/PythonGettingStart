import json
import pymongo
import time

# InsertOrUpdate Dic _ 底層
def UpdateUnderIndexDic( underDic , key ):
	if key in underDic :
		underDic[key] = underDic[key] + 1
	else :
		underDic.update({key:1})
		
# InsertOrUpdate Dic _ 外層
def UpdateTopIndexDicV2( topDic , keyOne , keyTwoList ):
	# Key One 是否存在
	if not keyOne in topDic :
		topDic.update( { keyOne : { } } )
	for index in range(len(keyTwoList)) :
		UpdateUnderIndexDic(topDic[keyOne],keyTwoList[index])

# 辨認型別 , 移除單元為1的非名詞		
def IdentifyWordTypeV2( wordList ):
	resultList = []
	for word in wordList :
		key = word.split("/")
		if( key[-1][0] == "n"  ) :
			if not  key[0] in resultList :
			    resultList.append(key[0])
		elif ( key[-1] == "x") : 
			if( len(key[0]) > 1 ) :
				if not  key[0] in resultList : 
					resultList.append(key[0])
	return resultList


# MongoDB的 InsertAndUpdate
def UpdateKeywordV2( mongoDbCollection , mainKey , SubKeyList ):
	# 搜尋條件
	condition = {'MainKey': mainKey }
	# 搜尋結果
	result = mongoDbCollection.find_one(condition)
	# MainKey 不存在
	if result == None :
		# 新增
		newRecord = { 'MainKey': mainKey , 'SubKeyList':{ } }
		for size in range(len(SubKeyList)) :
			if( mainKey !=  SubKeyList[size] ) :
				newRecord['SubKeyList'][SubKeyList[size]] = 1 
		mongoDbCollection.insert_one(newRecord)
	# MainKey 存在
	else :
		# 更新
		for size in range(len(SubKeyList)) :
			if( mainKey !=  SubKeyList[size] ) :
				if SubKeyList[size] in result['SubKeyList'] :
					result['SubKeyList'][SubKeyList[size]] = result['SubKeyList'][SubKeyList[size]] + 1
				else :
					result['SubKeyList'][SubKeyList[size]] = 1
		mongoDbCollection.update_one(condition, {'$set': { 'SubKeyList': result['SubKeyList'] } } ,upsert=True )

# Main Start
print("LabTraining - Ch 1 KCM ")

# Init雙重的 Dic 
myUnderDic = { 'DefaultUnder' : 0 }
myTopDic = { 'DefaultTop' : myUnderDic }

# 1.開啟 Json Wiki資料
fileName = 'SampleEx2'
print("Loading file ...")
with open( fileName+'.json' , 'r' , encoding="utf-8" ) as reader:
	wikiSampleJson = json.loads(reader.read())

# 2.初始化 MongoDBClient
# MongoDBclient = pymongo.MongoClient(host='localhost', port=27017)
# db = MongoDBclient.PythonDB
# collection = db.Posseg_List9

localtime = time.asctime( time.localtime(time.time()) )
print("StartTime :", localtime)


print("Under processing ...")
# 3.處理資料
for key in wikiSampleJson :
	# 判斷與取得 一個 單字清單
	myNTypelist = IdentifyWordTypeV2( wikiSampleJson[key])
    # 對清單做CRUD
	for i in range(len(myNTypelist)) :
		UpdateTopIndexDicV2(myTopDic,myNTypelist[i],myNTypelist)


localtime = time.asctime( time.localtime(time.time()) )
print("EndTime :", localtime)

with open(fileName+'Result.txt', 'wt' , encoding="utf-8" ) as f:
	for key, value in myTopDic.items():
		for keyUd , valueUd in value.items():
			if(valueUd>0):
				res = '{} {} {}'.format(key,keyUd,valueUd)
				print(res, file=f)
