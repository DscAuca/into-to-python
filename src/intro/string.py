print("hello world") 
print('hello world')
print('"i think you\'re aweosme tho"')
print('this is "going to work" as i said')
name='salvi'
print('welcome '+ name +' you\'re awesome')
print(3*('i repeat you\'re  awesome '))
print(len('aesome shit')/len(name))
print(name[0])

# Quiz: Fix the Quote
# The line of code in the following quiz will cause a SyntaxError, thanks to the misuse of quotation marks. First run it with Test Run to view the error message. Then resolve the problem so that the quote (from Henry Ford) is correctly assigned to the variable ford_quote.

# TODO: Fix this string!
ford_quote = 'Whether you think you can, or you think you can't--you're right.'



# We’ve already seen that the type of objects will affect how operators work on them. What will be the output of this code?
coconut_count = "34"
mango_count = "15"
tropical_fruit_count = coconut_count + mango_count
print(tropical_fruit_count)


# Quiz: Write a Server Log Message
# In this programming quiz, you’re going to use what you’ve learned about strings to write a logging message for a server.

# You’ll be provided with example data for a user, the time of their visit and the site they accessed. You should use the variables provided and the techniques you’ve learned to print a log message like this one (with the username, url, and timestamp replaced with values from the appropriate variables):

# Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20.

# Use the Test Run button to see your results as you work on coding this piece by piece.

username = "Kinari"
timestamp = "04:50"
url = "http://petshop.com/pets/mammals/cats"

# TODO: print a log message using the variables above.
# The message should have the same format as this one:
# "Yogesh accessed the site http://petshop.com/pets/reptiles/pythons at 16:20."



# Quiz: len()
# Use string concatenation and the len() function to find the length of a certain movie star's actual full name. Store that length in the name_length variable. Don't forget that there are spaces in between the different parts of a name!
given_name = "William"
middle_names = "Bradley"
family_name = "Pitt"

name_length = #todo: calculate how long this name is

# Now we check to make sure that the name fits within the driving license character limit
# Nothing you need to do here
driving_license_character_limit = 28
print(name_length <= driving_license_character_limit)

# We've just used the len function to find the length of strings. What does the len function return when we give it the integer 835 instead of a string?

#835
#error
#3