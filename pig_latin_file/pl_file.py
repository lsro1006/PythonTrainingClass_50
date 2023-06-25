'''
練習31

寫一個函式 pl_file(), 傳入一個檔名, 以生成式將該文字檔的內容(每一行的每一個字)
轉成豬拉丁文後, 以一個字串形式傳回。這裡假設文字檔中只有英數和空白,
沒有標點符號等字元。


例如沿用第 5 章的文字檔 text2.txt :

In :
Beautiful is better than ugly.
Explicit is better than implicit.
Simple is better than complex.
Complex is better than complicated.
Flat is better than nested.
Sparse is better than dense.
Readability counts.

Out :
eautifulbay isway etterbay hantay uglyway explicitway isway
etterbay hantay implicitway implesay isway etterbay hantay
omplexcay omplexcay isway etterbay hantay omplicatedcay latfay
isway etterbay hantay estednay parsesay isway etterbay hantay
enseday eadabilityray ountscay

'''
import os


current_p = os.getcwd()
file_p = os.path.join(current_p, 'text2.txt')

def pig_latin(word) :

    # Both list and string work
    #vowels = ['a', 'e', 'i', 'o', 'u']
    vowels = 'aeiou'

    if word[0] in vowels :
        return f'{word}way'
    else:
        return f'{word[1:]}{word[0]}ay'


def pl_file(filename):
    mylist = list()
    with open(filename, 'r') as f:
        for line in f :
            for word in line.split() :
                mylist.append(pig_latin(word.lower().replace('.','')))
    results = ' ' .join(mylist)
    return results

def pl_file_comprehension(filename):

    with open(filename, 'r') as f:
        return ' '.join([pig_latin(word.lower().replace('.',''))
                for line in f
                    for word in line.split()])


print(pl_file(file_p))
print('\n')
print(pl_file_comprehension(file_p))
