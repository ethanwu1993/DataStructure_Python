import numpy as np

arr = np.array(
    [[11, 15, 10, 6],
     [10, 14, 11, 5],
        [12, 17, 12, 8],
        [15, 18, 14, 9]
     ]
)


def accessElements(arr, r_index, col_index):

    if r_index >= len(arr) or col_index >= len(arr[0]):
        print('Incorrect index')
    else:
        print(arr[r_index][col_index])


# accessElements(arr, 2, 3)


def traverse(arr):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            print(arr[i][j])


# traverse(arr)


def search(arr, target):
    for i in range(len(arr)):
        for j in range(len(arr[0])):
            if arr[i][j] == target:
                print(arr[i][j])
                return 'The value is located at index: ' + str(i) + " " + str(j)

    return 'value not found'


print(search(arr, 6))


# deletion

newArr = np.delete(arr, -1, axis=1)

print(newArr)