'''
練習30

寫一個函式 flatten(), 用生成式 comprehension 將二維list 轉換成一維

例如 :

In :
[[1, 2], [3, 4]]


Out :
[1, 2, 3, 4]

'''

input_patten = [[1, 2], [3, 4]]

def flatten_forloop(inputs):

    mylist = list()
    for x in inputs:
        for y in x :
            mylist.append(y)

    return mylist

def flatten_comprehension(inputs):

    return [y for x in inputs
                for y in x]

print(flatten_forloop(input_patten))

print(flatten_comprehension(input_patten))
