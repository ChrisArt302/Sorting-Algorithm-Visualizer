import time

# parameters: data array,
def merge_sort(data, drawData, timeTick):
    # parameters: data, 0 for left index, len(data) - 1 for right index, drawData, timeTick
    merge_sort_alg(data, 0, len(data)-1, drawData, timeTick)

# call algorithm. Parameters: data array, left and right index, drawData and timetick.
def merge_sort_alg(data, left, right, drawData, timeTick):
    # condition for recursion to stop;
    # left index has to be one smaller than the right index, if so continue dividing and calling itself
    if left < right:
        # get the middle index
        middle = (left + right) // 2
        # recursion: function calling itself
        # index is from left to middle; left side
        merge_sort_alg(data, left, middle, drawData, timeTick)
        # index is from middle+1 to right, the right side
        merge_sort_alg(data, middle+1, right, drawData, timeTick)
        # merge data and indexes from left to middle to right, and others
        merge(data, left, middle, right, drawData, timeTick)

# define merge function
def merge(data, left, middle, right, drawData, timeTick):
    drawData(data, getColorArray(len(data), left, middle, right))
    time.sleep(timeTick)

    leftPart = data[left:middle+1]
    rightPart = data[middle+1:right+1]

    L = 0
    R = 0

    for dataIdx in range(left, right+1):
        if L < len(leftPart) and R < len(rightPart):
            if leftPart[L] <= rightPart[R]:
                data[dataIdx] = leftPart[L]
                L +=1
            else:
                data[dataIdx] = rightPart[R]
                R += 1
        elif L < len(leftPart):
            data[dataIdx] = leftPart[L]
            L += 1
        else:
            data[dataIdx] = rightPart[R]
            R += 1

    # when finished sorting array, color it green
    drawData(data, ["green" if x >= left and x <= right else "white" for x in range(len(data))])
    time.sleep(timeTick)

def getColorArray(length, left, middle, right):
    # create an empty array
    colorArray = []

    # if working in current sublist
    for i in range(length):
        if i >= left and i <= right:
            if i <= middle:
                colorArray.append("red")
            else:
                colorArray.append("blue")
        # not working in the current array
        else:
            colorArray.append("white")

    return colorArray

