import random

chars = "+-*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"
password = ''
length = int(input("Какая длинна пароля? "))
for i in range(length):
    password += random.choice(chars)



print(password)