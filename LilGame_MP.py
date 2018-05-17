import random

number = random.randint(0,3)

words = ["Vine","New Girl","panda","Spongebob"]
hint1 = ["Croissants","True American","eates bamboo","yellow"]
hint2 = ["Go back to sleep and starve","Jess","lives in China","I love Krabby Patties"]


secretword = words[number]

guess = ""
counter = 1

while True:
    print("Guess the secret word")
    print("Type 'hint1', 'hint2', 'first letter', or 'give up' for answer.")
    guess = input()

    if guess == secretword:
          print("You win!")
          print("It took you " + str(counter) + " guesses.")
          break
        
    elif guess == "hint1":
            print( hint1[number] )
            
    elif guess == "hint2":
            print( hint2[number] )

    elif guess == "first letter":
            print( secretword[0] )

    elif guess == "give up":
            print("Wow. What even is your GPA?")
            print("You failed...not surprised that you failed " + str(counter)+ " times.")
            break

    else:
        print("Guess again.")
        counter += 1
          
