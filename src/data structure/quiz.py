# Great job, you understand the properties of a tuple! A tuple is an immutable, ordered data structure that can be indexed and sliced like a list. Tuples are defined by listing a sequence of elements separated by commas, optionally contained within parentheses: ().
# Great job, you understand the properties of a set! A set is a mutable data structure - you can modify the elements in a set with methods like add and pop. A set is an unordered data structure, so you can't index and slice elements like a list; there is no sequence of positions to index with!

# One of the key properties of a set is that it only contains unique elements. So even if you create a new set with a list of elements that contains duplicates, Python will remove the duplicates when creating the set automatically 

# Correct! A set is defined with curly braces, {}, but it isn't the only data structure that does; dictionaries do as well! However, the difference is that a set is defined as a sequence of elements separated by commas:
# set_example = {element1, element2, element3}
# while a dictionary is defined as a sequence of key, value pairs marked with colons, separated by commas:
# dict_example = {key1: value1, key2: value2, key3: value3}.

# Note: if you define a variable with an empty set of curly braces like this: a = {}, Python will assign an empty dictionary to that variable. You can always use set() and dict() to define empty sets and dictionaries as well.

# Great job, you understand the properties of a dictionary! A dictionary is a mutable, unordered data structure that contains mappings of keys to values. Because these keys are used to index values, they must be unique and immutable. For example, a string or tuple can be used as the key of a dictionary, but if you try to use a list as a key of a dictionary, you will get an error.

# Correct! The error you saw was TypeError: unhashable type: 'list'. In Python, any immutable object (such as an integer, boolean, string, tuple) is hashable, meaning its value does not change during its lifetime. This allows Python to create a unique hash value to identify it, which can be used by dictionaries to track unique keys and sets to track unique values. This is why Python requires us to use immutable datatypes for the keys in a dictionary.

# The lists used in the code above are NOT immutable, and thus cannot be hashed and used as dictionary keys. Can you try modifying the datatype of the keys in the dictionary above to make the code run without errors? Hint: What other data structure can you use to store a sequence of values and is immutable?


# Quiz: Count Unique Words
# Your task for this quiz is to find the number of unique words in the text. In the code editor below, complete these three steps to get your answer.

# Split verse into a list of words. Hint: You can use a string method you learned in the previous lesson.
# Convert the list into a data structure that would keep only the unique elements from the list.
# Print the length of the container.

verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# split verse into list of words
verse_list =
print(verse_list, '\n')

# convert list to a data structure that stores unique elements
verse_set =
print(verse_set, '\n')

# print the number of unique words
num_unique = 
print(num_unique, '\n')


verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, '\n')

# split verse into list of words
verse_list = verse.split(' ')
print(verse_list, '\n')

# convert list to a data structure that stores unique elements
verse_set =set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set)
print(num_unique, '\n')

verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = 
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = 
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = 

# get the first element in the sorted list of keys
print()

# find the element with the highest value in the list of keys
print() 



#solutions 

verse = "if you can keep your head when all about you are losing theirs and blaming it on you   if you can trust yourself when all men doubt you     but make allowance for their doubting too   if you can wait and not be tired by waiting      or being lied about  don’t deal in lies   or being hated  don’t give way to hating      and yet don’t look too good  nor talk too wise"
print(verse, "\n")

# split verse into list of words
verse_list = verse.split()
print(verse_list, '\n')

# convert list to set to get unique words
verse_set = set(verse_list)
print(verse_set, '\n')

# print the number of unique words
num_unique = len(verse_set)
print(num_unique)

verse_dict =  {'if': 3, 'you': 6, 'can': 3, 'keep': 1, 'your': 1, 'head': 1, 'when': 2, 'all': 2, 'about': 2, 'are': 1, 'losing': 1, 'theirs': 1, 'and': 3, 'blaming': 1, 'it': 1, 'on': 1, 'trust': 1, 'yourself': 1, 'men': 1, 'doubt': 1, 'but': 1, 'make': 1, 'allowance': 1, 'for': 1, 'their': 1, 'doubting': 1, 'too': 3, 'wait': 1, 'not': 1, 'be': 1, 'tired': 1, 'by': 1, 'waiting': 1, 'or': 2, 'being': 2, 'lied': 1, 'don\'t': 3, 'deal': 1, 'in': 1, 'lies': 1, 'hated': 1, 'give': 1, 'way': 1, 'to': 1, 'hating': 1, 'yet': 1, 'look': 1, 'good': 1, 'nor': 1, 'talk': 1, 'wise': 1}
print(verse_dict, '\n')

# find number of unique keys in the dictionary
num_keys = len(verse_dict)
print(num_keys)

# find whether 'breathe' is a key in the dictionary
contains_breathe = "breathe" in verse_dict
print(contains_breathe)

# create and sort a list of the dictionary's keys
sorted_keys = sorted(verse_dict.keys())

# get the first element in the sorted list of keys
print(sorted_keys[0])

# find the element with the highest value in the list of keys
print(sorted_keys[-1]) 