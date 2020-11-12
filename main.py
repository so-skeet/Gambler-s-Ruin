import random

print('''GAMBLER'S RUIN

Eddie the Gambler is the fastest gambler around. Today, He is playing a game called 
"50% Or Nothing."
Eddie has an initial bankroll and a goal amount of money he wants to win. He has 
a 50% chance of either winning or losing and can only make $1 bets. Eddie will keep playing 
until he reaches his goal or goes broke. You decide the initial and goal amounts. 
Can you make Eddie win?
''')

bankroll = int(input('''Enter Eddie's initial bankroll: 
'''))
goalamnt = int(input('''Enter Eddie's desired amount: 
'''))
roundnum = 0
winnum = 0
lossnum = 0

#random number generation

while (bankroll < goalamnt and bankroll > 0):
  result = random.randint(1, 2)

  if result == 1:
    bankroll += 1
    print(bankroll)
    roundnum += 1
    winnum += 1

  elif result == 2:
    bankroll -= 1
    print(bankroll)
    roundnum += 1
    lossnum += 1

if(bankroll == 0):
    print('''
Eddie went broke. Sad! '''
+ '''
Amount of wins: ''' + str(winnum)
+ '''
Amount of losses: ''' + str(lossnum)
+ '''
Total amount of rounds: ''' + str(roundnum))

elif(bankroll == goalamnt):
     print('''
Eddie got the goal! Epic Win!'''
+ '''
Amount of wins: '''+ str(winnum)
+ '''
Amount of losses: ''' + str(lossnum)
+ '''
Total amount of rounds: ''' + str(roundnum))
