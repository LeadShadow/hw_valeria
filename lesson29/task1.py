# Завдання: Перевантаження індексації
# Опис: Розробіть клас Matrix, який представляє матрицю. Використайте магічний метод __getitem__
# для перевантаження індексації, щоб дозволити отримувати значення елементів матриці за допомогою
# квадратних дужок. При цьому індекси починаються з 1, а не з 0.


class Matrix:
    def __init__(self, rows, columns):
        self.rows = rows
        self.columns = columns
        self.data = [[0] * columns for _ in range(rows)]

    def __getitem__(self, item):
        row, column = item
        return self.data[row - 1][column - 1]

    def __setitem__(self, key, value):
        row, column = key
        self.data[row - 1][column - 1] = value


matrix = Matrix(3, 3)
matrix[1, 1] = 1
matrix[2, 2] = 2
matrix[3, 3] = 3

print(matrix[1, 1])
print(matrix[2, 2])
print(matrix[3, 3])