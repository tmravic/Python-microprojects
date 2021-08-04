import random
HP = 5
finish = 3
correct = [0]

while finish >= 0:
    value = random.randint(1, 3)
    correct.append(value)
    print("\nTry guessing a number 1, 2, or 3:")
    answer = int(input())
    if finish == 0:
        print("It's over! Thank you for playing.")
        break
    if HP == 0:
        print("You lose! Sorry.")
        break
    if answer > 3 or answer < 1:
        print("Out of bounds")
        continue
    if answer == value:
        print("correct")
        print(f"The answer was {correct[-1]}.")
        print(f"HP left: {HP}")
        finish -= 1
        print(f"correct answers until finish: {finish}")
    else:
        print("incorrect")
        print(f"The answer was {correct[-1]}.")
        HP -= 1
        print(f"HP left: {HP}")
        print(f"correct answers until finish: {finish}")
        continue
input()