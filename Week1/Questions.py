########### Working with lists ##################

# # Create a list of numbers from 1-5
# mylist = [i for i in range(1, 6)]
# print(mylist)
#
# # Add an element on the end
# mylist.append(8)
# print(mylist)
#
# # Remove the first element
# mylist.pop(0)
# print(mylist)
#
# # Remove the last element
# mylist.pop()
# print(mylist)


########### Using dictionaries #################

# Create a dictionary consisting of a surnames as keys, and first names as values for members of The Beatles

keys = ['Mcartney', 'Harrison']
values = ['Paul', 'George']

mydict = dict(zip(keys, values))
print(mydict)

# Print all the keys
for key in mydict:
    print(key)

# Print all the values
for val in mydict.values():
    print(val)

# Try looking up some values for given keys and printing them

a = 'Harrison'

print(mydict.get(a))
