class Student:
    def __init__(self,name,ListofMarks):
        self.name=name
        self.ListofMarks=ListofMarks

    def average(self):
        sum=0
        for each in self.ListofMarks:
            sum=sum+each

        average=sum/3
        print("average is",average)

student1=Student('Ram', [90,67,86])
student1.average()