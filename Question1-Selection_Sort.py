def SelectionSort(arr):
    n = len(arr)
    for i in range(n-1):
        minIndex = i
        for j in range(i+1, n):
            if(arr[j] < arr[minIndex]):
                minIndex = j
        temp = arr[i]
        arr[i] = arr[minIndex]
        arr[minIndex] = temp
    

arr = [5,416,54,21,6135,15,741]
n = len(arr)
SelectionSort(arr)
for i in range(n):
    print(arr[i])