class laptop:
    brand='Default'
    RAM='Default 8GB'
    price='Default 1lakh'

#obj values has more significance than class

obj1=laptop()
obj1.brand='macbook'
obj1.RAM='64GB'
obj1.price='2Lakh'
print('brand',obj1.brand)

obj2=laptop()
obj2.brand='hp'
obj2.RAM='128GB'
print('brand',obj2.brand)
print('price:',obj2.price)