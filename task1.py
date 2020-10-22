with open('file_for_task_1.txt', 'w', encoding='utf-8') as file:
    while True:
        content = input()
        text = file.write(content + '\n')
        if content == '':
            break
file = open('file_for_task_1.txt')
content = file.read()
print(content)


