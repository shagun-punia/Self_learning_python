class vehicle:
    colour = "black" #attribute
    performance = "high" #attribute
    mileage = "10" #attribute
    def work():
        print('work of vehicle') #methods define what an object can do

#object creation
car=vehicle()     
print(car.colour)

bike=vehicle()
print(bike.performance)

aeroplane=vehicle()
print(aeroplane.mileage)

#created one class and 3 objects if that
'''Class attribute share by all objects
Instance attribute unique for each object'''

class fooditem:
    category='Snacks'
o1=fooditem()
o1.category='gulabjamun'

o2=fooditem()
o2.category='samosa'
print(o1.category)
print(o2.category)