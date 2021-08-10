# input user
# computer
# cases
# return winner
# rock wins scissors 
# paper wins rock 
# scissors wins  paper 
# rock 1 paper 2 scssiors 3

import random

def game(comp,user):
    set=0
    if comp=='r' and user=='s' or comp=='p' and user=='r' or comp=='s' and user== 'p':
       set=1
    elif comp=='s' and user=='r' or comp=='r' and user=='p' or comp=='p' and user== 's':
        set=2
    else:
        set=-1
    return set



user=input("Enter your choice \n r for rock\n p for paper\n s for scissors \n")
comp=random.randint(1,3)
if comp==1:
    comp='rock'

elif comp==2:
    comp='papaer'

else:
    comp='scissors'

result=game(comp,user)
if(result==1):
    print(f"Computer chose {comp}")
    print("COMPUTER WON..")
    
elif(result==2): 
    print(f"Computer chose {comp}")
    print("USER WON..")
elif(result==-1):
    print(f"Computer chose {comp}")
    print("TIE GAME..")
