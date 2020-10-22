with open('file_for_task_5.txt', 'w', encoding='utf-8') as file:
    my_str = input('Введите числа через пробел: ')
    file.write(my_str)
my_sum = 0
for i in my_str.split():
    my_sum = my_sum + int(i)
print(my_sum)


