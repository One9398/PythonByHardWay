


cars = 100
space_in_a_car = 4
drivers = 30
passenger = 90
cars_not_driver = cars - drivers
cars_drivers = drivers
carpool_capacity = cars_drivers * space_in_a_car
average_passenger_per_car = passenger / cars_drivers

print "there are ", cars, "cars"
print "there are only", drivers, "drivers avaible"
print "there will be", cars_not_driver, "empty cars today"
print "we have ", passenger, "passengers to carpool today"
print "we need to put about", average_passenger_per_car, "in each car"
