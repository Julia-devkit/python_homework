with open(r'C:\Users\panty\PycharmProjects\untitled1\lesson5_filse\python_homework\file_for_task_6txt', encoding='utf-8') as fl:
    lst = fl.readlines()
    sum_hours = []
    name_for_dicipline = []
for i in range(len(lst)):
    lst[i] = lst[i].split()
    hours = []
    name_for_dicipline.append(lst[i][0])
    for j in range(len(lst[i])):
        lst[i][j] = lst[i][j].split('(')
        for x in lst[i][j]:
            if x.isdigit():
                hours.append(int(x))
    sum_hours.append(sum(hours))
print(dict(zip(name_for_dicipline, sum_hours)))



