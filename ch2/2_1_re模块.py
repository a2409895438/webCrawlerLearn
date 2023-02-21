import re

# 匹配字符串中所有符合正则的内容
list = re.findall(r"\d+","sdad10059 \n,sda2da")


#FINDITER: 匹配字符串所有的内容【返回的是迭代器】,从迭代器中拿到内容需要.group()
it = re.finditer(r"\d+","sdad10059 \n,sda2da")
for i in it:
    print(i.group())
#search 返回的结果是MATHCH对象。拿数据需要.group()   检索到一个就返回
s = re.search(r"\d+","sdad10059 \n,sda2da")
print(s)

#从头开始匹配 相当于前面加个 ^
s = re.match(r"\d+","sdad10059 \n,sda2da")
print(s)

#预加载正则表达式
obj = re.compile(r"\d+")
it = obj.finditer("213s")

#rs.S:让.能匹配换行符    (?P<x>{匹配符})  拿到匹配符处的值——>i.group("x")
obj = re.compile(r"1(?P<x>.*?)23",re.S)
it = obj.finditer("""1xxxx23s
sdasd
asdas
2111123""")
for i in it:
    print(i.group("x"))