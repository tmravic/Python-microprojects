def code(word, num):
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
    return print("Your secret message is: \n" + coded_word)
z = "start"
while z == "start":
    print("Welcome to the Cryptography program.")
    print("You can input a message and a number less than 26, and this program will generate a secret code for you.")
    x = input("Input your word: ")
    y = int(input("Input your number: "))
    code(x, y)
    z = input("Type 'Quit' to end the program, or 'Start' to code another message.").lower()
    if z == "quit":
        print("Thanks for playing!")
        break
    elif z == (not "start") or (not "quit"):
        print("Type 'Quit' to end the program, or 'Start' to code another message.")
input()