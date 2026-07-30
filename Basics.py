file=open('Intro.txt','r') #if we don't specify the mode, it will open in read mode by default
data=file.read() #read the entire file
print('Data of the file:', data) #print the data
file.close() #close the file

with open('Intro.txt') as i:
    #with keyword close  the file automatically
    data=i.read()
    print(data)

with open('Intro.txt') as i:
    #with keyword close  the file automatically
    line=i.readline()
    print(line)