import requests


url = "https://movie.douban.com/j/chart/top_list"

param={
    "type": "24",
    "interval_id": "100:90",
    "action": "",
    "start": "0",
    "limit": "100"
}

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

resp = requests.get(url=url,params=param,headers=headers)

rs = resp.json()
resp.close()
print(type(rs))
print(type(rs[0]))



import xlsxwriter as xw

wb = xw.Workbook('text.xlsx')
ws = wb.add_worksheet("sheet1")

#表头heads，用于判断字典中的键值是否已存在
heads = []
answers = [rs]

#n用于确定行数，每循环到一个字典就加1
n = 0
#循环list1，list2
for answer in answers: 
	#以list1为例，循环小红和小白的信息
    for a in answer: 
        n += 1
        #获取字典中的键 
        for key in a.keys(): 
        	#判断每个键是否存在于heads，不存在则添加
            if key not in heads: 
                heads.append(key) 
                #将key添加至excel作为列名
                ws.write(0, len(heads)-1,key)
            #写入excel。ws.write(行，列，值)
            ws.write(n, heads.index(key), str(a[key])) 
wb.close()
