def sortTwo(array):
    for i in range(len(array)-1):
        if array[i] < array[i+1]:
            bigger = array[i+1]
            smaller = array[i]
    j = 0
    for i in range(len(array)):
        if array[i] < bigger:
            array[i], array[j] = array[j], array[i]
            j = j+1
array = [5,5,5,5,6,5,6,6,6,5,6,6,5,6,6,5,6,5,6,5,6,6,5,6]
sortTwo(array)
print(array)

#Jest to alogrytm o złożoności liniowej O(n)