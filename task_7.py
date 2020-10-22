import json
with open(r'C:\Users\panty\PycharmProjects\untitled1\lesson5_filse\python_homework\file_for_task_7.txt', encoding='utf-8') as file:
  file = file.readlines()
names, profit = [], []
for i in file:
    i = i.split()
    names.append(i[0])
    profit.append(int(i[2]) - int(i[3]))
dict(zip(names, profit))
my_sum = 0
num = 0
for i in profit:
    if i > 0:
        my_sum +=i
        num += 1
average_profit = my_sum/num
data = [dict(zip(names, profit)), {'average_profit': average_profit}]
with open('file_for_task_7.json', 'w') as file_j:
    json.dump(data, file_j)