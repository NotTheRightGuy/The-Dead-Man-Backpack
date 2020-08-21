
def rotatebyone(arr, n):
    temp = arr[0]
    for i in range(n - 1):
        arr[i] = arr[i + 1]
    arr[n - 1] = temp


def rotatearr(arr, d, n):
    for i in range(d):
        rotatebyone(arr, n)


arr = [1, 2, 3, 4, 5, 6, 7]
rotatearr(arr, 3, 7)
print(arr)


