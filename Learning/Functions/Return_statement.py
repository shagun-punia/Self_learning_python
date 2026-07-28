#question:1
def square(a=0):
    return a**2
print(f'{square(15)}\n')

#question:2-Write a function that takes a string and returns the count of vowels and consonants saperately.
def fun(userInput):
    
    vowels='aeiouAEIOU'
    countVowels=0
    countConsonants=0

    for eachChar in userInput:
        if(eachChar.isalpha()):
            if(eachChar in vowels):
                countVowels+=1
            else:
                countConsonants=+1

    return countVowels,countConsonants
vowels , consonants=fun('My name is ram')
print(vowels,consonants)

#question:3-return upper case version 
def uppercase(a):
    return a.upper()
print(uppercase('har har mahadev'))


#question:4-full name joined with space
def full_name(fname,lname):
    first=fname.capitalize()
    last=lname.capitalize()

    return first,last
f,l=full_name('ram','sharma')
print(f'{f} {l}')


