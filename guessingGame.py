import random

chances = input(
    'Computer has a number, you have 5 chances to guess that number , Yup!All the best!')
chances = 1
number = random.randint(1, 9)


while chances < 6:
    userInput = int(input('generate number between 1 to 9: '))

    if number > userInput:
        print('Your number is too less, please guess a higher number')
    elif number < userInput:
        print('Your number is too high, please guess a lower number')
    else:
        print('Congratulations you Won!')
        break
    chances += 1


if not chances < 6:
    print('You lost')
