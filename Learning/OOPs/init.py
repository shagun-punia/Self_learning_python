class student:
    schoolname='ABC School'

    def __init__(self,name,course):
        #print('Whenver a new obj is created I called automatically')
        self.name=name
        #print(self.name)
        self.course=course
        #print(self.course)

    
student1=student('ram','betch')#ini t method called
print(student1.schoolname)
print(student1.name)
print(student1.course)

student2=student('sham','bsc') 
