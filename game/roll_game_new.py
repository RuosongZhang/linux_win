import random

def roll_dice(numbers=3, points=None):
    print('<<<<< ROLL THE DICE! >>>>>')
    if points is None:
        points = []

    while numbers > 0:
        point = random.randrange(1,7)
        points.append(point)
        numbers = numbers - 1

    return points


def roll_result(total):
    isBig = 11 < total <= 18
    isSmall = 3 <= total <= 10

    if isBig:
        return 'big'
    elif isSmall:
        return 'small'



def start_game():
    your_money = 1000

    while your_money > 0:
        print('<<<<<<<<<<<<< GAME START >>>>>>>>>>>>>')
        choices = ['big', 'small']
        your_choices = input('big or small :')

        if your_choices in choices:
            your_bet = int(input('How much you wanna bet ? -'))
            points = roll_dice()
            total = sum(points)
            you_win = your_choices == roll_result(total)

            if you_win:
                print('The point is',points,'You Win')
                print('You gained {},you have {} now'.format(your_bet,your_money + your_bet))
                your_money = your_money + your_bet

            else:
                print('The point is',points,'You lose')
                print('You gained {},you have {} now'.format(your_bet,your_money - your_bet))
                your_money = your_money - your_bet

        else:
            print('Invalid Words')

    else:
        print('GAME OVER')

start_game()
