# 9.Given an integer array, find k'th smallest element in the array where k is a positive integer less than or equal to the length of array.

# Input : [7, 4, 6, 3, 9, 1], k = 3
# Output: 4
# Explanation: The 3rd smallest array element is 4

# Input : [1, 5, 2, 2, 2, 5, 5, 4], k = 5
# Output: 4
# Explanation: The 5th smallest array element is 4

def mini_num(array, k):
    if k <= len(array) and k > 0:
        for i in range(k-1):
            array.remove(min(array))
        print(f"the {k}th minimum element is {min(array)}")
    else:
     print("Enter a valid k value")


if __name__ =="__main__":
    array = [1, 5, 2, 2, 2, 5, 5, 4]
    # array = [7, 4, 6, 3, 9, 1]
    print("the array is ",array)
    k = int(input("Enter the kth element: "))
    mini_num(array, k)


