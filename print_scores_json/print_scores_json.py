'''
練習 23

寫一個函式, print_scores_json(), 會讀取 JSON 格式的成績檔,　
統計各科的最高分, 最低分 和 平均並印出

能輸出以下的統計結果:

班級: 9a
科目: math
  最高分: 100
  最低分: 65
  平均: 85.0
科目: literature
  最高分: 98
  最低分: 78
  平均: 83.6
科目: science
  最高分: 97
  最低分: 75
  平均: 86.4 

心得 :
1.
2.
3.

'''
import os
import json
from collections import defaultdict

current_p = os.getcwd()
file_p = os.path.join(current_p, 'score.json')

def print_scores_json(filename):

    with open(filename, 'r') as f_json:

        dict_results = json.load(f_json)
        results = defaultdict(list)

        print("班級: ", dict_results['class'])

        for record in dict_results['score']:
            for subject, score in record.items():
                results[subject].append(score)
        print(results)

        for key, value in results.items():
            print("科目: ", key)
            print('\t最高分: ', max(value))
            print('\t最低分: ', min(value))
            print('\t平均: ', sum(value)/len(value))

print_scores_json(file_p)
        
