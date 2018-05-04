#Maurine Chepkoech
#Rock paper scissors.
player1= input('player 1?')
if not(player1 == 'rock' or player1 == 'scissors' or player1 == 'paper'):
    print ('This is not a valid object selection')
else :
    player2= input('player 2?')
    if not(player2 == 'rock' or player2 == 'scissors' or player2 == 'paper'):
        print ('This is not a valid object selection')
    elif (player1 == 'rock' and player2 == 'scissors'):
            print ('player 1 wins.')
    elif (player1 == 'rock' and player2 == 'rock'):
            print ('Tie')
    elif (player1 == 'rock' and player2 == 'paper'):
            print (' player 2 wins')
    elif (player1 == 'scissors' and player2 == 'rock'):
            print (' player 2 wins')
    elif (player1== 'scissors' and player2 == 'scissors'):
            print ('Tie')
    elif (player1== 'scissors' and player2 == 'paper'):
            print ('player 1 wins')
    elif (player1== 'paper' and player2 == 'rock'):
            print ('player 1 wins')
    elif (player1== 'paper' and player2 == 'paper'):
            print ('Tie')
    elif (player1== 'paper' and player2 == 'scissors'):
            print ('player 2 wins')
