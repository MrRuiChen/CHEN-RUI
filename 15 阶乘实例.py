# -*- coding: UTF-8 -*-
num=int(input('请输入数字：'))
b=1
if num<0:
    print('没有负数阶乘，请重新输入：')
    num=int(input('请输入数字：'))
elif num==0:
    print('0的阶乘为 1 ')
else:
    for i in range(1,num+1):
        b=b*i
    print('%d的阶乘为%d' %(num,b))
