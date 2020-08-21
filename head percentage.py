import random
head = 0
tail = 0
for i in range(1,1000000):
    outcome = random.randint(0,1)
    if outcome == 0:
        head += 1
    else:
        tail += 1

head_per = (head/1000000) * 100
tail_per= (tail/1000000) * 100

print("Percentage of heads are:{}%".format(head_per))
print("Percentage of tails are:{}%".format(tail_per))
