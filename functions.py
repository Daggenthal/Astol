# Author:	Daggenthal
# Started:	05/13/2021 at 01:20
# Finished:	02/06/2022 at 20:39

import sys, subprocess							# This imports the required utilities for Python 3 to run this script.
								

									# This allows us to exit the program with 'CTRL+C' or 'CTRL+D' without spitting out errors / nonsense.
									# The program starts out with a loop so it doesn't exit / crash instantly when a non-supported string (input) is, well, inputted.
def update():								# Defines a function called update.
		
	OS = subprocess.getoutput(['cat /etc/os-release'])		# Defines OS, then runs a command located in (['']) + grabs the output of said command and stores it into the variable called

	if 'debian' in OS:					# Scans the string that's outputted by the command and searches for what's in '', so in this case it's searching for the word "debian".
		subprocess.run(['sudo apt update -y && sudo apt upgrade -y --allow-downgrades && sudo apt autoremove -y'], shell=True)	
	elif 'fedora' in OS:
		subprocess.run(['sudo dnf update -y && sudo dnf upgrade -y'], shell=True)
	elif 'arch' in OS:
		subprocess.run(['sudo pacman -Syu'], shell=True) 	# Runs a command through the shell based off of what is returned by the string. In this instance, it runs "sudo pacman -Syu" because the scanned string contained the word "arch" in it.
	elif 'opensuse' in OS:
		subprocess.run(['sudo zypper refresh && sudo zypper update -y'], shell=True)
	elif 'freebsd' in OS:
		subprocess.run(['sudo freebsd-update fetch && sudo freebsd-update install'], shell=True)

def remove():
	while True:
				
		print('\n\t Would you like to remove some software, or go back?\n')
		print('\t 1: Remove software')
		print('\t 2: Go back\n\t')
				
		response = str(input('\t Please input your selection: '))

		if response == '1':

			OS = subprocess.getoutput(['cat /etc/os-release'])

			if 'debian' in OS:
				subprocess.run(['clear && printf "\t Please input the software you would like to remove: " && read remove && sudo apt remove $remove'], shell=True)
			elif 'fedora' in OS:
				subprocess.run(['clear && printf "\t Please input the software you would like to remove: " && read remove && sudo dnf remove $remove'], shell=True)
			elif 'arch' in OS:
				subprocess.run(['clear && printf "\t Please input the software you would like to remove: " && read remove && sudo pacman -R $remove'], shell=True)
			elif 'opensuse' in OS:
				subprocess.run(['clear && printf "\t Please input the software you would like to remove: " && read remove && sudo zypper remove $remove'], shell=True)
			elif 'freebsd' in OS:
				subprocess.run(['clear && printf "\t Please input the software you would like to remove: " && read remove && sudo pkg remove -y $remove'], shell=True)
		elif response == '2':
				break
		
def software():
	while True:
			
		print('\n\t Would you like to install some software, or go back?\n')
		print('\t 1: Install software')
		print('\t 2: Go back\n\t')
				
		response = str(input('\t Please input your selection: '))
		if response == '1':
		
			OS = subprocess.getoutput(['cat /etc/os-release'])
					
			if 'debian' in OS:
				subprocess.run(['clear && printf "\t Please input the software you would like to install: " && read install && sudo apt install -y $install'], shell=True)
			elif 'fedora' in OS:
				subprocess.run(['clear && printf "\t Please input the software you would like to install: " && read install && sudo dnf install -y $install'], shell=True)
			elif 'arch' in OS:
				subprocess.run(['clear && printf "\t Please input the software you would like to install: " && read install && sudo pacman -S --noconfirm $install'], shell=True)
			elif 'opensuse' in OS:
				subprocess.run(['clear && printf "\t Please input the software you would like to install: " && read install && sudo zypper install -y $install'], shell=True)
			elif 'freebsd' in OS:
				subprocess.run(['clear && printf "\t Please input the software you would like to install: " && read install && sudo pkg install -y $install'], shell=True)
					
		elif response == '2':
			break
		
def nvidia():
	while True:
			
		subprocess.run(['clear'], shell=True)
		print("\t This will blacklist the Nouveau driver for systems that have an\n\t NVIDIA card installed w/o proper drivers.\n\n\t Are you sure you want to do this?\n\n\t Please note that this has only been tested on Ubuntu 21.04;\n\t")
		print('\t 1: Yes')
		print('\t 2: No')
		
		response = str(input('\n\t Response: '))
		if response == '1':
			subprocess.run(['clear'], shell=True)
			NVIDIA = subprocess.run(['sudo bash -c "echo blacklist nouveau > /etc/modprobe.d/blacklist-nvidia-nouveau.conf" && sudo bash -c "echo options nouveau modeset=0 >> /etc/modprobe.d/blacklist-nvidia-nouveau.conf" && sudo update-initramfs -u'], shell=True)
			print("\t You'll have to reboot your computer in order for this to apply.")
			sys.exit()
		elif response == '2':
			break

			
		
def return_to_loop():
	while True:
					
		print('\n\n ----------------------------------------------------------------------------\n')
		print('\t\t\t\t Astol')
		print('\n\n\t Would you like to return to the main menu?\n\t')
		print('\t 1. Yes')
		print('\t 2. No')
		
		response = str(input('\n\t Response: '))
		if response == '1':
			break
		elif response == '2':
			subprocess.run(['clear'], shell=True)
			sys.exit() 				# This causes the program to terminate gracefully.

