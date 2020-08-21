array = [1, 2, 3, 4, 5, 6]
k = 5


def divisible(array, k):
    counter = 0
    length = len(array)
    for i in range(length):
        for j in range(i + 1, length):
            if (array[i] + array[j]) % k == 0:
                counter += 1
    print(counter)


a = divisible(array, k)
