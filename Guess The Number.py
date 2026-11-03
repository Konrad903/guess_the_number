from random import *
num=randint(1,1000)
attempts=0


def play():
    global attempts
    won=False

    
    while attempts<10:
        attempts+=1
        user=int(input('___WELCOME TO GUESS THE NUMBER___\n\n' \
        'Enter your guess here:')) 
        try:
            if user>num:
                print('Sorry! Your guess was too high')
                ask=str(input('Type "go" to try again:'))
                if ask=='go':
                    play()
                    return
            elif user<num:
                print('Sorry! Your guess was too low')
                ask=str(input('Type "go" to try again:'))
                if ask=='go':
                    play()
                    return
            elif user==num:
                print('YOU WIN!! Your guess was correct!',num)
                break        
        except ValueError:
            print('Input is invalid. Please enter a valid number.')
    if attempts==10:
            print(f'You ran out of attempts. Better luck next time!\nThe secrect number is: {num}')
play()


        
