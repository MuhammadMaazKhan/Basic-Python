#Basic Built In Data Structures in Python
# 1. Tuples                        (1, 2, 3)
# 2. List                          [1, 2, 3]
# 3. Dictionaries                  {'key1': 'value1', 'key2': 'value2'}
# 4. Set                           {1, 2, 3} or set([1, 2, 3])

#DIFFERENCE 
# CHANGE ABLE (CRUD) ALL EXCEPT TUPLE
# List and Tuples allow duplicate elements dict have unique key but set doesn't 

# 1. List
my_list = [] #create empty list
print(my_list)
my_list = [1, 2, 3, 'example', 3.132] #creating list with data
print(my_list)

#Add and inser items in List
my_list = [1, 2, 3]
print(my_list)
my_list.append([555, 'abc']) #add as a single element
print(my_list)
my_list.extend([234, 'more_example']) #add as different elements
print(my_list)
my_list.insert(1, 'insert_example') #add value at index 1
print(my_list)

# Delete and remove items in List
my_list = [1, 2, 3, 'example', 3.132, 10, 30]
del my_list[5] #delete element at index 5
print(my_list)
my_list.remove(3) #remove element with value
print(my_list)
a = my_list.pop(2) #pop element from list
print('Popped Element: ', a, ' List remaining: ', my_list)
my_list.clear() #empty the list
print(my_list)

#Accessing Elements in List
my_list = [1, 2, 3, 'example', 3.132, 10, 30]
for element in my_list: #access elements one by one
    print(element)
print(my_list) #access all elements
print(my_list[3]) #access index 3 element
print(my_list[0:2]) #access elements from 0 to 1 and exclude 2
print(my_list[::-1]) #access elements in reverse ????

#other methods
my_list = [1, 2, 3, 10, 30, 10]
print(len(my_list)) #find length of list
print(my_list.index(10)) #find index of element that occurs first
print(my_list.count(30)) #find count of the element
print(sorted(my_list)) #print sorted list but not change original
my_list.sort(reverse=True) #sort and change original list 
print(my_list)

