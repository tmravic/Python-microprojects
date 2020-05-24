times = 0
def code(word, num):
    global times
    alphabet = 'abcdefghijklmnopqrstuvwxyz'
    storage = []
    out = []
    if type(num) != int:
        return print("A key number must be entered")
    if num >= 26 or num <= 0:
        return print("This number couldn't produce a coded message")
    if type(word) != str:
        return print("A key word must be entered")
    word = word.lower()
    word = word.replace(" ", "")
    for i in word:
        if i not in alphabet:
            return print("Your message cannot contain non-letters")
    for i in range(len(word)):
        storage.append(alphabet.index(word[i]))
    storage2 = list(map(lambda x: x + num, storage))
    def lose26(d):
        for x in d:
            if x >= 26:
                out.append(x-26)
            else:
                out.append(x)
        return out
    storage3 = list(lose26(storage2))
    coded_word = ""
    for x in storage3:
        coded_word += alphabet[x]
    times = times + 1
    print(times)
    return print("Your secret message is: \n" + coded_word)
while times <= 3:
    print("Welcome to the Cryptography program. You can input a message and a number less than 26, and this program will generate a secret code for you.")
    x = input("Input your word: ")
    y = int(input("Input your number: "))
    code(x, y)
    if times < 3:
        print("Let's try it again!")
    else:
        print("Thanks for playing!")
        break
input()