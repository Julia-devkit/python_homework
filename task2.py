with open('file_for_task_2', encoding='utf-8') as poem:
    lst = poem.readlines()
    num_of_lines = len(lst)
    for i, j in enumerate(lst, 1):
        print(f'Строка {i}:  "{j.strip()}",  количество слов: {len(j.split())}')



