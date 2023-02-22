import re
import requests
import csv

row_url = "https://movie.douban.com/top250"

headers={
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}

target = re.compile(r'<li>.*?<span class="title">(?P<name>.*?)</span>.*?'
                    r'<br>.*?(?P<year>[0-9]*?)&nbsp.*?</li>',re.S)

resp = requests.get(row_url,headers=headers)
data = resp.text
result = target.finditer(data)
for it in result:
    print(it.groupdict().values())
    
resp.close()
