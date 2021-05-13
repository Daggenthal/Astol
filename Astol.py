#Author:	Daggenthal
#Started:	05/13/2021 at 01:20
#Finished:	05/13/2021 at 03:23
#Edited:	05/13/2021 at 06:24 (Fixed issue of not being able to read the string output of "subprocess.getoutput()" on different Distros)


# I created this as a tool to combine my Update.sh, and Software_Install.sh bash scripts. This was both to learn Python3, and to get rid of a shell-requirement, which this took me around 2 hours to learn how to do.
# I started this around 01:20, and finished it at 03:23.
# This tooks me lots of Googling. I learned about sys, subprocess, and platform to grab the things that I need. While I can read this and know what it does;
# I need to re-do it a few more times to burn it into memory.

import sys, subprocess							# This imports the required utilities for Python 3 to run this script.

while True:								# The program starts out with a loop so it doesn't exit / crash instantly when a non-supported string (input) is, well, inputted.
	def update():							# Defines a function called update.
	
		OS = subprocess.getoutput(['cat /etc/os-release'])	# Defines OS, then runs a command located in (['']) + grabs the output of said command and stores it into the variable called
		#output, _ = OS.communicate()
		#p_status = OS.wait()
		 	
		if 'debian' in OS:					# Scans the string that's outputted by the command and searches for what's in '', so in this case it's searching for the word "debian".
			subprocess.run(['sudo apt update -y && sudo apt upgrade -y --allow-downgrades && sudo apt autoremove -y'], shell=True)	
		elif 'fedora' in OS:
			subprocess.run(['sudo dnf update -y && sudo dnf upgrade -y'], shell=True)
		elif 'arch' in OS:
			subprocess.run(['sudo pacman -Syu'], shell=True) # Runs a command through the shell based off of what is returned by the string. In this instance, it runs "sudo pacman -Syu" because the scanned string contained the word "arch" in it.
		elif 'opensuse' in OS:
			subprocess.run(['sudo zypper refresh && sudo zypper update -y'], shell=True)

	def software():
	
		OS = subprocess.getoutput(['cat /etc/os-release'])
		
		if 'debian' in OS:
			subprocess.run(['clear && printf "Please input the software you would like to install: " && read install && sudo apt install -y $install'], shell=True)
		elif 'fedora' in OS:
			subprocess.run(['clear && printf "Please input the software you would like to install: " && read install && sudo dnf install -y $install'], shell=True)
		elif 'arch' in OS:
			subprocess.run(['clear && printf "Please input the software you would like to install: " && read install && sudo pacman -S --noconfirm $install'], shell=True)
		elif 'opensuse' in OS:
			subprocess.run(['clear && printf "Please input the software you would like to install: " && read install && sudo zypper install -y $install'], shell=True)
	
	def nvidia():
	
		NVIDIA = subprocess.run(['sudo bash -c "echo blacklist nouveau > /etc/modprobe.d/blacklist-nvidia-nouveau.conf" && sudo bash -c "echo options nouveau modeset=0 >> /etc/modprobe.d/blacklist-nvidia-nouveau.conf" && sudo update-initramfs -u'], shell=True)
	
	subprocess.run(['clear'], shell=True)					# Clears the Terminal.
	print('\t Welcome to my script panel! What would you like to do? \n') 	# Outputs to the shell.
	print("\t 1. Update")
	print('\t 2. Install software')						# Breaks a line to ready for user input.
	print('\t 3. Blacklist Nouveau')
	print('\t 4. Exit \n')
	
	response = str(input('\t Please input your selection as a number: '))	# Sets up a string-variable called "response" to get user input for it to run functions based off of what was inputted.
	subprocess.run(['clear'], shell=True)					
	if response == '1':							# Checks to see what was inputted by the User. If "1" is inputted, the update() function is called, and once it's done, exits. If an invalid input is entered, nothing happens.
		update()
		sys.exit()							# Exits the program, otherwise the loop will continuously loop through the entire thing, recursively. 
	elif response == '2':
		software()
		sys.exit()
	elif response == '3':
		while True:
			subprocess.run(['clear'], shell=True)
			print("\t This will blacklist the Nouveau driver for systems that have an\n\t NVIDIA card installed w/o proper drivers.\n\n\t Are you sure you want to do this?\n\t ")
			print('\t 1. Yes')
			print('\t 2. No')
			response = str(input("\n\t Response: "))
			if response == '1':
				subprocess.run(['clear'], shell=True)
				nvidia()
				print("\t You'll have to reboot your computer in order for this to apply.")
				sys.exit()
			elif response == '2':
				break
	elif response == '4':
		sys.exit()
