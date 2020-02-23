#A dictionary is a mutable data type that stores mappings of unique keys to values
elements = {"hydrogen": 1, "helium": 2, "carbon": 6}
print(elements["helium"])  # print the value mapped to "helium"
elements["lithium"] = 3  # insert "lithium" with a value of 3 into the dictionary
iscarbom=("carbon" in elements)
print(elements.get("dilithium")) #return none if element is not in dictionary
print(iscarbom is not None)
elements.get('dilithium')
None
elements['dilithium'] #keyError
elements.get('kryptonite', 'There\'s no such element!')
"There's no such element!"

# Test the code here if you'd like
a = [1, 2, 3]
b = a
c = [1, 2, 3]
print(a == b)
print(a is b)
print(a == c)
print(a is c)

animals = {'dogs': [20, 10, 15, 8, 32, 15], 'cats': [3,4,2,8,2,4], 'rabbits': [2, 3, 3], 'fish': [0.3, 0.5, 0.8, 0.3, 1]}
print(animals[3])