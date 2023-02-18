import requests

query = input("请输入查询信息:")
url = f'http://www.sogou.com/web?query={query}'

#加入user agent，处理一个小小的反爬
dic = {
    "User-Agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 Safari/537.36"
}
resp = requests.get(url,headers=dic)
resp.close()
print(resp)
print(resp.text) #页面源代码
