import random

with open('wordlist.txt', 'r') as f:
    words = f.readlines()

word = random.choice(words)[:-1]

allowed_errors = 5 #change to the number of your choice
guesses = []
done = False

while not done:
    for letter in word:
        if letter.lower() in guesses:
            print(letter, end=" ")
        else:
                print("__", end=" ")
    print("")
            
    guess = input(f"Allowed Erros Left {allowed_errors}, Next Guess: ")
    guesses.append(guess.lower())
    if guess.lower() not in word.lower():
        allowed_errors -= 1
        if allowed_errors == 0:
            break
                
    done = True
    for letter in word:
        if letter.lower() not in guesses:
            done = False

if done:
    print(f"You Won! The Word Was {word}!!!")
else:
    print(f"You Lost! The Word Was {word}!")