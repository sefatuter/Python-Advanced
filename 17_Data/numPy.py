import numpy as np

py_list = [1,2,3,4,5,6,7,8,9]

# numpy array'i oluşturma

np_array = np.array(py_list)

print(type(py_list))
print(type(np_array)) # Tipi array

py_multi = [[1,2,3],[4,5,6],[7,8,9]] # Çok boyutlu liste
np_multi = np_array.reshape(3,3) # 3'e 3'lük bir matris oluştur

print(py_multi)
print(np_multi)


print(np_array.ndim) # Kaç boyutlu olduğu
print(np_multi.ndim) 

print(np_array.shape) # 9'a 1 lik
print(np_multi.shape) # 3'e 3'lük

