# coding:utf8
# 迭代方法打印1-N
import time,sys
sys.setrecursionlimit(100000) # 设置递归最深层次

def PrintN(N):
    for i in xrange(1, N + 1):
        print i

# 递归方法打印1-N
def PrintNum(N):
    if N:
        PrintNum(N - 1)
        print N
    return # 这里不写return 也不影响程序执行

N = 10000 # 我的电脑超过10000层递归 程序就直接退出

start = time.clock()
# PrintN(N)
PrintNum(N)
end = time.clock()

print '用时：%fs' % (end - start)