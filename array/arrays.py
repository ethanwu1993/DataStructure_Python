from array import *

arr1 = array('i', [1, 2, 3, 4, 5])

for i in arr1:
  print(i)


print(arr1[2])

arr1.append(6)

print(arr1)

arr1.insert(0, 0)
print(arr1)


arr2 = array('i', [7, 8])
arr1.extend(arr2)
print(arr1)

temp_list = [20, 21, 22]
arr1.fromlist(temp_list)
print(arr1)

arr1.reverse()

print(arr1)
str_arr = arr1.tobytes()