#Rock Paper Scissor
import random
game='y'
userpoint=0
compoint=0
while(game=='y'):

    print('Rock Paper Scissor')
    hand=input('R=rock,P=paper,S=scissor')

    a=random.randint(1,3)
    if a==1:
        a='R'
    elif a==2:
        a='P'
    elif a==3:
        a='S'
    if hand=='R':
       
        if a=='R':
            print('You choose Rock')
            print('Computer chooses Rock')
            print("It's a tie")
        elif a=='P':
            print('You choose Rock')
            print('Computer chooses Paper')
            print("you lose")
            compoint+=1
        elif a=='S':
            print('You choose Rock')
            print('Computer chooses Scissors')
            print("you win")
            userpoint+=1
    if hand=='P':
        
        if a=='R':
            print('You choose Paper')
            print('Computer chooses Rock')
            print("you win")
            userpoint+=1
        elif a=='P':
            print('You choose Paper')
            print('Computer chooses Paper')
            print("It's a tie")
        elif a=='S':
            print('You choose Paper')
            print('Computer chooses Scissors')
            print("you lose")
            compoint+=1
    if hand=='S':
        
        if a=='R':
            print('You choose Scissors')
            print('Computer chooses Rock')
            print("you lose")
            compoint+=1
        elif a=='P':
            print('You choose Scissors')
            print('Computer chooses Paper')
            print("you win")
            userpoint+=1
        elif a=='S':
            print('You choose Scissors')
            print('Computer chooses Scissors')
            print("It's a tie")
    game=input('Play Again(y/n)')
    
print('GAME OVER')
print('User score:',userpoint)
print('Computer score',compoint)
