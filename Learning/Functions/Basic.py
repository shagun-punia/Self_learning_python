#Functions basics .....Functions improve the readability and reusability of code

def sumFunc():
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    sum = a + b
    print("Sum is:", sum) #this code part doesn't print anything bcoz here we define the fun. not call the fun. 
#....100 line of code
sumFunc()#function calling


print('---------------------------')
#Function definition with parameters
def average(a=0,b=0):#0 are default values that are used in case their is no any arguments are given
    averageValue=(a+b)/2
    print(averageValue)

       
#Function calling with arguments e.g.,(5,10)
average(5,10)
average(7,10)
average(80,98)
average(2,4)
average()#gives error as there is no any arguments in it

#RETURN statement
'''Used to send a value back from a function; After return, the function stops execution'''
def multiply(a=10,b=10):
    return a*b
print(multiply(15,10))
'''result=multiply(5,10)
print(result)'''

#keyword arguments:we can use parameter name while passing values.
def student_info(name,age):
    print(name,'is',age,'years old.')
student_info(age=21,name='ram')
