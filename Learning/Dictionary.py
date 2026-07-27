Student={'name':'Ram',
          'age':'19',"Place":"Delhi",'name':'sham'}
Students={'a':'1','b':'2','c':'3'}
Student['age']='21'#update or modify
Student['fav sub']='Maths'#add new
Student.pop('Place')#remove
print(Student)
print(Student['name'])
print(type(Student))
Student.keys()#return keys
print(Student.keys())
Student.values()#retuen all values
print(Student.values()) 
Student.items()#all value in tuple
print(Student.items())
Student.get('name')
print(Student.get('name'))
a=Student.update({'Student':'Students'})#updtes or add element
print(a)
print(Student)
print(Students)
print('------------------------------------')

#question for practice
marks={}
marks['maths']=98
marks['english']=96
marks['hindi']=90
print(marks)
print('--------------------')

#question
words={'Begin':'Start','Rich':'Wealthy','Smart':'Intelligent'}
print(words)