# Author:	Daggenthal
# Started:	05/13/2021 at 01:20
# Finished:	02/06/2022 at 20:39


# I created this as a tool to combine my Update.sh, and Software_Install.sh bash scripts. This was both to learn Python3, and to get rid of a shell-requirement, which this took me around 2 hours to learn how to do.
# I started this around 01:20, and finished it at 03:23.
# This tooks me lots of Googling. I learned about sys, subprocess, and platform to grab the things that I need. While I can read this and know what it does;
# I need to re-do it a few more times to burn it into memory.

##########################################################################################################################################################################################################################################################################################################################################

import sys, subprocess, functions									# This imports the required utilities for Python 3 to run this script.

try:											# This allows us to exit the program with 'CTRL+C' or 'CTRL+D' without spitting out errors / nonsense.
	while True:									# The program starts out with a loop so it doesn't exit / crash instantly when a non-supported 
##########################################################################################################################################################################################################################################################################################################################################	
		
		subprocess.run(['clear'], shell=True)					# Clears the Terminal.
		print('\t Welcome to Astol! What would you like to do? \n') 		# Outputs to the shell.
		print('\t 1: Update')
		print('\t 2: Install software')						# Breaks a line to ready for user input.
		print('\t 3: Remove software')
		print('\t 4: Exit \n')
		
		response = str(input('\t Please input your selection as a number: '))	# Sets up a string-variable called "response" to get user input for it to run functions based off of what was inputted.
		subprocess.run(['clear'], shell=True)					
		if response == '1':							# Checks to see what was inputted by the User. If "1" is inputted, the update() function is called, and once it's done, exits. If an invalid input is entered, nothing happens.
			functions.update()
			functions.return_to_loop()
		elif response == '2':
			functions.software()
		elif response == '3':
			functions.remove()
		elif response == '4':
			sys.exit()
except KeyboardInterrupt:								# This checks for 'CTRL+C' or 'CTRL+D', whichever comes first, and clears the Terminal, then prints out a statement.
	subprocess.run(['clear'], shell=True)
	print('User has purposefully interrupted the execution of Astol.')
	
	
	
#############################################################################################################################################################-Edit History-##############################################################################################################################################################

# 05/13/2021: Fixed the issue of not being able to read the string output of "subprocess.getoutput()" on different Distros. This is what caused me to spend a few extra hours on this as it kept searching for Debian's output and trying those commands. Now, by searching for the output of 'cat /etc/os-release' directly, I can apply it for the other distros :)
# 05/20/2021: Added 'Try:' and 'except KeyboardInterrupt:' to output a message when a user ctrl+c's the program to abruptly end the program. Instead of displaying the source, it just prints a message instead.
# 07/20/2021: Changed the output of the NVIDIA function to properly display that it has only been tested on Ubuntu 20.04. Support for other OSs is a simple fix, but currently untested, but most other OSs automatically install the NVIDIA drivers... most of the time. Also, added tabs for the output of some of the terminal responses in order to comply with the standard I've hereby set, therefore it all looks "similar".
# 02/06/2022: I honestly forgot to update this changelog. Major changes include: Splitting my definitions up into a file called "funcitons.py", adding a "remove" function, fix the process of finding if Debian / Ubuntu (which started throwing errors on some specific derivatives), added a return_to_loop function, and learned about "break".
