# Exercise 4: Variables and Names

#total available cars
cars = 100

#how many people can seat in car
space_in_a_car = 4.0

#total number of available drivers
drivers = 30

#total number of passengers
passengers = 90

#unused cars
cars_not_driven = cars - drivers

# number of used cars
cars_driven = drivers

#total number passengers can travel today
carpool_capacity = cars_driven * space_in_a_car

#average passengers per car
average_passengers_per_car = passengers / cars_driven

print("There are", cars, "cars available.")
print("There are only", drivers, "drivers available.")
print("There will be", cars_not_driven, "empty cars today.")
print("We can transport", carpool_capacity, "people today.")
print("We have", passengers, "to carpool today.")
print("We need to put about", average_passengers_per_car,
      "in each car.")