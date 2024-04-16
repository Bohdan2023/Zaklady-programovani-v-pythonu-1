import random

def selection_sort(arr):
    n = len(arr)
    for i in range(n):
        
        min_index = i
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j
        
        arr[i], arr[min_index] = arr[min_index], arr[i]
    
    return arr

# tady můžeme změnit limit
arr = [random.randint(1, 10000) for _ in range(10000)]
print("pocatecni:", arr)

sorted_arr = selection_sort(arr)
print("konecny:", sorted_arr)
