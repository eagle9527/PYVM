#!/usr/bin/env python
#_*_ coding:utf-8 _*_
import  sys

def Usermessages(Username):                                  #判断用户是否锁定
    user_locked  = file('user_lockd.txt')
    for  lines in  user_locked.readlines():
	    if  Username  in  lines:
	        return 'locked'

def  Pwd(Username,Password):                                #判断用户名密码是否正确
    user_messages = file('user_messages.txt','rb')
    match_flag = False
    for line in user_messages.readlines():
        user, passwd  = line.strip(' ').split() 
        if Username == user and Password == passwd:
            match_flag = True
    return  match_flag

if __name__ == '__main__':
    counts =0
    while counts < 3:
        Username =  raw_input('Please input Username:')
    	Password =  raw_input('Please input Password:')
    	locked_msg = Usermessages(Username)
    	if locked_msg  == 'locked':                         #如果调用函数返回locked 说明用户被锁定，打印消息并退出
    	    print "The  User %s  is  locked" % (Username)
            sys.exit()
        if len(Password) < 6:                               #如果用户输入密码小于6个字符，打印消息，并记录次数
            print "Password  so Short"
            counts += 1
            
        else:
            if  Pwd(Username, Password) != True:            #调用函数，判断用户名密码是否正确，如果错误记录次数
                counts += 1
                print 'User name or password Error'
            else:
                print "####Wlcome  %s login####" % (Username) # 正确就返回欢迎信息
                sys.exit()

    else:
        print "The  User %s  is  locked" % (Username)       #将输入密码错误三次的用户锁定
        rw_user_lockd = file('user_lockd.txt','ab')
        rw_user_lockd.write(Username)
        rw_user_lockd.write("\n")                     
        rw_user_lockd.close()
	
