#!/usr/bin/env python
# coding: utf-8

def code(word, n):
    storage = [x for x in word]
    storage2 = []
    for i in storage:
        if i == " ":
            storage2.append(i)
        elif i.isupper():
            storage2.append(chr((ord(i) + n - 65) % 26 +65))
        elif i.islower():
            storage2.append(chr((ord(i) + n - 97) % 26 + 97))
        else:
            storage2.append(i)
    return print("Your secret message is: " + ''.join(storage2))
z = "S"
while z == "S":
    print("Welcome to the Cryptography program.")
    print("You can input a message and a number less than 26, and this program will generate a secret code for you.")
    x = input("Input your word: ")
    y = int(input("Input your number: "))
    code(x, y)
    z = input("Type 'Q' to (Q)uit the program, or 'S' to (S)tart coding another message.")
    if z == "Q":
        print("Thanks for playing!")
        break
    elif z == (not "S") or (not "Q"):
        print("Type 'Q' to (Q)uit the program, or 'S' to (S)tart coding another message.")
input()
