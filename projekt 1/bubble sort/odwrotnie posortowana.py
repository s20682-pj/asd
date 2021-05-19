import datetime
def bubbleSort(array):
    n = len(array)
 
    for i in range(n):
        for j in range(0, n-i-1):
            if array[j] > array[j+1] :
                array[j], array[j+1] = array[j+1], array[j]

array = [96, 84, 73, 63, 57, 50, 43, 37, 27, 15]
 
start = datetime.datetime.now()
bubbleSort(array)
print(array)
end = datetime.datetime.now()
elapsed = end - start
print(elapsed)