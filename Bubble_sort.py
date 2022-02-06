import time

# third parameter: passing in the select speed option
def bubbleSort(data, drawData, timeTick):
    n = len(data)

    # traverse through all array elements
    # for every element in the range of data, iterate through loop. Thus, e.g. 0, 1, 2, 3, 4 = 5 indexes.
    for i in range(n-1):
        # traverse the array from 0 to the last value
        for j in range(n-1):
            # swap elements if the former is greater than the latter
            if data[j] > data[j+1]:
                data[j], data[j + 1] = data[j+1], data[j]
                drawData(data, ['green' if x == j or x == j+1
                                else 'red' for x in range(len(data))])
                time.sleep(timeTick)
    # once sorting is done, call function
    drawData(data, ['green' for x in range(len(data))])



