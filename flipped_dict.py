'''
練習32

寫一個函式 flipped_dict(), 傳入一個 dict, 用生成式顛倒其 key 和 value 後傳回。

例如：

In :
{'a':1, 'b':2, 'c':3}

Out:
{1:'a', 2:'b', 3:'c'}

'''

def flipped_dict(input_dicts):

    return {value:key for key, value in input_dicts.items()}

print(flipped_dict({'a':1, 'b':2, 'c':3}))
