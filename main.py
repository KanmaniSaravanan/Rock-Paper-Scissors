# To set the choices of the computer
import random

print('1.Rock\n2.Paper\n3.Scissors')

winning_conditions = {
    '1.Rock': {'1.Rock': 'GAME TIE', '2.Paper': 'YOU LOST', '3.Scissors': 'YOU WON'},
    '2.Paper': {'1.Rock': 'YOU WON', '2.Paper': 'GAME TIE', '3.Scissors': 'YOU LOST'},
    '3.Scissors': {'1.Rock': 'YOU LOST', '2.Paper': 'YOU WON', '3.Scissors': 'GAME TIE '}

}


def player_outcome(number):
    if number == 1:
        return '1.Rock'
    elif number == 2:
        return '2.Paper'
    elif number == 3:
        return '3.Scissors'
    else:
        print('INVALID INPUT !!!')


def comp_outcome(number):
    if number == 1:
        return '1.Rock'
    elif number == 2:
        return '2.Paper'
    elif number == 3:
        return '3.Scissors'


while True:
    player = int(input('Enter your choice: '))
    player_choice = player_outcome(player)

    random_number = random.randint(1, 3)
    comp_choice = comp_outcome(random_number)

    print('YOUR CHOICE: ', player_choice)
    print('COMP CHOICE: ', comp_choice)

    print(winning_conditions[player_choice][comp_choice])

    restart = (input('Do want to play again? y/n '))

    if restart.lower() == 'y':
        continue
    else:
        break
