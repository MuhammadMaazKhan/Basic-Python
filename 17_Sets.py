# Built in Data Structures
# 4. Sets  union Intersection diff sym.diff
# (Sets cannot have two items with the same value).

my_set = {1, 2, 3, 4, 5, 5, 5} #create set
print(my_set)

# Adding elements

my_set = {1, 2, 3}
my_set.add(4) #add element to set
print(my_set)


# Operations in sets

my_set = {1, 2, 3, 4}
my_set_2 = {3, 4, 5, 6}
print(my_set.union(my_set_2), '----------', my_set|my_set_2)
print(my_set.intersection(my_set_2), '----------', my_set & my_set_2)
print(my_set.difference(my_set_2), '----------', my_set - my_set_2)
print(my_set.symmetric_difference(my_set_2), '----------', my_set ^ my_set_2)
my_set.clear()
print(my_set)

#The union() function combines the data present in both sets.
#The intersection() function finds the data present in both sets only.

#The difference() function deletes the data present in both and outputs 
# data present only in the set passed.

#The symmetric_difference() does the same as the difference() function but 
# outputs the data which is remaining in both sets.
