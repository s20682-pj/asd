import datetime
def bubbleSort(array):
    n = len(array)
 
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]

array = [5, 39, 47, 1, 47, 33, 59, 2, 8, 20]
 
start = datetime.datetime.now()
bubbleSort(array)
print(array)
end = datetime.datetime.now()
elapsed = end - start
print(elapsed)