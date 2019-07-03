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
    isBig = 11 <= total <= 18
    isSmall = 3 <= total <= 10

    if isBig:
        return 'big'
    elif isSmall:
        return 'small'


def start_game():
    print('<<<< GAME START! >>>>')
    choices = ['big', 'small']
    your_choices = input('big or small : \n')
    if your_choices in choices:
        points = roll_dice()
        total = sum(points)
        youWin = your_choices == roll_result(total)
        if youWin:
            print('The points are',points,'You Win !')
            return 'youwin'
        else:
            print('The points are',points,'You Lose !')

        return 'youWin'

    else:
        print('Invalid Word')
        start_game()

def roll_money(money_now,money_bet):
    while money_now > 0:
        money_bet = input('How much you wanna bet ?:')
        win = start_game()
        if win == 'youwin':
            print(win)
            money_now = int(money_now)  + int(money_bet)
            print('You gained ', money_bet, 'you have ', money_now, 'now!')
        else:
            money_now = int(money_now) - int(money_bet)
            print('You losed ', money_bet, 'You have' , money_now, 'now!')


roll_money(1000,1)
print('GAME OVER')
