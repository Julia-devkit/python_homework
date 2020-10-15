with open('file_for_task_4.txt',encoding='utf-8') as file:
    lines = file.readlines()
nums = ['один', 'два', 'три', 'четыре']
with open('new_file_for_task_4','w', encoding='utf-8') as new_file:
    for i, j in enumerate(lines):
        j = j.replace(j.split()[0], nums[i])
        new_file.write(j)












#str_list = ['stroka_1\n', 'stroka_2\n', 'stroka_3\n']
#out_f.writelines(str_list)
