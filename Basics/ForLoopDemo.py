
list1 = [0, 1, 2, 3, 4]
i = iter(list1)
while True:
    try:
        e = next(i)
        print(e)
    except StopIteration:
        break


for i in list1:
    print(i)

