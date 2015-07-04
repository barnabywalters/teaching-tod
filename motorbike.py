# coding: utf-8

from __future__ import division

b = {
	'fuel': 0,
	'mileage': 0,
	'is_started': False,
	'mpg': 75
}


def fill_up(bike):
	bike['fuel'] = 100
	return bike


def start(bike):
	if bike['fuel'] > 0:
		bike['is_started'] = True
	else:
		print "Cannot start bike"

	return bike


def drive(bike, distance):
	if bike['is_started']:
		bike['mileage'] += distance
		fuel_consumption = (1 / bike['mpg']) * distance
		bike['fuel'] -= fuel_consumption
	else:
		print "Cannot drive as bike is not started"
	return bike


print b['fuel']
start(fill_up(b))

drive(b, 37.5)
drive(b, 37.5)

print b
