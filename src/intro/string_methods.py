my_string='salvi is awesome'
print(my_string.islower())
print("the guy has {} balloons".format(27))
animal = "dog"
action = "bite"
print("Does your {} {}?".format(animal, action))
#copitalise() incode() format() isalpha() istitle() casefold() endswith() isprintable() join() count() find() isalnum()
#format_map() isdecimal() isnumeric() isupper() center() expandtabs() index() isdigit() isidentifier() isspace() ljust()



# Browse the complete list of string methods at:
# https://docs.python.org/3/library/stdtypes.html#string-methods
# and try them out here



new_str = "The cow jumped over the moon."
print(new_str.split())
print(new_str.split(' ', 3))

print(new_str.split('.'))
print(new_str.split(None, 3))


# What is the length of the string variable verse?
# What is the index of the first occurrence of the word 'and' in verse?
# What is the index of the last occurrence of the word 'you' in verse?
# What is the count of occurrences of the word 'you' in the verse?


verse = "If you can keep your head when all about you\n  Are losing theirs and blaming it on you,\nIf you can trust yourself when all men doubt you,\n  But make allowance for their doubting too;\nIf you can wait and not be tired by waiting,\n  Or being lied about, don’t deal in lies,\nOr being hated, don’t give way to hating,\n  And yet don’t look too good, nor talk too wise:"


# Use the appropriate functions and methods to answer the questions above
# Bonus: practice using .format() to output your answers in descriptive messages!