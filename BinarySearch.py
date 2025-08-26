import time

import TestDataGen


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

if __name__ == "__main__":
    arrN = TestDataGen.random_int_list(0,95020,5990)
    arrN.sort(reverse=1)
    print(
        binary_search(arrN,int(input("bSearch What")))
    )
