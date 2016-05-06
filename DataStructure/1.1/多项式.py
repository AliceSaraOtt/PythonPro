# coding:utf8
# 多项式求和两种算法
import time

# 最简单最直接最笨的方法
def fun1(n, a, x):
    res = a[0]
    for i in xrange(1, n + 1):
        res += a[i] * (x ** i)
    return res

# 秦九韶提取公因子X法
def fun2(n, a, x):
    res = a[n]
    for i in xrange(n, 0, -1):
        res = a[i - 1] + x * res
    return res

n = 1000 # 多项式的最大项数，即多项式阶数+1
a = [i for i in xrange(0,n)]
x = 1.1
times = 10000000

start = time.clock()
sum = fun2(n-1, a, x)
end = time.clock()
print "%fs" % (end - start)

# 需要解决问题
# 1.秦九韶算法