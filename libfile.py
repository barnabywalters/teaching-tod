# coding: utf-8


def say_hello(target=None):
	if target is None:
		return "Hello"
	elif isinstance(target, list):
		return "Hello {}".format(' and '.join(target))
	else:
		return "Hello, {}".format(target)


if __name__ == '__main__':
	# Tests

	print "\n\nTesting “say_hello” without arguments:"
	expected = 'Hello'
	actual = say_hello()
	if actual == expected:
		print " -> Success! Calling say_hello with no argument returns Hello"
	else:
		print " -> Failure! Calling say_hello with no argument returns {} when it was supposed to return {}".format(actual, expected)


	print "\n\nTesting “say_hello” with an argument:"
	expected = 'Hello, Tod'
	actual = say_hello('Tod')
	if actual == expected:
		print " -> Success! Calling say_hello with “Tod” returns {}".format(expected)
	else:
		print " -> Failure! Calling say_hello with “Tod” returns {} when it was supposed to return {}".format(actual, expected)


	print "\n\nTesting “say_hello” with multiple arguments:"
	arguments = ['Tod', 'Barnaby']
	expected = 'Hello Tod and Barnaby'
	actual = say_hello(arguments)
	if actual == expected:
		print " -> Success! Calling say_hello with {} returns {}".format(arguments, expected)
	else:
		print " -> Failure! Calling say_hello with {} returns {} when it was supposed to return {}".format(arguments, actual, expected)
