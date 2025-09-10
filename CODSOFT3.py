#To do list
li={}
di=[]
u='y'
while(u=='y'):
    print('A to add,R to remove,U to update,D for task done')
    choice=input('Enter operation')
    if choice=='A':
       t=int(input('Task number'))
       n=input('Task description')
       li[t]=n
    elif choice=='R':
       t=int(input('Enter task number to remove'))
       del li[t]
    elif choice=='U':
       t=int(input('Enter task number to update'))
       n=input('Enter the new description')
       li[t]=n
    elif choice=='D':
       t=int(input('Enter the task number for the task done'))
       d=li.pop(t)
       di.append(d)
    else:
       print('Invalid operation')
    
    print('To do list',li)
    print('Done list',di)
    u=input('Want to continue?(y/n)')
    
