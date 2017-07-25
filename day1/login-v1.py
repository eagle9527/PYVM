#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import  sys
counts = 0 

while  counts   < 3 : 
    Username = raw_input('Please input you name:')       #读取user_lockd.txt 判断用户是否被锁定
    user_locked = file('user_lockd.txt')
    for  lines in  user_locked.readlines():
        if  Username  in  lines:
            print "The  User %s  is  locked" % (Username)
            sys.exit()
 
    Password = raw_input('Please input you Password:')
    if len(Password) > 6:
        user_messages = file('user_messages.txt','rb')   #打开user_messages.txt 文件
        match_flag = False
        for line in user_messages.readlines():
            user, passwd  = line.strip(' ').split()      #去掉空格，以空格为分隔符分开账号密码
            if Username == user and Password == passwd:  #判断用户名密码是否正修改match_flag的值为true
                match_flag = True
                break
        if  match_flag == False:                       
                print 'User name or password Error'
                counts +=1
        else:
                print "####Wlcome  %s login####" % (Username)
                sys.exit()
        user_messages.close()
    else:
         counts +=1
         print "密码太短了"
else:
    print "The  User %s  is  locked" % (Username) #将输入密码错误三次的用户锁定
    rw_user_lockd = file('user_lockd.txt','ab')
    rw_user_lockd.write(Username)
    rw_user_lockd.write("\n")                     
    rw_user_lockd.close()
            
