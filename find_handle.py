#create file and write

'''with open('example.txt','w') as file:
    file.write('hello sumiya')
    file.write('\nhello tareq')



#file append 
with open('example.txt','a') as file:
    file.write('\nlove you')'''
   

#file read
'''
with open('example.txt','r') as f:
    c=f.read()
    print(c)
'''
#rename file 
import os 
#os.rename('example.txt','file1.txt')


#delete file 
os.remove('file1.txt')