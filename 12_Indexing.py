#Indexing start from 0 in Maaz Khan on index 0 there is 'M'
#Length start from 1 so in Maaz Khan 'M' is on Length 1 it tells length of string

name = "Maaz Khan"

print(len(name))  # Tell us length of string Output: 9 but total indexes is 0-8
print(name[0])    # Character on index 0 is M
print(name[1])    # Character on index 1 is a

print(name[1:9])                 
# it will return characters from index 1 to 8 b/c last value is exclusive  
# In short [1st ind val : to your wish index val + 1]

print(name[-7:4])  #it counts from backward for -ve and for +ve count forward
 
