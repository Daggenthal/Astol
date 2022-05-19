import sys, functions									# This imports the required utilities for Python 3 to run this script.

from subprocess import run

try:											# This allows us to exit the program with 'CTRL+C' or 'CTRL+D' without spitting out errors / nonsense.
	while True:									# The program starts out with a loop so it doesn't exit / crash instantly when a non-supported 	
		
		run(['clear'], shell=True)					# Clears the Terminal.

		print('\t Welcome to Astol! What would you like to do? \n') 		# Outputs to the shell.
		print('\t 1: Update')
		print('\t 2: Install software')						# Breaks a line to ready for user input.
		print('\t 3: Remove software')
		print('\t 4: Exit \n')
		
		response = str(input('\t Please input your selection as a number: '))	# Sets up a string-variable called "response" to get user input for it to run functions based off of what was inputted.

		run(['clear'], shell=True)

		if response == '1':							# Checks to see what was inputted by the User. If "1" is inputted, the update() function is called, and once it's done, exits. If an invalid input is entered, nothing happens.
			functions.update()
			functions.return_to_loop()
		elif response == '2':
			functions.software()
		elif response == '3':
			functions.remove()
		elif response == '4':
			sys.exit()
			
except KeyboardInterrupt:								# This checks for 'CTRL+C' or 'CTRL+D', whichever comes first, clears the Terminal, then prints out a statement.
	run(['clear'], shell=True)
	print('User has purposefully interrupted the execution of Astol.')
