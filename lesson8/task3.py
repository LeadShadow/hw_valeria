# Вернемся к нашей задаче с телефонными номерами. Компания расширяется и вышла на рынок Азии.
# Теперь в списке приходят телефоны разных стран. Каждая страна имеет свой телефонный код .
#
# Компания работает со следующими странами
# +43438272348
# Страна	Код ISO	Префикс
# Japan	      JP	+81
# Singapore	  SG	+65
# Taiwan	  TW	+886
# Ukraine	  UA	+380
# Чтобы мы могли корректно выполнить маркетинговую SMS кампанию, необходимо выдать для каждой
# страны свой список телефонных номеров.
#
# Напишите функцию get_phone_numbers_for_сountries, которая будет:
#
# Принимать список телефонных номеров.
# Санитизировать (нормализовать) полученный список телефонов клиентов с помощью нашей функции
# sanitize_phone_number.
# Сортировать телефонные номера по указанным в таблице странам.
# Возвращать словарь со списками телефонных номеров для каждой страны в следующем виде:
# {
#     "UA": [<здесь список телефонов>],
#     "JP": [<здесь список телефонов>],
#     "TW": [<здесь список телефонов>],
#     "SG": [<здесь список телефонов>]
# }
# Если не удалось сопоставить код телефона с известными, этот телефон должен быть добавлен в список
# словаря с ключом "UA".

#
def sanitize_phone_number(phone):
    new_phone = (
        phone.strip()
        .removeprefix("+")
        .replace("(", "")
        .replace(")", "")
        .replace("-", "")
        .replace(" ", "")
    )
    return new_phone


def get_phone_numbers_for_countries(list_phones: list):
    list1 = []
    list2 = []
    list3 = []
    list4 = []
    for phone in list_phones:
        phone = sanitize_phone_number(phone)
        if phone.startswith('81'):
            list1.append(phone)
            continue
        elif phone.startswith('65'):
            list2.append(phone)
            continue
        elif phone.startswith('886'):
            list3.append(phone)
            continue
        else:
            list4.append(phone)
            continue
    return {'JP': list1, "SG": list2, "TW": list3, "UA": list4}


if __name__ == "__main__":
    print(get_phone_numbers_for_countries(['+380937316048', '+435875844589', '+654234232', '8865834753453']))
