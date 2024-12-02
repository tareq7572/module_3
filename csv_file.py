import csv
data=[
    ['Book_Name','Autho_Name','Price'],
    ['Coding','Tareq',100],
    ['Love','Sumiya',200],
    ['Love2','Tareq',150]

]

#here newline='' for avoding space
#only create ? 
'''
with open('my.csv','w',newline='') as file:
    w=csv.writer(file)
    w.writerows(data)


with open('my.csv','r') as file:
    r=csv.reader(file)
    print(r)
    for x in r:
        print(x)
    
'''
'''
data2=[
  ['Math', 'Ahmed', 120],
  ['Science', 'Kazi', 250]
]

#append in csv file 
with open('my.csv','a',newline='') as file:
    w=csv.writer(file)
    w.writerows(data2)
'''

#how to update csv file 
update_data=[]
with open('my.csv','r') as file:
    r=csv.reader(file)
    for x in r:
        if(x[0]=='Love2'):
            x[2]=250
        update_data.append(x)

with open('my.csv','w',newline='') as file:
    w=csv.writer(file)
    w.writerows(update_data)





