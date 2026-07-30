
with open('Intro.txt') as i:
    #with keyword close  the file automatically
    lines=i.readlines()
    
    print(len(lines))
    line1=i.readline()
    line2=i.readline()
    print(line1)
    #line2=i.readline()
    print(line2)
    line3=i.readline()
    print(line3)
    data=i.read()
    print(data)
    