
y=25>58 #false
age=25
marks=70
discipline=40
is_acccepted=(not(age<20) and(marks>60 or discipline>50))
print(is_acccepted)

# Quiz: Which is denser, Rio or San Francisco?
# Try comparison operators in this quiz! This code calculates the population densities of Rio de Janeiro and San Francisco.

# Write code to compare these densities. Is the population of San Francisco more dense than that of Rio de Janeiro? Print True if it is and False if not.

sf_population, sf_area = 864816, 231.89
rio_population, rio_area = 6453682, 486.5

san_francisco_pop_density = sf_population/sf_area
rio_de_janeiro_pop_density = rio_population/rio_area
# Write code that prints True if San Francisco is denser than Rio, and False otherwise


#Why do you think Python uses == for checking equality rather than =?