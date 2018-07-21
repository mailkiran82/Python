from functools import reduce
list1 = [x+1 for x in range(0, 5)]
print(list1)

list1 = [str(x) for x in range(0, 5)]
print(list1)

list1 = list(map(lambda x: x+1, range(1, 5)))
print(list1)

mysum = reduce(lambda x, y: x+y, list1)
print(mysum)
print(sum(list1))

list1 = list(filter(lambda x: x%2 == 0, range(0, 5)))
print(list1)

for i, j in zip(range(0, 5), range(10, 15)):
    print(i, j)

for i, e in enumerate(range(100, 105)):
    print(i, e)
