import time

running = True
operations = ["+", "-", "*", "/"]
def calc():
	while running:
# first number
		print("-----------------------------------------------------------")
		num_1 = input("Enter the first number: ")
		if num_1.isdigit():
			num_1_int = int(num_1)
		else:
			print("invalid input....")
			continue
	
		
# operators
		print("-----------------------------------------------------------")
		operator_input = input("Enter the Operation: ")
		if operator_input not in operations:
			print("invalid operator!")
			continue
	
# second number	
		print("-----------------------------------------------------------")
		num_2 = input("Enter the second number: ")
		if num_2.isdigit():
			num_2_int = int(num_2)
		else:
			print("invalid input....")
			continue
	# calculation
	  # addition
		if operator_input == "+":
			calculation = num_1_int + num_2_int
			print(f'The result is " {calculation} ".')
			time.sleep(1)
		# subtraction	
		if operator_input == "-":
			calculation = num_1_int - num_2_int
			print(f'The result is " {calculation} ".')
			time.sleep(1)
		# multiplication	
		if operator_input == "*":
			calculation = num_1_int * num_2_int
			print(f'The result is " {calculation} ".')
			time.sleep(1)
		#division	
		if operator_input == "/":
			calculation = num_1_int / num_2_int
			print(f'The result is " {calculation} ".')
			time.sleep(1)
			
calc()
	
	
