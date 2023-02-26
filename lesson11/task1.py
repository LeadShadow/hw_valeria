# Приклад 1
# Наступна програма зчитує весь вміст файлу input.txt, записує його в змінну s,
# а потім виводить її в файл output.txt.
# Нехай в файл input.txt записано We are learning Python programming language

file1 = open('input.txt', 'r')
file2 = open('output.txt', 'w')
s = file1.read()
file2.write(s)
file1.close()
file2.close()
