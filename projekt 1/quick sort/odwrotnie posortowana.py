import datetime
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

 
array = [96, 84, 73, 63, 57, 50, 43, 37, 27, 15]
n = len(array)
start = datetime.datetime.now()
quickSort(array, 0, n-1)
print(array)
end = datetime.datetime.now()
elapsed = end - start
print(elapsed)