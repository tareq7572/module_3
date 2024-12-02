#try except (error handle)

'''i=int(input('enter a number'))
print(i)'''

#there is problem after error next line not working 
'''try:
    i=int(input('enter a number'))
    print(i)
    x=10
    print(x)
except:
    print('x is not found')
finally:
    print('thank you')'''


'''
try:
    a=int(input('enter a number'))
    print(a)
except:
    print('wrong input')'''

#multiple exception handle
#only first error showing 
try:
    with open('file3.txt','r') as file:
        r=file.read()
        print(r)
        print(10/0)
except Exception as e:
    print(e)



