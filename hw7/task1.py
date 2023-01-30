# Второй этап. Необходимо написать функцию is_valid_password,
# которая будет проверять полученный параметр — пароль на надежность.
#
# Критерии надежного пароля:
#
# 1 Длина строки пароля восемь символов.
# 2 Содержит хотя бы одну букву в верхнем регистре. (можна створити змінну наприклад has_upper)
# далі бігати по символах в строці і поставити умову if 'A' <= i <= 'Z': has_upper = True
# схоже прописати до 3, 4 пунктів
# 3 Содержит хотя бы одну букву в нижнем регистре.
# 4 Содержит хотя бы одну цифру.
# Функция is_valid_password должна вернуть True, если переданный в качестве параметра пароль
# отвечает требованиям надежности. В противном случае вернуть False.

def is_valid_password(yourpass: str):
    has_upper = False
    has_lower = False
    has_num = False
    for i in yourpass:
        if 'A' <= i <= 'Z':
            has_upper = True
        elif 'a' <= i <= 'z':
            has_lower = True
        elif '0' <= i <= '9':
            has_num = True
    if len(yourpass) == 8 and has_lower and has_upper and has_num:
        return True
    return False

password = "567uponU"
print(is_valid_password(password))

