import random

words = ["машина", "кот", "собака", "клубника", "виноград"]

word = random.choice(words)

guesses = ["*"] * len(word)

attemps = 6

while True:
    print('Слово: ', ' '.join(guesses))
    print('Осталось попыток: ' + str(attemps))
    
    guess = input("Угадайте букву: ")
    
    if guess in word:
        for i in range(len(word)):
            if word[i] == guess:
                guesses[i] = guess
    else:
        attemps -= 1
    
    if "*" not in guesses:
        print('Поздравляю, вы победили! Слово: ' + str(word))
        break
    
    if attemps == 0:
        print('К сожалению вы проиграли! Слово: ' + str(word))
        break
