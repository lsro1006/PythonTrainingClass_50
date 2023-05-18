'''
 Question :
 寫一個函式 read_final_line(), 傳入文字檔的路徑與檔名,
 然後傳回該檔案中的最後一行文字

 1. 用 readlines 寫
 2. 用 readline 寫
 3. 用 with.. open.. 寫
'''
import os

current_p = os.getcwd()
file_p = os.path.join(current_p, 'logs.log')

# readlines
def read_final_line_readlines(filename) :

    try :
        f = open(filename)
        lastline = f.readlines()[-1]
        return lastline
    finally :
        f.close()


# readline
# 使用readline就不能使用for line in readline()了, 因為readline()只會列出一行
def read_final_line_readline(filename):
    try:
        f = open(filename)
        while True:
            line = f.readline()
            if not line:
                break
            lastline = line
        return lastline
    finally:
        f.close


# with.. open..
def read_final_line_with_open(filename):
    with open(filename, 'r') as f:
        for line in f:
            pass
        return line


#print(read_final_line_realines(file_p))
#print(read_final_line_readline(file_p))
print(read_final_line_with_open(file_p))    
