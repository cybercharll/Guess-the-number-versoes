import random #library 

def guess(x): #create the main function function 
    random_number = random.randint(1,x)
    guess = 0
    while guess != random_number: #while loop for guesses
        guess = int(input(f'Type a number between 1 and {x}:'))
        if guess < random_number:
            print('Too low.')
        elif guess > random_number:
            print('Too high.')

    print(f'Yay! You guessed the number {random_number}')

guess(10)
