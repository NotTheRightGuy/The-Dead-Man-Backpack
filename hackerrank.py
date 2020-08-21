
def birthday(array, sum, length):
        var = 1
        ways = 0
        while var <= len(array)+1:
            value = 0
            for i in array[var:var+length]:
                value += i
                if value == sum:
                    ways += 1
            var += 1
        return ways

array = [4]
print(birthday(array,4,1))
