import requests

url = "https://fanyi.baidu.com/sug"

s = input("请输入你要翻译的英文单词:")
dat = {
    "kw":s
}

resp = requests.post(url,data=dat,verify=False)
print(resp.json())
resp.close()