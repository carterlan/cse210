import random
list = ['stock', 'over', 'flow']
word = random.choice(list)
word_in_progress = []
size = len(word)

jumper = ['  ___',
        ' /___\ ',
        ' \   / ',
        '  \ / ',
        '   O  ',
        '  /|\ ',
        '  / \ ',
        '      ',
        '^^^^^^^']
trys = 5

for j in word:
        word_in_progress += '_'

while trys != 0:
    guesser = True
    failed = 0
    j = 0

    
    #print(word_in_progress[j])
    for i in range(len(jumper)):
        print(jumper[i])

    guess = input('Guess a letter [a-z]: ')
    
    for letter in word:
        if word_in_progress[j] == "_":
            if letter == guess:
                word_in_progress[j] = letter
                #replace the i element in the line
            else:
                failed += 1
        else:
            #word_in_progress += '_'
            failed += 1
        j += 1
    

    if failed == size:
        guesser = False

    if guesser is False: 
        jumper.pop(0)
        trys -= 1

    if trys == 0:
        jumper.insert(0,'   x')
        for i in range(len(jumper)):
            print(jumper[i])
        quit()
    
    final_word = ''.join(word_in_progress)
    print(f'{final_word}\n')

    if final_word == word:
        print('You Win')
        quit()

