#coding:utf8

# s = '123321'
s = u'清莲碧水照花红，水照花红碧云空，空云碧红花照水，红花照水碧莲清'

length = len(s)
mid = length/2

start = mid
if length % 2 != 0:
    start += 1

flag = 1
j = 1
for i in range(start,length):
    if s[i] != s[mid - j]:
        flag = 0
        break
    j += 1

if flag:
    print 'Yes'
else:
    print 'No'