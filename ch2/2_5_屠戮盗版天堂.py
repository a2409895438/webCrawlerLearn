import requests
import re

domain = "https://www.dytt89.com/"
resp = requests.get(domain,verify=False)  #verify=False 去掉安全验证
resp.encoding = 'gb2312'
row_data = resp.text
resp.close()

obj1 = re.compile(r'2023必看热片.*?<ul>(?P<ul>.*?)</ul>',re.S)
result1 = obj1.search(resp.text)
print(result1.group("ul"))
