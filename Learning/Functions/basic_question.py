#question:1 
def welcome_message():#function definition by def keyword
    print('Welcome to Python Programming!\n'*3)
print('-----------')
welcome_message()#function calling

#question:2
def inspire():
    print('\"The future depends on your next move.Make it count\"')
print('----------')
inspire()

#question:3
def good_morning():
    print('\"Good Morning<--->Have a NICE DAY😊\"')
print('------------------------')
good_morning()
good_morning()

#question:4
#Why functions use in programming?Write two advantages.
'''Functions are used in programming to improve code :
organization, readability, and reusability. 
They allow developers to break down complex problems into smaller, manageable pieces, 
making the code easier to understand and maintain
Advantage 1: Reusability - 
Functions can be called multiple times without rewriting the same code.
Advantage 2: Maintainability - 
Changes to a function are reflected everywhere it is called, making it easier to update and maintain the code.'''

#question:5
def learn():
    print("3 topics of python :\n")
    print('Dictionary,Tuples,List')
print('-----------------------')
learn()

#question:6
#Explain what happens if you call a function before defining it.
"""
If you try to call a function before it is defined in Python, 
the interpreter raises a NameError.
The function name has not been bound to a callable object yet, 
so Python cannot execute it until the definition appears earlier in the code.

"""
