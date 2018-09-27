#Program to calculate Fibonacci series till a user entered number
fibonacci_limit = input("Please enter the number till which you want to see Fibonacci Series\n")
first_num = 0
second_num = 1
print(first_num)
print(second_num)
while fibonacci_limit > 0:
	show = first_num + second_num
	print(show)
	first_num = second_num
	second_num = show
	fibonacci_limit -= 1


	

