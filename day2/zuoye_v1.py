#!/usr/bin/env  python
#_*_ coding:utf-8 _*_
__author__ = 'Eagle'
#1. 导入time模块，及Counter计数器模块
import   time
from collections import Counter
#2. 取当前时钟时间，打开文件，赋值一个空列表
start = time.clock()
log_file = file('access.txt')
#3. 循环日志文件，使用空格作为分隔符，取出，ip这个元素，写入列表，关闭文件

log_list = [i.split(' ')[0] for i in log_file]
log_file.close()

#4. 使用计数器模块counter计数，写入字典
log_dict = Counter(log_list)

#5. 循环列表，使用sorted进行降序排列，使用key 进行排序，取前十个元素
print "==============IP TOP10 信息=============="
for j in  sorted(log_dict.iteritems(), key=lambda x: x[1], reverse=True)[:10]:
    print "IP: %s 出现次数：%s" % (j[0], j[1])
	
#6. 赋值程序结束时间，并打印输出
end = time.clock()
print "程序运行时间: %f s" % (end - start)


