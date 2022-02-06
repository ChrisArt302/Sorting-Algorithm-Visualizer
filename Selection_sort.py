import time

def selectionSort(data, drawData, timeTick):
    n = len(data)

    # traverse through all array elements
    for i in range(n):
        # find the minimum element in array
        min_idx = i # variable to store minimum value


        # traverse through the array to compare values
        # j will begin at index 1 in the array
        for j in range(i+1, n):
            # search for the smallest number by comparing value at index 0 (min_idx) with value at
            # index + 1 (j). If former is greater, minimum value is now j
            if data[min_idx] > data[j]:
                min_idx = j

        # create sorted array by swapping the smallest value to the beginning
        data[i], data[min_idx] = data[min_idx], data[i]

        drawData(data, ['green' if x == i else 'red' for x in range(len(data))])
        time.sleep(timeTick)
    # once sorting is done, color array green
    drawData(data, ['green' for x in range(len(data))])
