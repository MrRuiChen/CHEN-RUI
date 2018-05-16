# -*- coding: UTF-8 -*-
with open('123.txt','wt')as out_file:
    out_file.write('这个文字会写到txt里面\n 换行一下')

with open('123.txt','rt')as in_file:
    text=in_file.read()

print(text)
