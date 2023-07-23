# Завдання: Розробка контекстного менеджера
# Опис: Створіть контекстний менеджер Timer, який дозволяє виміряти час виконання
# певного блоку коду. Використайте магічні методи __enter__ та __exit__ для реалізації
# контекстного менеджера. При вході в блок коду with Timer() as t:, таймер починає
# відлік часу, а при виході з блоку коду відображається час виконання.
import time
import math


class Timer:
    def __enter__(self):
        start = time.time()
        print('Stopwatch started <3')
        while True:
            command = input("Print 'stop' if you want to stop the stopwatch.\n")
            if command == "stop":
                end = time.time()
                time_ = end - start
                print(f'{math.trunc(time_)} seconds.')
                return self
            else:
                print("Command isn't familiar.")

    def __exit__(self, exc_type, exc_val, exc_tb):
        print('Goodbye!')


with Timer() as t:
    print('Thanks for using our stopwatch <3')
