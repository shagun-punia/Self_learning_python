'''modules are the files containing python code which can be imported in other python files.
They can define functions, classes and variables which can be used in other python files.
They can used to copy , rename and delete files.
Think of modulesas a toolbox '''
#COPY CODE 
import shutil
shutil.copy('Module.py','try.txt')#copy the file Module.py to try.txt

#RENAME CODE
import os
os.rename('try.txt','try1.txt')#rename the file try.txt to try1.txt

with open('none.py','x') as f:
    f.write('print("hello")')#create a new file none.py and write the data in it

#DELETE CODE
import os
os.remove('none.py')#delete the file none.py