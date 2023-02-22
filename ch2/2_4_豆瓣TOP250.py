import re
import requests
import csv

row_url = "https://movie.douban.com/top250"

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

target = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?'
                    r'<br>.*?(?P<year>[0-9]*?)&nbsp'
                    r'.*?<span class="rating_num" property="v:average">(?P<score>.*?)</span>'
                     r'.*?<span class="inq">(?P<quote>.*?)</span>'
                    r'.*?</li>',re.S)
f = open("data.csv",mode="w",newline='')
csvwriter = csv.writer(f)
title = ["电影名","年份","评分","quote"]
csvwriter.writerow(title)

for i in range(10):
    url = row_url + "?start=%d"%(i*25)
    print(url)
    resp = requests.get(url,headers=headers)
    data = resp.text
    result = target.finditer(data)
    for it in result:
        
        csvwriter.writerow(it.groupdict().values())
    resp.close()


f.close()


# a=r'123'
# r'123'
# print(a)

# f = open("data.csv",mode="w")
# csvwriter = csv.writer(f)

# csvwriter.writerow()