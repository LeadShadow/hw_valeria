# Наш ассистент уже умеет взаимодействовать с пользователем посредством командной строки,
# получая команды и аргументы и выполняя нужные действия. В этом задании нужно будет поработать
# над внутренней логикой ассистента, над тем, как хранятся данные, какие именно данные и что с ними
# можно сделать.
#
# Применим для этих целей объектно-ориентированное программирование. Для начала выделим несколько
# сущностей (моделей) с которыми будем работать.
#
# У пользователя будет адресная книга или книга контактов. Эта книга контактов содержит записи.
# Каждая запись содержит некоторый набор полей.
#
# Таким образом мы описали сущности (классы), которые необходимо реализовать. Далее рассмотрим
# требования к этим классам и установим их взаимосвязь, правила, по которым они будут взаимодействовать.
#
# Пользователь взаимодействует с книгой контактов, добавляя, удаляя и редактируя записи. Также
# пользователь должен иметь возможность искать в книге контактов записи по одному или нескольким
# критериям (полям).
#
# Про поля также можно сказать, что они могут быть обязательными (имя) и необязательными (телефон или
# email например). Также записи могут содержать несколько полей одного типа (несколько телефонов например).
# Пользователь должен иметь возможность добавлять/удалять/редактировать поля в любой записи.
#
# В этой домашней работе вы должны реализовать такие классы:
#
# Класс AddressBook, который наследуется от UserDict, и мы потом добавим логику поиска по записям в этот класс.
# Класс Record, который отвечает за логику добавления/удаления/редактирования необязательных полей и
# хранения обязательного поля Name.
# Класс Field, который будет родительским для всех полей, в нем потом реализуем логику общую для всех полей.
# Класс Name, обязательное поле с именем.
# Класс Phone, необязательное поле с телефоном и таких одна запись (Record) может содержать несколько.
# Критерии приёма
# Реализованы все классы из задания.
# Записи Record в AddressBook хранятся как значения в словаре. В качестве ключей используется значение
# Record.name.value.
# Record хранит объект Name в отдельном атрибуте.
# Record хранит список объектов Phone в отдельном атрибуте.
# Record реализует методы для добавления/удаления/редактирования объектов Phone.
# AddressBook реализует метод add_record, который добавляет Record в self.data.
from __future__ import annotations

from collections import UserDict
import re

class Field:
    def __init__(self, value) -> None:
        self.value = value

    def __str__(self) -> str:
        return f'{self.value}'


class Name(Field):
    pass


class Phone(Field):
    pass


class Record:
    def __init__(self, name: Name, phones: list|Phone = []) -> None:
        self.name = name
        self.phone_list = phones

    def __str__(self) -> str:
        return f'User {self.name.value} - Phones: {", ".join([phone for phone in self.phone_list])}'

def hello(*args):
    return 'Hello! How can I help you?'


# add Sasha +380937316048 -> add Sasha
def add_contact(contacts, *args):
    name, phone = args[0], args[1]
    phone = verify_phone(phone)
    contacts[name] = phone
    return f'Added user {name}'


def change_contact(contacts, *args):
    name, phone = args[0], args[1]
    contacts[name] = verify_phone(phone)
    return f'Change user {name}'


def show_phone(contacts, *args):
    name = args[0]
    return f'User - {name}, phone - {contacts[name]}'


def show_all(contacts, *args):
    result = 'List of all users: '
    for name, phone in contacts.items():
        result += '\n|User - {:^10}| phone - {:^15}|'.format(name, phone)
    return result

def goodbye(*args):
    return None


def help_me(*args):
    return """Command format:
help or ? - help
hello - func of greeting
add <name> <phone> - add user to dict
change <name> <phone> - change the user's phone number
phone <name> - show the user's phone number
show all - show all contacts
close or . or exit or stop - exit the program"""


def verify_phone(phone: str) -> str:
    new_phone = re.sub(r'\+|\(|\)|-| |[a-zA-Zа-яА-Я]', '', phone)
    return new_phone


COMMANDS = {'hello': hello, 'add': add_contact, 'change': change_contact, 'phone': show_phone,
            'show all': show_all, 'exit': goodbye, 'close': goodbye, '.': goodbye, 'stop': goodbye,
            'help': help_me, '?': help_me}


def main():
    contacts = {}
    while True:
        user_command = input('Enter command: ')
        for key in COMMANDS.keys():
            if user_command.lower().startswith(key):
                args = user_command[len(key):].split()
                result = COMMANDS.get(key)(contacts, *args)
                if result is None:
                    print('Good Bye!')
                    exit(0)
                print(result, '\n')
                break
        else:
            print('Unknown command! Enter again!')


if __name__ == "__main__":
    main()