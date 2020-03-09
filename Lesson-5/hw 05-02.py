# Author Aponasevich Ivan
# Задание 2
#
# Создать текстовый файл (не программно), сохранить в нем несколько строк,
# выполнить подсчет количества строк, количества слов в каждой строке.


my_list = {"Привет!\n", "Я текстовый файл для второго задания.\n"}
# записываем лист в файл
with open("TextFile for hw 05-02.txt", "w") as My_File:
    My_File.writelines(my_list)

# вывести содержимое файла
with open("TextFile for hw 05-02.txt", "r") as My_File:
    content = My_File.read()
    print(f'Содержимое файла:\n{content}')

# показать сколько строк
with open("TextFile for hw 05-02.txt", "r") as My_File:
    content = My_File.readlines()
    print(f'Строк в файле: {len(content)}')

# показать сколько символов в каждой строке (с \n и пробелами)
with open("TextFile for hw 05-02.txt", "r") as My_File:
    content = My_File.readlines()
    for line in range(len(content)):
        print(f'В {line + 1} строке: {len(content[line])} символов.')

# показать сколько слов в файле
with open("TextFile for hw 05-02.txt", "r") as My_File:
    content = My_File.read()
    content = content.split()
    print(f'Всего слов в файле: {len(content)}')
