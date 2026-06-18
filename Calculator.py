def user_interface():
	import time
	print("<<-------------------------Calculator--------------------------------->>")
	print("""instructions:
	1. choose mode to calculate.
	2. if you want to exit from a mode type ' exit ' .
	3. type ' help ' if you dont understand. """)
	time.sleep(1)
def user_ui():
	options = [1, 2, 3]
	print("-----------------------------------------------------------")
	request = input("""What do you want to do?  
	  1. Basic calculator
	  2. find circumference
	  3. find Square  
	  Type the respective numbers to Continue.... """)
	if request == "1" :
		calculator()
	elif request == "2" :
		circumference()
	elif request == "3" :
		square()
	elif request == "help":
		user_interface()
	elif request not in options:
		print("invalid mode selected")
def calculator():
	import time
	running = True
	operations = ["+", "-", "*", "/"]
	while running:
   # first number
		print("------------------------CALCULATOR-----------------------------------")
		num_1 = input("Enter the first number: ")
		if num_1 == "exit":
			running = False
			continue
		elif num_1 == "help":
			user_interface()
			continue
	
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
def circumference():
	import math
	import time
	constant = 2
	pi_constant = 3.1415
	run = True 
	while run:
		print("-----------------------CIRCUMFERENCE------------------------------------")
		radius = input("Enter the RADIUS of the Circle: ")
		if radius == "exit":
			run = False
			continue
		elif radius == "help":
			continue
	
		if radius.isdigit():
			radius_int = int(radius)
		else:
			print("-----------------------------------------------------------")
			print("invalid input!")
			continue
		calculation_of_circumference = constant * pi_constant * radius_int
		print("-----------------------------------------------------------")
		print(f'The circumference is " {calculation_of_circumference} "')
		time.sleep(1)
def square():
	import time
	operate = True
	while operate:
		print("-------------------------SQUARE----------------------------------")
		square = input("Enter the number you want to square: ")
		if square == "exit":
			operate = False
			continue
		elif square == "help":
			continue

		if square.isdigit():
			square_int = int(square)
		else:
			print("-----------------------------------------------------------")
			print("invalid input!")
			continue
    # square calculation
		square_calculation = square_int * square_int
		print("-----------------------------------------------------------")
		print(f'The SQUARED number is " {square_calculation} ". ')
		time.sleep(1)
def main(permission):
	access = permission
	if access:
		user_interface()
		while access:
			user_ui()
	else:
		print("permission was not given....")

main(True)
	
	
