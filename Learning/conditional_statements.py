#conditional statements
marks=85
if (marks>=90):
    print('Your grade is A')
else:   #if you want condition in else also then use elif(marks>=80) ,print('your grade is b)
    #elif used for multiple conditions

    print('your grade is not A')
print('---------------------')
#used of elif
a=int(input('enter a number:'))
if(a>0):
    print('a is positive.')
elif(a==0):
    print("a is zero")
elif(a<0):#here we can also simply use elsle(): print('negative')
    print('a is negative')
print('-----------------------')

#grade using if -elif
marks=int(input("enter marks:"))
if(marks>=90):
    print('Grade A')
elif(marks>=80):
    print('Grade B')
elif(marks>=70):
    print('Grade C')
elif(marks>=60):
    print('Grade D')