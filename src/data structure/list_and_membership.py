list_of_random_things = [1, 3.4, 'a string', True]
print(list_of_random_things[2])
print(list_of_random_things[len(list_of_random_things) - 1]) #zero indexing
print(list_of_random_things[-4] )  

#Slice and Dice with Lists
print(list_of_random_things[1:3])
print(list_of_random_things[:3])
print(list_of_random_things[2:])

#in or not in 
print('this' in 'this is a string') #True
print('in' in 'this is a string') #True
print('isa' in 'this is a string') #False
print(5 not in [1, 2, 3, 4, 6]) #True
print(5 in [1, 2, 3, 4, 6]) #False

#mutability 

my_lst = [1, 2, 3, 4, 5]
my_lst[0] = 'one'
print(my_lst)
my_lst[0] = 1
print(my_lst)


#string object is imutable 
greeting = "Hello there"
print(greeting[0]) #H
#greeting[0] = 'M' #error

#both string and list are ordered but string is not mutable while object is mutable


# Quiz: List Indexing
# Use list indexing to determine how many days are in a particular month based on the integer variable month, and store that value in the integer variable num_days. For example, if month is 8, num_days should be set to 31, since the eighth month, August, has 31 days.

# Remember to account for zero-based indexing!

month = 8
days_in_month = [31,28,31,30,31,30,31,31,30,31,30,31]

# use list indexing to determine the number of days in month
print()

# Quiz: Slicing Lists
# Select the three most recent dates from this list using list slicing notation. Hint: negative indexes work in slices!

eclipse_dates = ['June 21, 2001', 'December 4, 2002', 'November 23, 2003',
                 'March 29, 2006', 'August 1, 2008', 'July 22, 2009',
                 'July 11, 2010', 'November 13, 2012', 'March 20, 2015',
                 'March 9, 2016']
                 
                 
# TODO: Modify this line so it prints the last three elements of the list
print(eclipse_dates)


##list methods

#len() max() min()
#sorted() returns a copy of a list in order from smallest to largest, leaving the list unchanged
print(sorted(eclipse_dates))
print(sorted(eclipse_dates,reverse=True))

#join method 
new_str = "\n".join(["fore", "aft", "starboard", "port"])
print(new_str)

#append
letters = ['a', 'b', 'c', 'd']
letters.append('z')
print(letters)