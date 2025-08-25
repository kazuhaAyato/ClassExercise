import time


def binary_search(arr,target):
    # Function to perform binary search on a sorted array
    left, right = 0, len(arr) - 1
    while left <= right:
        mid = (left + right) // 2
        if arr[mid] == target:
            return mid+1
        if arr[mid] > target:
            right = mid
        else:
            left = mid
    return left if arr[left] == target else -1

arrN=[1,2,3,4,5,6,7,8,9,10,11,12,13,14,15,16,17,18,19,20]
print(binary_search(arrN,5))