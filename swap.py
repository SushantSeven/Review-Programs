# i/p : [ 22, 4 , 1 , 77 , 38 , 9 ,  5 , 11 , 44 ]
# o/p : [ 1 , 77 , 22 , 4 , 5 , 11, 38 , 9 , 44 ]

arr = input().split()
arr2 = list()

if len(arr)%4 == 0:
    for i in range(0,len(arr)-1,4):
        arr2.append(arr[i+2])
        arr2.append(arr[i+3])
        arr2.append(arr[i])
        arr2.append(arr[i+1])

else:
    for i in range(0,len(arr)-len(arr)%4,4):
            arr2.append(arr[i+2])
            arr2.append(arr[i+3])
            arr2.append(arr[i])
            arr2.append(arr[i+1])
    for i in range(len(arr2), len(arr)):
            arr2.append(arr[i])

print(*arr2)
