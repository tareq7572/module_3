import os
#make a directory 
#os.mkdir('new')
#make file inside a directory 
'''with open('new/test.txt','w') as file:
    file.write('hello')'''
#os.mkdir('new2')
#listing directory
'''dir=os.listdir()
print(dir)'''

#rename directory 
#os.rename('new','mydir')

#delete non empty directory
'''import shutil 
shutil.rmtree('new')'''

#we can use here try 

'''import shutil 
try:
    shutil.rmtree('new3')
    print('file delete done')
except:
    print('file not found')'''

#list all files of directory 
f=os.listdir('new2')
print(f)
