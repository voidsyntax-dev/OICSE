mountains = ['Everest', 'K2', 'Kangchenjunga', 'Lhotse', 'Makalu']

print(mountains)
print(len(mountains))
print(mountains[0])
print(mountains[-1])

mountains.append('Cho Oyu')
print(mountains)

mountains.insert(2, 'Dhaulagiri')
print(mountains)

mountains.remove('K2')
print(mountains)

popped = mountains.pop()
print(popped)
print(mountains)

popped = mountains.pop(1)
print(popped)
print(mountains)

del mountains[0]
print(mountains)

mountains.sort()
print(mountains)

mountains.sort(reverse=True)
print(mountains)

print(sorted(mountains))
print(mountains)

mountains.reverse()
print(mountains)

mountains.reverse()
print(mountains)

print(mountains.index('Makalu'))
print(mountains.count('Everest'))

mountains.clear()
print(mountains)