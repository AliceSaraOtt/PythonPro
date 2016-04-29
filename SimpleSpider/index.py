#coding:utf8
import requests as req, re

# headers = {'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/45.0.2454.101 Safari/537.36'}
# html = req.get('http://www.baidu.com',headers = headers)

res = req.request('get','http://www.jikexueyuan.com/course/2555_1.html')

# s = '<a>蓝思科技的看1<a>'
# s += '<a>蓝思科技的看2<a>'
# s += '<a>蓝思科技的看3<a>'
#
# m = re.findall(r'<a>(.*?)<a>',s,re.S)   # ? 开启非贪婪模式   re.S 表示把字符串看做一个整体匹配，不区分\r\n
#
# for v in m:
#     print v

print res.headers

