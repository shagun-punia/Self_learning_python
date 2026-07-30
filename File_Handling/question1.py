#write a program to read a text from file certificate.txt 
# and find whether it contains the word Live.

file= open('certificate.txt','r')
filedata=file.read()
filedata=filedata.lower()
if 'live' in filedata:
    print('yes live word is present')
else:
    ('no live word isn\'t present')
    file.close()