#!/usr/bin/env pytthon
# -*- coding: utf8 -*-
__author__ = 'Eagle'
import   time
start = time.clock()
log_dict = {}
# 1. 打开access.txt,定义一个空字典
log_file = file('access.txt')

for i in log_file:
    '''2. 通过空格作为分隔符，打散，每一行，取值，ip
       3. 元组里面内容作为key 默认值0 作为value,如果key，value存在就加+1，写入字典,关闭文件
    '''
    arr= i.split(' ')
    ip= arr[0]
    log_dict[ip] = log_dict.get(ip, 0) + 1
log_file.close()

# 4. 通过字典items方法，返回，key和value值，通过切片，取得key,元组里面的值，赋值给列表
log_list  = [(k,v) for  k,v in log_dict.items()]
print log_list
print "==============IP TOP10 信息=============="
#5. sorted 方法对log_list列表进行排序，通过列表第三个值进行，排序，通过reverse 升序排序，取前10个
for j  in sorted(log_list,key = lambda x:x[1], reverse=True)[:10]:

    print "IP: %s 出现次数：%s" % (j[0],j[1])
end = time.clock()
print "程序运行时间: %f s" % (end - start)