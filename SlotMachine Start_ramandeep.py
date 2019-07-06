import random
import time
import sys

reelList = ['orange', 'orange', 'orange', 'lemon', 'lemon', 'lemon', \
           'plum', 'plum', 'plum', 'cherries', 'cherries', 'cherries', \
           'banana', 'banana', 'banana', 'bar', 'bar', 'Lucky 7'] #adding quote
nPicturesInReel = len(reelList)#adding len
nCoins = 100
print('You have', nCoins, 'coins to start.  Good luck.')
print()

def payTable(myList): #function to def
    picture1 = myList[0]
    picture2 = myList[1]
    picture3 = myList[2]
    if myList.count(picture1) == 3:
        if picture1== 'Lucky 7':
            nCoinsWon = 500
        elif picture1== 'bar':
            nCoinsWon = 100
        else:
            nCoinsWon = 10

    else:
        if (picture1 == picture2) or (picture2 == picture3) or (picture1 == picture3):#picture 3-added instead of picture 2
            nCoinsWon = 2
        else:
            nCoinsWon = 0

    return nCoinsWon #added nCoinsWon
        

while True:

    bet = input('How many coins do you want to bet (defaults to 1, enter 0 to quit): ')
    if bet == '0': #adding quote
        print( 'Sorry to see you go.  Come back again soon.')
        sys.exit(0)     # New, but works to quit the program
    if bet == '':
        bet = 1
    bet=int(bet)#converting the entry into integer

    resultList = []
    for spin in range(3):
        thisReelIndex = random.randrange(0, nPicturesInReel)
        thisPicture = reelList[thisReelIndex]
        resultList.append(thisPicture)

    print( 'Spinning ... ')
    print()
    time.sleep(.5)
    print( '     ', resultList[0])
    time.sleep(.5)
    print( '     ', resultList[1])
    time.sleep(.5)
    print( '     ', resultList[2])
    print( )
        
    nCoins = nCoins - bet #it should reduce the ncoins left after spinning instead of addition
    payOut = bet * payTable(resultList)

    if payOut == 0:
        print( 'Sorry - you lose.')
    else:
        print( 'You won', payOut, 'coins.  Cha-ching!')
        if payOut > 50:
            print( '                         WOOOOO  HOOOOOOOOOOO!!!!')
            
    nCoins = nCoins + payOut

    print( 'You now have',nCoins, 'coins.')#giving path to print 
    print 
    
