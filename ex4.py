# Exercise 4: Variables and Names

# Cars Available
cars = 100

# How Many Passengers Can Each Car Take
space_in_a_car = 4.0

# How Many Drivers Are Working Today
drivers = 30

# Passenger Quantity
passengers = 90

# How Many Cars Stay in Parking Today
cars_not_driven = cars - drivers

# How Many Cars would be On the Road
cars_driven = drivers

# Full Capacity of All the Cars on the Road Today
carpool_capacity = cars_driven * space_in_a_car


average_passengers_per_car = passengers / cars_driven


# When using print, remember to seperate the elements with comas
print "There are", cars, "cars available."
print "There are only", drivers, "drivers available."
print "There will be", cars_not_driven, "empty cars today."
print "We can transport", carpool_capacity, "people today."
print "We have", passengers, "to carpool today."
print "We need to put about", average_passengers_per_car, "in each car."
