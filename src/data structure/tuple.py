#immutable ordered seauence of elements 

location = (13.4125, 103.866667)
print("Latitude:", location[0])
print("Longitude:", location[1])
#tuple used when you have values that are so closly related and will be eventually used together 

#tuple unpacking
dimensions = 52, 40, 100
length, width, height = dimensions
print("The dimensions are {} x {} x {}".format(length, width, height))

#whats the output 
tuple_a = 1, 2
tuple_b = (1, 2)

print(tuple_a == tuple_b)
print(tuple_a[1])