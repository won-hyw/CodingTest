arr = [1, 4, 2, 3]

reversed_arr = [0] * len(arr)

length = len(arr)

for i in range(length):
    reversed_arr[length -i-1] = arr[i]
