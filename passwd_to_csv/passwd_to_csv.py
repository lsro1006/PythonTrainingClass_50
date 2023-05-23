'''
練習 22 : 讀寫 CSV 檔
寫一個函式 passwd_to_csv(), 傳入兩個檔名。
函式會讀取第一個 CSV 格式檔案內的帳號與 ID 資訊, 並改用 Tab 當成資料分隔符號,
寫入第二個 CSV 檔案。

暖身觀念 :
1. 讀 CSV 檔
2. 寫 CSV 檔

用觀念 1 and 2 寫出本題。

'''
import os
import csv

current_p = os.getcwd()
file_p = os.path.join(current_p, 'passwd.cfg')

def passwd_to_csv(filename):

    with open(filename, 'r') as f_read:


        csv_reader = csv.reader(f_read, delimiter=':')
        #csv_writer = csv.writer(f_write, delimiter='\t', lineterminator='\n')

        for line in csv_reader:
            print(line)

passwd_to_csv(file_p)
        

