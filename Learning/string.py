a=input('enter your fav food:')
mid=len(a)//2
output1=a[mid-2:mid+2]
print(output1)
print('----------------------------')

#program to use string methods
a=input('Enter any word:')
print(a.upper())
print(a.lower())
print(a.title())
print(a.find('ha'))
print(a.replace('un','unn'))
print(a.count('a'))
print(a.endswith('a'))
print('-----------------------')

#one ques on sentence
a=input('enter a sentence:')
b=(a.lower())
c=(b.replace(' ','_'))
print('---new string is----\n',c)
print('------------------------')

#question
a=input('Enter a string or line:\n')
print('Total characters are:\n',len(a))
print('lowercase version is:\n',a.lower())
print('uppercase version is:\n',a.upper())
print('---------------------------------------')

#next ques
a=input('Enter a string or line:\n')
print(a[0])
b=len(a)
print(b)
print(a[b-1])
