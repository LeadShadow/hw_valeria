import sqlite3


class DataBase:
    connect = sqlite3.connect('example.db')
    def __enter__(self):
        print(f'connected to database')
        return self.connect

    def __exit__(self, exc_type, exc_val, exc_tb):
        if exc_type is not None:
            print('Some Error!')
        else:
            print('GoodBye!')
            self.connect.close()

# Встановлюємо з'єднання з базою даних і використовуємо менеджер контекста
db = DataBase()
with db as connection:
    # Створюємо курсор для виконання SQL-запитів
    cursor = connection.cursor()

    # Виконуємо SQL-запит для створення таблиці
    cursor.execute('''CREATE TABLE IF NOT EXISTS users
                          (id INTEGER PRIMARY KEY AUTOINCREMENT,
                           name TEXT,
                           age INTEGER)''')

    # Виконуємо SQL-запит для вставки даних
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('John Doe', 25))
    cursor.execute("INSERT INTO users (name, age) VALUES (?, ?)", ('Jane Smith', 30))

    # Зберігаємо зміни у базі даних
    connection.commit()

    # Виконуємо SQL-запит для вибірки даних
    cursor.execute("SELECT * FROM users")
    rows = cursor.fetchall()

    # Виводимо результати вибірки
    for row in rows:
        print(row)


# 4, 5, 5, 5, 5 -> 4.8
# 4, 5, 5, 3, 5 -> 4.4
# 4, 2, 5, 5, 5 -> 4.2
# 13.4 / 3 -> 4.47