#import math


p=0
def linear_search(n,l):
    for i in l:
        if n==i:
            global p
       #     print(n,i)
            return True
        else:
            p=p+1

    return False


def binary_search(n,list):
    l=0
    u=len(list)-1
    while l<u:

        mid = int((l + u) / 2)
        if n==list[mid]:
            globals()['p']=mid
            return True
        elif n<list[mid]:
            u=mid-1
        else:
            l=mid+1
    return  False



list=[1,2,3,45,47,49,99,101]
n=451
'''
if search(n,list):
    print("Found at position ",p)
else:
    print("Not Found")

'''
if binary_search(n,list):
    print("Found at position ",p)
else:
    print("Not Found")


print(len(list))


def ternarySearch(arr, l, r, x):
    if (r >= l):
        mid1 = l + (r - l) // 3
        mid2 = mid1 + (r - l) // 3

        # If x is present at the mid1
        if arr[mid1] == x:
            return mid1

        # If x is present at the mid2
        if arr[mid2] == x:
            return mid2

        # If x is present in left one-third
        if arr[mid1] > x:
            return ternarySearch(arr, l, mid1 - 1, x)

        # If x is present in right one-third
        if arr[mid2] < x:
            return ternarySearch(arr, mid2 + 1, r, x)

        # If x is present in middle one-third
        return ternarySearch(arr, mid1 + 1, mid2 - 1, x)

    # We reach here when element is not present in array
    return -1