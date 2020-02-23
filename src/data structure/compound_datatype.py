elements = {"hydrogen": {"number": 1,
                         "weight": 1.00794,
                         "symbol": "H"},
              "helium": {"number": 2,
                         "weight": 4.002602,
                         "symbol": "He"}}
helium = elements["helium"]  # get the helium dictionary
hydrogen_weight = elements["hydrogen"]["weight"]  # get hydrogen's weight
oxygen = {"number":8,"weight":15.999,"symbol":"O"}  # create a new oxygen dictionary 
elements["oxygen"] = oxygen  # assign 'oxygen' as a key to the elements dictionary
print('elements = ', elements)




#This is how I added values to the elements dict. The syntax for adding elements to nested data structures is about the same as it is for reading from them.


elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True

#List are sortable, you can add an item to a list with .append and list items are always indexed with numbers starting at 0.



#Sets are not ordered, so the order in which items appear can be inconsistent and you add items to sets with .add. Like dictionaries and lists, sets are mutable.

# You cannot have the same item twice and you cannot sort sets. For these two properties a list would be more appropriate


#Each item in a dictionary contains two parts (a key and a value), the items in a dictionary are not ordered, and we have seen in this lesson examples of nested dictionaries.

#Because dictionaries are not ordered, they are not sortable. And you do not add items to a dictionary with .append.

elements = {'hydrogen': {'number': 1, 'weight': 1.00794, 'symbol': 'H'},
            'helium': {'number': 2, 'weight': 4.002602, 'symbol': 'He'}}

elements['hydrogen']['is_noble_gas'] = False
elements['helium']['is_noble_gas'] = True