'''
練習 27

寫一個函式 set_password_source(), 指定要拿來產生密碼的來源字串,
它會傳回一個密碼產生器函式。
接著只要呼叫這個密碼產生器函式, 傳入長度參數就能產生特定長度的密碼。

In :
my_password_gen = set_password_source('0123456789abcdefghij')
print(my_password_gen(10))

Out :
fd3436c16e

'''

import random

def set_password_source(source):
    def password_gen(length):

        result_list = list()

        for i in range(length):
            result_list.append(random.choice(source))

        result = ''.join(result_list)
        return result
    return password_gen

my_password_gen = set_password_source('0123456789abcdefghij')
print(my_password_gen(10))
print(my_password_gen(12))
