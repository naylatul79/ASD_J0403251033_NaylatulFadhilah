def quickSort(data):
    quickSortHelper(data,0,len(data)-1)

def quickSortHelper(data,first,last):
    if first < last:
        splitpoint = partition(data,first,last)

        quickSortHelper(data,first,splitpoint-1)
        quickSortHelper(data,splitpoint+1,last)

def partition(data,first,last):
    pivotvalue = data[first]

    leftmark = first + 1
    rightmark = last

    done = False
    while not done:

        # descending
        while leftmark <= rightmark and data[leftmark] >= pivotvalue:
            leftmark = leftmark + 1

        while data[rightmark] <= pivotvalue and rightmark >= leftmark:
            rightmark = rightmark - 1

        if rightmark < leftmark:
            done = True
        else:
            temp = data[leftmark]
            data[leftmark] = data[rightmark]
            data[rightmark] = temp

    temp = data[first]
    data[first] = data[rightmark]
    data[rightmark] = temp

    return rightmark


data = [43, 76, 12, 89, 33, 57, 98, 22, 68, 9]

print("Data awal:", data)

quickSort(data)

print("Data setelah diurutkan (descending):", data)

print("5 nilai tertinggi:", data[:5])

print("Kandidat yang lolos:")
for i in range(len(data[:5])):
    print("Kandidat dengan nilai:", data[i])