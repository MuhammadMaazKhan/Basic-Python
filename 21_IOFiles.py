
f = open('text.txt', 'r')

'''data = f.read()'''

data = f.readline()
data = f.readline()

print(data)
f.close()

f = open('write.txt','w') # it will make new file and write given lines
f.write(' writing in new file')
f.close()

f = open('write.txt','a')
f.write(' I am appending new text in write file')
f.close()

''' best way for IO file is with statement'''
with open('text.txt' , 'r') as f:
    f.read()
with open('text.txt' , 'w') as f:
    f.write(' His problem will be resolved soon')
with open('text.txt' , 'a') as f:
    f.write(' verry soon append')