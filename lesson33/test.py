import csv
import pickle
import copy


with open('eggs.csv', 'w', newline='') as file:
    spam_writer = csv.writer(file)
    spam_writer.writerow(['Spam'] * 5 + ['Baked Beans'])
    spam_writer.writerow(['Spam', 'Lovely Spam', 'Wonderful Spam'])

with open('eggs.csv', newline='') as file:
    spam_reader = csv.reader(file, delimiter=',')
    for row in spam_reader:
        print(', '.join(row))


with open('names.csv', 'w', newline='') as file:
    fields_names = ['first_name', 'last_name']
    writer = csv.DictWriter(file, fieldnames=fields_names)
    writer.writeheader()
    writer.writerow({'first_name': 'Baked', 'last_name': 'Beans'})
    writer.writerow({'first_name': 'Sasha', 'last_name': 'Samus'})
    writer.writerow({'first_name': 'Valeria', 'last_name': 'Ariaieva'})


with open('names.csv', 'r', newline='') as file:
    reader = csv.DictReader(file)
    for row in reader:
        print(row)


class Reader:
    def __init__(self, file):
        self.file = file
        self.fh = open(self.file)
        self.position = 0

    def close(self):
        self.fh.close()

    def read(self, size=1):
        data = self.fh.read(size)
        self.position = self.fh.tell()
        return data

    def __getstate__(self):
        attributes = self.__dict__.copy()
        attributes['fh'] = None
        return attributes

    def __setstate__(self, value):
        self.__dict__ = value
        self.fh = open(value['file'])
        self.fh.seek(value['position'])


reader = Reader('test.bin')
reader.read()
reader.close()

# with open(reader.file, 'rb') as file:
#     unpacked = pickle.load(file)


my_list = [1, 2, 3]
copy_list = my_list
copy_list.append(4)
print(id(my_list))
print(id(copy_list))


my_list = [1, 2, 3]
copy_list = my_list[:]
copy_list.append(4)
print(my_list)

d = {1: 'a'}
d_copy = {**d}
d_copy[2] = 'b'
print(d)
print(d_copy)

my_list = [1, 2, {1: 'a'}]
copy_list = copy.copy(my_list)
copy_list.append(4)
print(my_list)
print(copy_list)

copy_list[2][2] = 'b'
print(my_list)
print(id(my_list[2]))
print(id(copy_list[2]))


my_list = [1, 2, {1: 'a'}]
copy_list = copy.deepcopy(my_list)
copy_list.append(4)
print(my_list)
print(copy_list)

copy_list[2][2] = 'b'
print(my_list)


class Expenses:
    def __init__(self):
        self.data = {}
        self.places = []

    def spent(self, place, value):
        self.data[str(place)] = value
        self.places.append(place)

    def __copy__(self):
        copy_obj = Expenses()
        copy_obj.data = self.data
        copy_obj.places = self.places
        return copy_obj

    def __deepcopy__(self, memo):
        copy_obj = Expenses()
        memo[id(copy_obj)] = copy_obj
        copy_obj.data = copy.deepcopy(self.data)
        copy_obj.places = copy.deepcopy(self.places)
        return copy_obj


e = Expenses()
e.spent('hotel', 1000)
e.spent('taxi', 150)
print(e.places)

e_copy = copy.copy(e)
print(e_copy is e)
e_copy.spent('bar', 500)
print(e.places)

e_deep_copy = copy.deepcopy(e)
print(e_deep_copy is e)
e_deep_copy.spent('airport', 5000)
print(e.places)
print(e_deep_copy.places)
