'''
寫一個函式 wordcount(), 此函式會印出該文字檔的
1. 字元數
2. 單字數
3. 不重複單字數
4. 行數

在此假設內文只用英文和數字組成。
'''


file_p = r"C:\Users\lsro1006\Desktop\python_prep\wordcount\test.txt"

results = {
    'chars' : 0,
    'words' : 0,
    'uniq_words' : 0,
    'lines' : 0
    }

uniq_set = set()


def wordcount(filename) :

    with open(filename, 'r') as f :
        for line in f:
            word_list = line.split()
            results['chars'] += len(line)
            results['words'] += len(word_list)
            results['lines'] += 1
            uniq_set.update(word_list)

        results['uniq_words'] = len(uniq_set)

    for key, value in results.items():
        print(f'{key}:{value}')

wordcount(file_p)


            
            
