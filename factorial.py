#Code to calculate Factorial of the user entered integer

factorial_input = input("Please enter the number to calculate Factorial\n\n")
output = 1

while factorial_input >= 1:
	output *= factorial_input
	factorial_input -=1

print "The Factorial is {}".format(output)