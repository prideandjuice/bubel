def bubble_sort(arr):
    n = len(arr)
    for i in range(n):
        already_sorted = True
        for j in range(n-i-1):
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]
                already_sorted = False
        if already_sorted:
            break 
    return arr

# Contoh array yang akan diurutkan
arr = [26,54,17,93,77,31,44,55,20]
bubble_sort(arr)
print(arr)