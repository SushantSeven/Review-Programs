# i/p : [ 22, 4 , 1 , 77 , 38 , 9 ,  5 , 11 , 44 ]
# o/p : [ 1 , 77 , 22 , 4 , 5 , 11, 38 , 9 , 44 ]

arr = input().split()
result_arr = list()

for i in range(0, len(arr) - len(arr) % 4, 4):
    result_arr.extend(arr[i+2:i+4])  # Append the 3rd and 4th elements
    result_arr.extend(arr[i:i+2])    # Append the 1st and 2nd elements

result_arr.extend(arr[len(arr) - len(arr) % 4:])

print(*result_arr)
