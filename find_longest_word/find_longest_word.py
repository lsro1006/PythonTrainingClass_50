'''
寫一個函式 find_longest_word(), 傳入一個檔名, 它會傳回該文字檔中最長的單字。
請注意 : 句點不能算是單字的一部分。

1. 用 空字串 當起始最長的單字
2. 用 set 來排序
'''

import os

current_p = os.getcwd()
file_p = os.path.join(current_p, 'test.txt')


def find_longest_word_empty_string(filename) :

    longest = ''

    with open(filename, 'r') as f :

        for line in f :
            clean_line = line.replace('.', '').split()
            for word in clean_line:
                if len(word) > len(longest):
                    longest = word

        return longest


def find_longest_word_set(filename) :

    set_all = set()

    with open(filename, 'r') as f :
        for line in f:
            clean_line = line.replace('.','').split()
            set_all.update(clean_line)

    return sorted(set_all, key=len)[-1]
                


#print(find_longest_word_empty_string(file_p))
        
print(find_longest_word_set(file_p))
