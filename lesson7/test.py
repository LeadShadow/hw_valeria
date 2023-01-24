s = 'hello world'
print(s[0])
# s[0] = 'q'
s1 = s.upper()
print(s1)
s2 = s1.lower()
print(s2)

s = 'Sasha Samus'
print(s.startswith('sa'))
s1 = 'hello.svg'
print(s1.endswith('.png'))
if s1.endswith('.png') or s1.endswith('.svg'):
    print('Це фотографія!')


password = 'qwfnghd123'
if 'qwerty' in password or '123' in password:
    print('This password is to weak!')

numbers = [2, 3, 5]
in_3_num = 3 in numbers
print(in_3_num)

user = {
    'name': 'Oleksandr',
    'surname': 'Samus',
    'age': 18
}
if 'age' in user:
    print(f'User is {user["age"]} years old.')

password = input('Password: ')
if len(password) < 8:
    print('Your password is too short!')