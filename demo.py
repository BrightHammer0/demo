new_file=open('second.txt','w')
with open ('first.txt','r') as f:
    str1=f.read()
    new_file.write(str1.replace('#',''))
