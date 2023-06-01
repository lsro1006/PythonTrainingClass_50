'''
練習 26 : 簡易前序式計算機

寫一個函式 prefix_cal(), 傳入比如 '+ 2 3' (算術符號 數字 數字) 這樣的字串。
其中各數字和符號之間以空格隔開, 並傳回計算結果。
這個函式得支援加減乘除計算。

心得筆記 :
1. operator 的 add, sub, mul and turediv 不只支援數字相加也包含字串相加
2. 後序式也是一樣的邏輯寫法

'''
import operator

calculator = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
    }

def prefix_cal(expression) :

    op, n1, n2 = expression.split()

    result = calculator[op](float(n1), float(n2))

    return result

print(prefix_cal('+ 10 7'))


'''
完整版的前序式計算機

In :
(2 + 4) * 3 / (1 + 5)

中序式轉換為前序式
In :
   (((2 + 4) * 3) / (1+5))
-> ((+ 2 4 * 3) / (1+5))
-> (* + 2 4 3) / (1+5))
-> (* + 2 4 3) / + 1 5)
-> / * + 2 4 3 + 1 5
'''

calculator = {
    '+': operator.add,
    '-': operator.sub,
    '*': operator.mul,
    '/': operator.truediv
    }

def isnumber(num): # 判斷是否為數字(整數 or 浮點數)
    # 如果傳進來的是浮點數, 因為小數點會被程式認為字串, 為避免誤判, 將小數點去掉
    return num.replace('.','').isnumeric()

def prefix_cal_pro(expression):
    
    item = expression.split()

    while len(item) > 1 :
        for i in range(len(item)- 2):
            op, n1, n2 = item[i:i+3]
            if op in calculator and isnumber(n1) and isnumber(n2):
                break
        item = item[:i] + [str(calculator[op](float(n1), float(n2)))] + item[i+3:]

    return float(item[0])

print(prefix_cal_pro('/ * + 2 4 3 + 1 5'))

        
