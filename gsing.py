import random

words = ["United States", "New York", "Los Angeles", "Toronto", "London", "Manchester", "Italy", "Rome"]
word = random.choice(words).upper() 

total_chances = 7
guessed_word = "_" * len(word)  

while total_chances > 0:
    print("\nGuessed Word: ", guessed_word)  
    letter = input("Guess a letter: ").upper()  

    if letter in word:
        for index in range(len(word)) :
            if word[word]==letter:
                guessed_word = guessed_word[:index]+letter+guessed_word[index +1 :]

        if guessed_word == word:  
            print("\n Congratulations, you won! :")
            break
    else:
        total_chances -= 1
        print(" Incorrect guess! Remaining chances: {total_chances}")

if guessed_word != word: 
    print("\nGame Over!  You lost.")
    print("The correct word was:", word)

         

