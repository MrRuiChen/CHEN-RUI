# -*- coding: UTF-8 -*-
a=int(input('你需要多少项？'))
n1=0
n2=1
count=2
if a<=0:
    print('请输入一个正数')
elif a==1:
    print('斐波那切数列：')
    print(n1)
else:
    print('斐波那切数列：')
    print(n1,',',n2,end=" , ")
    while count < a:
        b=n1+n2
        print(b,end=" , ")
        n1=n2
        n2=b
        count+=1
