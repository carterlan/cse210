import random

card = random.randint(1,13)
points = 100
play = 'y'

while play == 'y':
    print(f'The card is: {card}')
    guess = input('higher or lower? [h/l] ')

    next_card = random.randint(1,13)

    if next_card <= card:
        if guess == 'h':
            points = points - 75

        elif guess == 'l':
            points = points + 100

    if next_card >= card:
        if guess == 'h':
            points = points + 100

        elif guess == 'l':
            points = points - 75

    print(f'The next card was: {next_card}')
    print(f'Your score is : {points}')
    if points <= 0:
        print('Game over\n')
        quit()

    play = input(f'\nPlay again? [y/n] ')
    card = next_card

