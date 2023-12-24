#Tuples

my_tuple = (1, 2, 3) #create tuple
print(my_tuple) 

# Accessing Elements

my_tuple2 = (1, 2, 3, 'edureka') #access elements
for x in my_tuple2:
    print(x)
print(my_tuple2)
print(my_tuple2[0])
print(my_tuple2[:])  # access all value
print(my_tuple2[3][4]) #Nested tuple 3 index element's 4th value 'e'

# Appending Elements

my_tuple = (1, 2, 3)
my_tuple = my_tuple + (4, 5, 6) #add elements
print(my_tuple)

# Other Functions

my_tuple = (1, 2, 3, ['hindi', 'python'])
my_tuple[3][0] = 'english'
print(my_tuple)
print(my_tuple.count(2))
print(my_tuple.index(['english', 'python']))