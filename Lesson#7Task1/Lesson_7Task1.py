﻿word = str(input("Введите слово: ").lower())
if word == word[::-1]:
    print("Yes")
else:
    print("No")
