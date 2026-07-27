food=['apple','cake','banana','mango']
for i in food:
    print(i)
print('--------------------')
letter=('a','b','c')
for i in letter:
    print(i)
print('--------------------')
student={'name':'ram','age':20,'rollno':101}   # dictionary with keys and values
for i in student:  # iterates over keys in the dictionary
    print(f"{i}: {student[i]}")  # print current key and its value
print('---------------------')  # separator after each item

a={'a','e','c','d'}
for i in a:
    print(i)
    # explain: iterates over elements in the set; order may vary
print('---------------------')
#even number using for loop
for i in range(2,21,2):
    print(i)
print('---------------------')
for i in range(1,51):
    if(i%5==0):
        print('Ram')
    else:
        print(i)
print('---------------------')
#square of numbers using for loop
for i in range(1,11):
    print(f'square of {i} is {i*i}')#we also write it as pow{i,2}or {i**2}
print('---------------------')

i=int(input('enter a number:'))
for j in range(1,11):
    print(f'{i}x{j}={i*j}')
print('---------------------')

for i in range(100,0,-1):
    print(i)
print('---------------------')
a='shagunpunia'
for i in range(1,6):
    print(a.upper())