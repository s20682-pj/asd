import datetime
def max_heapify(arr, n, i):
    largest = i
    left = 2 * i + 1
    right = 2 * i + 2
    
    if left < n and arr[left] > arr[i]:
        largest = left

    if right < n and arr[right] > arr[largest]:
        largest = right

    if i != largest:
        arr[i], arr[largest] = arr[largest], arr[i]
        max_heapify(arr, n, largest)

def build_max_heap(arr):
    n = len(arr) - 1
    for i in range((n // 2), -1, -1):
        max_heapify(arr, n, i)

def heap_sort(arr):
    build_max_heap(arr)
    n = len(arr) - 1
    for i in range(n, 0, -1):
        arr[i], arr[0] = arr[0], arr[i]
        max_heapify(arr, i,  0)

table = [5, 23, 34, 35, 54, 67, 71, 74, 84, 95]

start = datetime.datetime.now()
heap_sort(table)
print(table)
end = datetime.datetime.now()
elapsed = end - start
print(elapsed)