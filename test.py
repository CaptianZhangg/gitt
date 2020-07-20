import re


content = '0013::通讯异常:Connection refused::其它错误'
pattern ='\S+通讯异常+'
n = 0
result = re.search(pattern, content)
print(result)
if result:
    n+= 1
print(n)