'''
練習 28

寫一個函式 abs_numbers(), 接收一個參數 (包含一系列數字的容器),
並在函式中以生成式 (comprehension) 傳回一個容器,
內容為所有元素的絕對值。

In :
print(abs_numbers([1, -2, 3, -4, 5]))

Out :
[1, 2, 3, 4, 5]

'''

def abs_numbers(nums) :

    return [abs(i) for i in nums]

print(abs_numbers([1, -2, 3, -4, 5]))


def abs_numbers_map(nums):
    # map() : 高階函式 -> 參數或回傳值為函式的函式
    return list(map(abs, nums))

print(abs_numbers_map([1, -2, 3, -4, 5]))
