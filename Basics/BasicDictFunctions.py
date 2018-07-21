
d = {'a': 1, 'b': 5, 'c': 3, 'e': 4, 'd': 2}
print(d)
print(d.keys())

'''copy of the dictionary’s list of (key, value) pairs.'''
print(d.items())

'''
deprecated in Python 3
does not return a list. This is only dictionary item iterator object. That means less memory usage 
for i, v in d.iteritems():
    print(i,v)
'''

l1 = [1, 2, 3, 4, 5]
l2 = ['e', 'd', 'c', 'b', 'a']

d1 = dict(zip(l1, l2))
print(d1)

l1 = zip(l1, l2)
for i in l1:
    print(i)

l1 = list(sorted(d1.items(), key=lambda x: x[1]))
print(l1)

print(list(map(lambda x: x[0], d1.items())))
print(list(map(lambda x: x[1], d1.items())))