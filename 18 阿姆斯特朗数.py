# -*- coding: UTF-8 -*-
a=int(input('请输入一个数字：'))
sum=0
n=len(str(a))
temp=a
while temp>0:
    digit = temp % 10
    sum += digit ** n
    temp //=10          #整数除法
if a==sum:
    print(a,'是阿姆斯特朗数')
else:
    print(a,'不是阿姆斯特朗数')
