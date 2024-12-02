a='I am Global'
print(a)
def myfunc():
    global a
    a='I am Local'
    print(a)

myfunc()
print(a)
