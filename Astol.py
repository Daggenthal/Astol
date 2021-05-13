# Created as a tool to combine my Update.sh, and Software_Install.sh bash scripts. This was both to learn Python3, and to get rid of a shell-requirement, which this took me around 2 hours to learn how to do.
# I started this around 1:20AM, and finished it at 3:23AM.
# This tooks me lots of Googling. I learned about sys, subprocess, and platform to grab the things that I need. While I can read this and know what it does;
# I need to re-do it a few more times to burn it into memory.

import sys, subprocess							# This imports the required utilities for Python 3 to run this script.

while True:								# The program starts out with a loop so it doesn't exit / crash instantly when a non-supported string (input) is, well, inputted.
	def update():							# Defines a function called update.
	
		OS = subprocess.getoutput(['cat /etc/os-release'])	# Defines OS, then runs a command located in (['']) + grabs the output of said command and stores it into the variable called OS.
	
		if OS.find('debian'):					# Scans the string that's outputted by the command and searches for what's in '', so in this case it's searching for the word "debian".
			subprocess.run(['sudo apt update -y && sudo apt upgrade -y --allow-downgrades && sudo apt autoremove -y'], shell=True)	
		elif OS.find('fedora'):
			subprocess.run(['sudo dnf update -y && sudo dnf upgrade -y'], shell=True)
		elif OS.find('arch'):
			subprocess.run(['sudo pacman -Syu'], shell=True) # Runs a command through the shell based off of what is returned by the string. In this instance, it runs "sudo pacman -Syu" because the scanned string contained the word "arch" in it.
		elif OS.find('opensuse'):
			subprocess.run(['sudo zypper refresh && sudo zypper update -y'], shell=True)

	def software():
	
		OS = subprocess.getoutput(['cat /etc/os-release'])
		
		if OS.find("debian"):
			subprocess.run(['clear && printf "Please input the software you would like to install: " && read install && sudo apt install -y $install'], shell=True)
		elif OS.find('fedora'):
			subprocess.run(['clear && printf "Please input the software you would like to install: " && read install && sudo dnf install -y $install'], shell=True)
		elif OS.find('arch'):
			subprocess.run(['clear && printf "Please input the software you would like to install: " && read install && sudo pacman -S --noconfirm $install'], shell=True)
		elif OS.find('opensuse'):
			subprocess.run(['clear && printf "Please input the software you would like to install: " && read install && sudo zypper install -y $install'], shell=True)
	
	subprocess.run(['clear'])						# Clears the Terminal.
	print('Welcome to my script panel! What would you like to do? \n') 	# Outputs to the shell.
	print("1. Update")
	print('2. Install software')						# Breaks a line to ready for user input.
	print('3. Exit \n')
	
	response = str(input('Please input your selection as a number: '))	# Sets up a string-variable called "response" to get user input for it to run functions based off of what was inputted.
	subprocess.run(['clear'])					
	if response == '1':							# Checks to see what was inputted by the User. If "1" is inputted, the update() function is called, and once it's done, exits. If an invalid input is entered, nothing happens.
		update()
		sys.exit()							# Exits the program, otherwise the loop will continuously loop through the entire thing, recursively. 
	elif response == '2':
		software()
		sys.exit()
	elif response == '3':
		sys.exit()
