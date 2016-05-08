#-*- coding: utf-8 -*-

name = "Simon" # 中文 
age = 23
weight = 55.0
height = "173 cm"
hobby = "reading"

print "Let's talk about %s." % name
print "He's %s tall" % height
print "He's %f heavy" % weight
print "He's %d years old" % age
print "He likes %s" % hobby

"""
%c  转换成字符（ASCII 码值，或者长度为一的字符串）
%r  优先用repr()函数进行字符串转换（Python2.0新增）
%s  优先用str()函数进行字符串转换
%d / %i  转成有符号十进制数
%u  转成无符号十进制数
%o  转成无符号八进制数
%x / %X (Unsigned)转成无符号十六进制数（x / X 代表转换后的十六进制字符的大
小写）
%e / %E 转成科学计数法（e / E控制输出e / E）
%f / %F 转成浮点数（小数部分自然截断）
%g / %G %e和%f / %E和%F 的简写
%%  输出%

Document aboout String Format:
https://docs.python.org/2/library/string.html?highlight=string%20format#string.Formatter.format

"""
