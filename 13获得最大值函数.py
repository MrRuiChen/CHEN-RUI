# -*- coding: UTF-8 -*-
N=int(input('请输入你要对比大小数字的个数：'))
print('请输入你要对比的数字：')
num=[]
for i in range(1,N+1):
    temp=int(input('输入第%d个数字'%i))
    num.append(temp)
print('输入的数字为： ',num)
print('最大值为： ',max(num))
