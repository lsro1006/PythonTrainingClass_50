'''
練習 26 : 簡易前序式計算機

寫一個函式 prefix_cal(), 傳入比如 '+ 2 3' (算術符號 數字 數字) 這樣的字串。
其中各數字和符號之間以空格隔開, 並傳回計算結果。
這個函式得支援加減乘除計算。

心得筆記 :
operator 的 add, sub, mul and turediv 不只支援數字相加也包含字串相加

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
