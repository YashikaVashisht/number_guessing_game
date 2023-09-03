import random

print("\t\t\t\t\tWELCOME TO NUMBER GUESSING GAME\n\n\n\n")
print("I'm thinking of a number between 1 to 100")

list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15, 16, 17, 18, 19, 20, 21, 22, 23, 24, 25
    , 26, 27, 28, 29, 30, 31, 32, 33, 34, 35, 36, 37, 38, 39, 40, 41, 42, 43, 44, 45, 46, 47, 48, 49, 50,
      51, 52, 53, 54, 55, 56, 57, 58, 59, 60, 61, 62, 63, 64, 65, 66, 67, 68, 69, 70, 71, 72, 73, 74, 75,
      76, 77, 78, 79, 80, 81, 82, 83, 84, 85, 86, 87, 88, 89, 90, 91, 92, 93, 94, 95, 96, 97, 98, 99,100]
def start(computer_choice):
    user = input("You have to choose a  difficulty level(hard or easy):")
    if user == 'easy' or user == 'Easy' or user == 'EASY':
        easy(computer_choice)
    elif user == 'hard'or user == 'Hard' or user == 'HARD':
        hard(computer_choice)
    else:
        print("You have entered an invalid option.Choose again.")

        start(computer_choice)
'''def guess(computer_choice):
    guess = int(input("make a guess"))
    if guess  not in range(0,101):
        print("you have entered the number out of range")
        
        #guess(computer_choice)

    else:
        if guess==computer_choice:
            return " you have made a right guess"
             
        elif guess>computer_choice:
            print("TOO HIGH")
            guess(computer_choice)
        elif guess<computer_choice:
            print("TOO LOW")
            guess(computer_choice)'''





def easy(computer_choice):
    attempts = 7
    while(attempts != 0):
        guess = int(input("Make a guess:"))
        if guess  not in range(0,101):
            print("you have entered the number out of range")
            #guess(computer_choice)

        else:
            if guess == computer_choice:
               print("You have made a right \n YOU WIN")
               break
            elif guess > computer_choice:
                print("TOO HIGH")
                #guess(computer_choice)
            elif guess < computer_choice:
                print("TOO LOW")
               # guess(computer_choice)
        attempts -= 1
        if attempts == 0:
            print("you are out of turns")
            print("GAME OVER")
            print("The number is:",computer_choice)



def hard(computer_choice):
     attempts = 5
     while (attempts != 0):
         guess = int(input("Make a guess:"))
         if guess not in range(0, 101):
             print("You have entered the number out of range.")
             #guess(computer_choice)

         else:
             if guess == computer_choice:
                 print("You have made a right guess.\nYOU WIN")
                 break
             elif guess > computer_choice:
                 print("TOO HIGH")
                 # guess(computer_choice)
             elif guess < computer_choice:
                 print("TOO LOW")
             # guess(computer_choice)
         attempts -= 1
         if attempts == 0:
             print("You are out of turns")
             print("GAME OVER!!")
             print("The number is:",computer_choice)


computer_choice = random.choice(list)

start(computer_choice)
