tup=(89,76,43)
print(tup)
#tup[0]=1----shows error bcoz tuple is immutable
emptytup=()
print(emptytup)
print(type(emptytup))
singletup=(1,)#if u don't add ,after element it show it datatype int not tuple
print(type(singletup))
#take input from user
a=int(input('enter element1:'))
b=int(input('enter element2:'))
c=int(input('enter element3:'))
tuple=(a,b,c)
print(tuple)
print('---------------------------------------------------------')

#question on tuple
#tuple of 5fav fruits by take input by user
a=input('enter your fav. fruits :\n')
b=input('enter your fav. fruits :\n')
c=input('enter your fav. fruits :\n')
d=input('enter your fav. fruits :\n')
e=input('enter your fav. fruits :\n')
tuple=(a,b,c,d,e)
print(len(tuple))
print(tuple[0])