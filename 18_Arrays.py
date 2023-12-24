import numpy as np

arr =  np.array([1,2,3,4,5]) #list (vector)
arr_0 = np.zeros(2 , dtype=np.int8)
arr_1 = np.ones(2, dtype=np.float16)
arr_empty = np.empty(2)
arr_arange = np.arange(6) #imp 
arr_arange1 = np.arange(6,12) #imp 6 to 11 array
arr_arange2 = np.arange(2,12,2) #imp  2 to 12 array with 2 num gap
arr_linsp = np.linspace(0,12,num=3) # give 3 num from 0 to 12 with same diff 
arr_reshape = arr_arange.reshape(2,3) # reshape vector 1d into matrices 2d


print(arr)
print(arr_0)
print(arr_1)
print(arr_empty)
print(arr_arange) #imp
print(arr_arange1) #imp
print(arr_arange2) #imp
print(arr_linsp) #imp
print(arr_reshape)



arr_2d = np.array([[1,2,3] , [9,2,3] , [4,5,6] , [5,6,7]])  #list of list(matrix)
print('\n''\n''2d array', '\n' , arr_2d)