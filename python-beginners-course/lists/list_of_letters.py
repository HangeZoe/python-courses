# На вход программе подается одно число n.
# Напишите программу, которая выводит список,
# состоящий из n букв английского алфавита
# ['a', 'b', 'c', ...] в нижнем регистре.

num = int(input())
letters = list(range(97, 97 + num))
for i in range(num):
    letters[i] = chr(letters[i])
print(letters)
