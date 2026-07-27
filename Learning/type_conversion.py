#implicit type conversion
print('program to show implicit type conversion')
print('--------------------------------')
a=5
b=8.5
c= a+b
print(c)
print('data type of c is:',type(c))
print('------------------------------------')

#explict type conversion
print('program to show explict type conversion')
a=input("enter a number:")
print('original value:',a,type(a))
b = float(a)
print('converted value:',a,type(b))
print("------------------------------")