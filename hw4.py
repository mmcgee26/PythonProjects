#create an empty queue
d = []

#add 1 to the rear
d.append(1)

#add 2 to the rear
d.append(2)

#add 3 to the front
d.insert(0, 3)

#remove an item from the rear and print the value
print(d.pop())

#remove an item from the front and print the value
print(d.pop(0))