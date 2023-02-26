# В компании существует несколько отделов. Список сотрудников для каждого отдела
# имеет такой вид:
#
# ['Robert Stivenson,28', 'Alex Denver,30']
# Это список строк с фамилией и возрастом сотрудника, разделенными запятыми.

# Реализуйте функцию записи данных о сотрудниках компании в файл, чтобы информация о
# каждом сотруднике начиналась с новой строки.

# Функция записи в файл write_employees_to_file(employee_list, path), где:

# path - путь к файлу.
# employee_list - список со списками сотрудников по каждому отделу, как в примере ниже:
# [['Robert Stivenson,28', 'Alex Denver,30'], ['Drake Mikelsson,19']]
# Требования:

# запишите содержимое employee_list в файл, используя режим "w".
# мы пока не используем менеджер контекста with
# каждый сотрудник должен быть записан с новой строки — т.е для предыдущего
# списка содержимое файла должно быть следующим:
# Robert Stivenson,28
# Alex Denver,30
# Drake Mikelsson,19

from pathlib import Path
def write_employees_to_file(employee_list, path):
    file = open(path, 'w+', encoding='utf-8')
    for section in employee_list:
        for employee in section:
          file.write(f'{employee}\n')
    file.close()

list_ = [['Mariam Loving,46', 'Peter Parker,27'],['Andy Lane,35']]
pth = Path("text_file.txt")
if __name__ == "__main__":
    write_employees_to_file(list_, pth)
