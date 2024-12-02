import zipfile
#zip create 

'''with zipfile.ZipFile('myzip.zip','w') as z:
    z.write('zipfile1.txt')
    z.write('zipfile2.txt')'''

#unzip

with zipfile.ZipFile('myzip.zip','r') as z:
    z.extractall()
    e=z.namelist()
    print(e)

