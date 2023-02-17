from urllib import request
 
# 打开网站，返回响应对象resp
resp = request.urlopen('https://buaa.yuketang.cn/pro/portal/home/?next=https%3A%2F%2Fbuaa.yuketang.cn%2Fpro%2Flms%2F9P32z92iFqL%2F14280463%2Fstudycontent')
 
# 通过.read()读取这个网页的源代码，相当于在百度页面右键检查
# print(resp.read().decode("utf-8"))
# 返回网页信息

with open("beihang.html",mode="w") as f:
    f.write(resp.read().decode("utf-8"))
print("over")
 