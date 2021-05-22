import datetime
from numpy import random
import sys
sys.setrecursionlimit(55000)

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
        
def bubbleSort(array):
    n = len(array)
 
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]
                
def partition(array, p, r):
    pivot = array[r]
    smaller = p 
    
    for i in range(p, r):
        if array[i] <= pivot:
            array[smaller], array[i] = array[i], array[smaller]
            smaller = smaller + 1
            
    array[smaller], array[r] = array[r], array[smaller]

    return smaller

def quickSort(array, p, r):
    if p < r:
        q = partition(array, p, r)
        quickSort(array, p, q-1)
        quickSort(array, q+1, r)


array=random.randint(100, size=(20000))
array.sort()
reverse_array = array[::-1]
array2 = reverse_array.copy()
array3 = reverse_array.copy()

start1 = datetime.datetime.now()
heap_sort(array)
end1 = datetime.datetime.now()
elapsed1 = end1 - start1
print(elapsed1)

n = len(array3)
start3 = datetime.datetime.now()
quickSort(array3, 0, n-1)
end3 = datetime.datetime.now()
elapsed3 = end3 - start3
print(elapsed3)

start2 = datetime.datetime.now()
bubbleSort(array2)
end2 = datetime.datetime.now()
elapsed2 = end2 - start2
print(elapsed2)
