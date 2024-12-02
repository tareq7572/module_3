#Dictionary items are ordered, changeable, and do not allow duplicates.

d={
    'item':'cake',
    'bday date': '27/11/24',
    'name': 'tareq'
}

#print (d['bday date'])

dic={
    'title':'coding',
    'author':'tareq',
    'price':'200'
}
#print(dic)
#print(dic['title'])

'''k=dic.keys()
print(k)
for x in k:
    print(x)
v=dic.values()
print(v)
for x in v:
    print(x)
if 'title' in dic:
    print(dic['title'])'''

'''
#update value
print(dic)
dic['title']='python coding'
print(dic)

#add value 
dic['quantity']=20
print(dic)

#delete value 
dic.pop('quantity')
print(dic) 

#when item not available
value=dic.pop('author','not found')
print(dic)
print(value)'''

#clear everything 
'''dic.clear()
print(dic)'''

#delelte full
'''del dic
print(dic)'''

#loop 
'''for x in dic:
    print(x)

for x in dic:
    print(dic[x])'''

'''for x in dic.values():
    print(x)

print(dic)

for x,y in dic.items():
    print(f'{x}: {y}')'''

#add in list discuss with sumiya



l=[]
l.append(dic)
l.append(d)
print(l[1])








