import TestDataGen


def bubble_sort(arr):
    sort = False
    n = -1
    while not sort:
        sort = True
        for j in range(len(arr) -2,n,-1):
            if arr[j] < arr[j+1]:
                arr[j],arr[j+1] = arr[j+1],arr[j]
                sort = False
        n=n+1
    return arr
a = TestDataGen.random_int_list(1,100,50)
print(bubble_sort(a))