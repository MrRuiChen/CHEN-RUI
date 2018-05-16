# -*- coding: UTF-8 -*-
def recur_fibo(n):
    if n<=1:
        return n
    else:
        return(recur_fibo(n-1)+ recur_fibo(n-2))

num=int(input('请输入要几项？'))
if num<=0:
    print('请输入正数')
else:
    print('菲波那切数列为：')
    for i in range(num):
        print(recur_fibo(i))
