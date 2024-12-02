def calculator_func(a,b):
    sum=a+b
    sub=a-b
    mul=a*b
    div=a/b

    #return sum,sub,mul,div
    #return [sum,sub,mul,div]
    return {'add':sum,'subtract':sub,'multi':mul,'divi':div}
result=calculator_func(20,10)
print(result['add'])

#early return 
'''
def even_check(number):
    for x in number:
        if(x%2==0):
            return x
    return None

r=even_check([3,2,5,7,9,10,11])
print(r)'''











