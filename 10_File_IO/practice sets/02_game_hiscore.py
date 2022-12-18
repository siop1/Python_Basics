'''
The game() function in a program lets a user play a game and returns the score as an integer. You need to read a file 'hiscore.txt' which is either blank or contains the previous hiscore. You need to write a program to update the hiscore whenever game() breaks the hiscore.

'''
def game():
    return 200

with open('02_hiscore.txt') as f:
    previous_score=f.read()
score=game()
if previous_score=='':
    with open('02_hiscore.txt','w') as f:
        f.write(str(score))


elif score>int(previous_score):
    with open('02_hiscore.txt','w') as f:
        f.write(str(score))

