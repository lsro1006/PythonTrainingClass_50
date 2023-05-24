'''
練習 22 : 讀寫 CSV 檔
寫一個函式 passwd_to_csv(), 傳入兩個檔名。
函式會讀取第一個 CSV 格式檔案內的帳號與 ID 資訊, 並改用 Tab 當成資料分隔符號,
寫入第二個 CSV 檔案。

暖身觀念 :
1. 讀 CSV 檔 : csv.reader 真正作用是是把每一個字串用指定的 delimiter ''拆解''成一個 list
2. 寫 CSV 檔 : csv.writer 真正作用是把每一個 list(或是 csv.reader 產生的), 用指定的 delimiter 和 lineterminator ''串接''回一個一個字串
3. Python 開檔案欲寫入資料時, 可多加一個參數 newline 並指定為空值 newline = ''
   由於不同 OS 的換行符號皆不同, 為避免解析符號時混淆, 空值表示開檔欲寫入時以'檔案本身原本的換行符號'來解析
   
4. writerow() 吃的參數要注意是 list, 若只是要寫入 list 的某幾個參數, 記得還是要用中括號 [] 括起來

'''
import os
import csv

current_p = os.getcwd()
read_file_p = os.path.join(current_p, 'passwd.cfg')
write_file_p = os.path.join(current_p, 'passwd.csv')


def passwd_to_csv(filename1, filename2):

    with open(filename1, 'r') as f_read, open(filename2, 'w', newline='') as f_write:

        csv_reader = csv.reader(f_read, delimiter = ':')
        csv_writer = csv.writer(f_write, delimiter = '\t', lineterminator = '\n')

        for line in csv_reader:
            csv_writer.writerow([ line[0], line[2] ])
            

passwd_to_csv(read_file_p, write_file_p)



