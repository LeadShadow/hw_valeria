# є випадковий список, потрібно представити його в зворотньому напрямку 
# [1, 3, 5] -> [5, 3, 1]


def reverse_list(my_list: list) -> list:
    my_list.reverse()
    return my_list


print(reverse_list([1, 3, 5]))
