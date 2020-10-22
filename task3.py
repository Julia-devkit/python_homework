with open('file_for_task_3.txt', encoding='utf-8') as low_salary:
    lst = low_salary.readlines()
    print('У следующих сотрудников зарплата ниже 20 000 руб:')
    salarys = []
    for i in lst:
        pare = i.split()
        salarys.append(float(pare[1]))
        if float(pare[1]) < 20000:
            print(pare[0], end=', ')
    print()
print(f'cредняя зарплата на каждого сотрудника составляет {sum(salarys) / len(lst)}. ')

