import json

# InsertOrUpdate Dic _ 底層
def UpdateUnderIndexDic( underDic , key ):
	if key in underDic :
		underDic[key] = underDic[key] + 1
	else :
		underDic.update({key:1})
		
# InsertOrUpdate Dic _ 外層
def UpdateTopIndexDic( topDic , keyOne , keyTwo ):
	if keyOne in topDic :
		UpdateUnderIndexDic(topDic[keyOne],keyTwo)
	else :
		tempUderDic = { keyTwo : 1 }
		topDic.update( { keyOne : tempUderDic } )
		
# 辨認型別 , 移除單元為1的非名詞		
def IdentifyWordType( word ):
	key = word.split("/")
	if( key[-1] == "ns" or key[-1] == "n"  ) :
		return key[0]
	elif ( key[-1] == "x") : 
		if( len(key[0]) > 1 ) :
			return key[0]
	return "X"
	
	
# Main Start
print("Hello Lab. - Ch 1 KCM ")

# Init雙重的 Dic 
myUnderDic = { 'DefaultUnder' : 0 }
myTopDic = { 'DefaultTop' : myUnderDic }
# 將資料分別放入 myTopDic 中
# 開啟 Json Wiki資料
with open('SampleEx.json' , 'r' , encoding="utf-8" ) as reader:
	wikiSampleJson = json.loads(reader.read())


dic ={}
def json_txt(wikiSampleJson):
    if isinstance(wikiSampleJson,dict): #判断是否是字典类型isinstance 返回True false     
        for key in wikiSampleJson:
            if isinstance(wikiSampleJson[key],dict):#如果dic_json[key]依旧是字典类型
                json_txt(wikiSampleJson[key])
                dic[key] = wikiSampleJson[key]
            else:
                dic[key] = wikiSampleJson[key]
                
json_txt(wikiSampleJson)
#print("dic ---: "+str(dic))

print("Res : ")

myNTypelist = []

for key , values in dic.items():
	myNTypelist = []
	for value in values :
		reV = IdentifyWordType(value)
		if( reV != "X" ):
			if not  reV in myNTypelist :
			    myNTypelist.append(reV)
	for i in range(len(myNTypelist)) :
		for j in range(len(myNTypelist)) :
			if( i != j ) :
				UpdateTopIndexDic(myTopDic,myNTypelist[i],myNTypelist[j])
		
# Show Result
for key, value in myTopDic.items():
	for keyUd , valueUd in value.items():
		if(valueUd>1):
			print( key, keyUd , valueUd)

				
# 空列表


#list.append('Runoob')

#print(IdentifyWordType(dic['494255'][0]))


#JackKey = {'Ben' : 1 } ;
#myTopDic.update( { 'Jack' : JackKey } );
#UpdateUnderIndexDic(myTopDic['Jack'],'Ben');
#print( myTopDic['DefaultTop']['DefaultUnder'] );
#print( myTopDic['Jack']['Ben'] )
#UpdateTopIndexDic(myTopDic,'Jack2','Lee');
#print( myTopDic['Jack2']['Lee'] )
# 顯示所有資料





