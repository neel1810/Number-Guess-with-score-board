import random
pt=0
no_matches=0
while (1):
    cgn = random.randint(1,9)
    
    for i in range(1,4):
        un = int(input('Enter Guess{} :'.format(i)))
        
        if i == 1 and un == cgn:
            pt+=10
        elif i==2 and un == cgn:
            pt+=6
        elif i==3 and un == cgn:
            pt+=4
        else:
            pt+=0
            
        if un>9 or un<1:
            print('Enter Number between 1 and 9 only')
            print('Number of Attempts left: ',3-i)
        elif un == cgn:
            print('Correct Guess')
            print('You choose {} Computer Choose {}'.format(un,cgn))
            break
        elif un > cgn:
            print('Guess is high')
            print('Number of Attempts left: ',3-i)
        else :
            print('Guess is low')
            print('Number of Attempts left: ',3-i)

        
    print()
    ch =input('Do u want to play again?').lower().strip()[0]
    no_matches+=1
    if ch == 'n':
        break
print()
print('Number of Matches Played: ',no_matches)
print('Points Gained: ',pt)
        
