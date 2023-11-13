def func(arr, low, high, k):
    if low<=high:
        mid = (low+high)//2
        if arr[mid] == k:
            return mid
        elif arr[mid] < k:
            return func(arr, mid+1, high, k)
        else:
            return func(arr, low, mid-1, k)
    else:
        return -1

class Solution:    
    def binarysearch(self, arr, n, k):

        pos = func(arr, 0, n-1, k)
        
        return pos
