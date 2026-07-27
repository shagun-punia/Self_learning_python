food=['chole bhature','120','burger','40','samosa','15']
price=[120,40,15,89]
print(len(food))
mid=len(food)//2
output=food[mid-1:mid+1]
print(output)
print('First value of list:',food[0])
print('Last value of list:',food[len(food)-1])
print('Middle value of list:',food[3])
food[0]='cold drinks'#modifying
print(food)
print(max(price))
print(min(price))
food.append('pizza')
food.remove('cold drinks')
food.insert(6,90)
print(food)
price.sort()
print(price)
food.reverse()
print(food)
print('------------------------')


#list by user input
a=input('enter name1:')
b=input('enter name2:')
c=input('enter name3:')
students=[a,b,c]
print(students)
print(len(students))
students.reverse()
print(students)

#now with the of append
students=[]
students.append('ram')
students.append('sham')
students.append('shiv')           
print(students)                                                                                                                                                                                                                                                                                       
print(len(students))
students.reverse()
print(students)

#movie from user
a=input('enter movie name:')
b=input('enter movie name:')
c=input('enter movie name:')
fav_movies=[a,b,c]
print(fav_movies)