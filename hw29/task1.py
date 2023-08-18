# Задача: Аналіз даних з CSV файлу
#
# У вас є CSV файл з даними про різних студентів у форматі:
#
# Ім'я, Вік, Середній_бал
# Анна, 21, 8.5
# Петро, 20, 7.2
# Марія, 22, 9.0
# Іван, 19, 6.8
# ...
# Це початкова структура файлу csv, який потрібно створити і наповнити данними(бажано через пайтон)
# Задача:
#
# Завантажте дані з CSV файлу та збережіть їх у зручній для роботи структурі даних.
# Обчисліть середній вік студентів.
# Знайдіть студента з найвищим середнім балом та виведіть його ім'я і бал.
# Порахуйте кількість студентів, які молодші за 20 років.
# Створіть новий CSV файл, в який запишете імена студентів, вік та середній бал, але
# відсортовані за спаданням середнього балу.

# ps: можна використовувати загальний клас(методи класу), наслідування(якщо потрібно), а також функ
# ціональний підхід(пам'ятай кожен крок це функція нова, 1 функція відповідає за одну дію))


import csv


with open('students_info.csv', 'w', newline='') as file:
    fields_names = ["Ім'я", 'Вік', 'Середній бал']
    writer = csv.DictWriter(file, fieldnames=fields_names)
    writer.writeheader()
    writer.writerow({"Ім'я": 'Анна', 'Вік': '21', 'Середній бал': '8.5'})
    writer.writerow({"Ім'я": 'Петро', 'Вік': '20', 'Середній бал': '7.2'})
    writer.writerow({"Ім'я": 'Марія', 'Вік': '22', 'Середній бал': '9.0'})
    writer.writerow({"Ім'я": 'Іван', 'Вік': '19', 'Середній бал': '6.8'})

# Завантаження даних з CSV файлу
data = []
with open('students_info.csv', 'r') as file:
    reader = csv.reader(file)
    next(reader)  # Пропустити заголовок
    for row in reader:
        name, age, score = row
        data.append({
            'name': name,
            'age': int(age),
            'score': float(score)
        })

# Обчислення середнього віку
total_age = sum(student['age'] for student in data)
average_age = total_age / len(data)

print(f"Середній вік студентів: {average_age} років")
# Знаходження студента з найвищим балом
best_student = max(data, key=lambda student: student['score'])
print(f"Студент з найвищим балом: {best_student['name']}, Бал: {best_student['score']}")

# Порахувати кількість студентів молодших за 20 років
young_students = sum(1 for student in data if student['age'] < 20)
print(f"Кількість студентів молодших за 20 років: {young_students}")

# Сортування та запис в новий CSV файл
sorted_data = sorted(data, key=lambda student: student['score'], reverse=True)

with open('sorted_students.csv', 'w', newline='') as file:
    writer = csv.writer(file)
    writer.writerow(['Ім\'я', 'Вік', 'Середній_бал'])
    for student in sorted_data:
        writer.writerow([student['name'], student['age'], student['score']])

print("Дані відсортовано та записано у файл 'sorted_students.csv'")


