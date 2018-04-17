import random
guesses_left = 10
"""
A general guide for Hangman
1.Make a word bank- 10 items
2.Pick a random item form the list
3.Add a guess to the list of letters guessed
4.Reveal letters already guessed
5.Create the win condition
"""
word_bank = ("Oh hi Mark", "Hey Vsauce Michael Here", "Aw yeah this is happenin", "What's the pythagorean theorem",
             "God Bless America", "Hi Billy Mason here", "Bill Nye the Science Guy", "Cory in the house", "Kachao")

word = random.choice(word_bank)
# print(word)
letters_guessed = [' ']

win = False
guess = ""
while guesses_left > 0 and not win:
    output = []
    for letter in word:
        if letter in letters_guessed:
            output.append(letter)
        else:
            output.append("*")
    print("".join(output))
    if output == list(word):
        print("You win")
        win = True
        continue
    guess = input("Guess a letter: ")
    letters_guessed.append(guess)
    print(letters_guessed)
    if guess not in word:
        guesses_left -= 1
    print(guesses_left)
    if guesses_left == 0:
        done = True
