'''
練習29

寫一個函式 sum_numbers(), 傳入一個字串 (當中各筆資料用空格分開)。
以生成式過濾出字串中的整數, 並傳回其總和。

In :
10 abc 20 de44 30 55fg 40

若將這個字串傳給 sum_numbers(), 就會得到 10 + 20 + 30 + 40 = 100
(de44 和 55fg 會被略過)

'''

def sum_numbers(inputs) :

    results = [int(i)
               for i in inputs.split()
               if i.isdigit()]
    return sum(results)

print(sum_numbers("10 abc 20 de44 30 55fg 40"))


def sum_numbers_filter(inputs):

    results = list(map(int, filter(lambda d : d.isdigit(), inputs.split())))
    return sum(results)

print(sum_numbers_filter("10 abc 20 de44 30 55fg 40"))
