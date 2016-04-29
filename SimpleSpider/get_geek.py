#coding:utf8
# 鱼c工作室copy
import re
import requests

head = {
            'Accept':'*/*',
            'Accept-Encoding':'identity;q=1, *;q=0',
            'Accept-Language':'zh-CN,zh;q=0.8',
            'Connection':'keep-alive',
            'Host':'cv3.jikexueyuan.com',
            'Range':'bytes=0-',
            'Referer':'http://www.jikexueyuan.com/course/202.html',
            'User-Agent':'Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/42.0.2311.152 Safari/537.36',
        }

##一定要写返回值是206（部分内容）的request

url = 'http://cv4.jikexueyuan.com/d44e88bc5008ffcfe5b3d30de0b88e4c/201604211428/course/2701-2800/2777/video/7739_b_h264_sd_960_540.mp4'
r = requests.head(url,headers = head,stream=True)

# url = r.headers['location']
# print(url)
# res = requests.head(url,headers = head,stream=True)
# print(res.status_code)

if (r.status_code == 302):
    url = r.headers['location']
    print(url)
    res = requests.head(url,headers = head,stream=True)
    print(res.status_code)
##确认响应类型