'''
Question :
寫一個函式 passwd_to_dict(), 讀取 /etc/passwd(passwd.cfg).
函式會讀取所有使用者的帳號名稱和其ID, 並將之包成dict形式傳回

1. 用 print 印出
2. 用 pprint 印出 -> 要知道排序的'參數名稱是'什麼, 以及 True and False 的意義

For example :
jdoe:*:202:1:John Doe:/home/jdoe:/usr/bin/ksh
- User name
- Encrypted password
- User ID number (UID)
- User's group ID number (GID)
- Full name of the user (GECOS)
- User home directory
- Login shell

'''

import pprint

passwd_p = r"C:\Users\lsro1006\Desktop\python_prep\passwd_to_dict\passwd.cfg"

def passwd_to_dict(filename):

    user_dict = {}
    with open(filename, 'r') as f:
        for line in f:
            user_info = line.split(':')
            user_dict.update({user_info[0]:user_info[2]})
        return user_dict

print(passwd_to_dict(passwd_p))
print('----------\n')
pprint.pprint(passwd_to_dict(passwd_p), sort_dicts = False)

