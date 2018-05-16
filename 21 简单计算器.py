# -*- coding: UTF-8 -*-
def add(x,y):
    return x+y
def sub(x,y):
    return x-y
def mul(x,y):
    return x*y
def divide(x,y):
    return x/y

print("选择运算：")
print("1、相加")
print("2、相减")
print("3、相乘")
print("4、相除")

choice = input('请输入你的选择(1/2/3/4):')

num1=int(input('请输入x：'))
num2=int(input('请输入y: '))

if choice=='1':
    print(num1,'+',num2,'=',add(num1,num2))
elif choice=='2':
    print(num1,'-',num2,'=',sub(num1,num2))
elif choice=='3':
    print(num1,'*',num2,'=',mul(num1,num2))
elif choice=='4':
    print(num1,'/',num2,'=',divide(num1,num2))
else:
    print('非法输入')
