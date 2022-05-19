import sys							# This imports the required utilities for Python 3 to run this script.
								
from subprocess import run, getoutput
from string import input
									
									# This allows us to exit the program with 'CTRL+C' or 'CTRL+D' without spitting out errors / nonsense.
									# The program starts out with a loop so it doesn't exit / crash instantly when a non-supported string (input) is, well, inputted.

OS = getoutput(['cat /etc/os-release']) # Defines OS, then runs a command located in (['']) + grabs the output of said command and stores it into the variable called

def update():								# Defines a function called update.
		
	if 'debian' in OS:					# Scans the string that's outputted by the command and searches for what's in '', so in this case it's searching for the word "debian".
		run(['sudo apt update -y && sudo apt upgrade -y --allow-downgrades && sudo apt autoremove -y'], shell=True, check=True)	
	elif 'ubuntu' in OS:
		run(['sudo apt update -y && sudo apt upgrade -y --allow-downgrades && sudo apt autoremove -y'], shell=True, check=True)
	elif 'fedora' in OS:
		run(['sudo dnf update -y && sudo dnf upgrade -y'], shell=True, check=True)
	elif 'arch' in OS:
		run(['sudo pacman -Syu'], shell=True, check=True) 	# Runs a command through the shell based off of what is returned by the string. In this instance, it runs "sudo pacman -Syu" because the scanned string contained the word "arch" in it.
	elif 'opensuse' in OS:
		run(['sudo zypper refresh && sudo zypper update -y'], shell=True, check=True)
	elif 'freebsd' in OS:
		run(['sudo freebsd-update fetch && sudo freebsd-update install'], shell=True, check=True)

def remove():
	while True:
				
		print('\n\t Would you like to remove some software, or go back?\n')
		print('\t 1: Remove software')
		print('\t 2: Go back\n\t')
				
		response = input('\t Please input your selection: ')

		if response == '1':

			if 'debian' in OS:
				run(['clear && printf "\t Please input the software you would like to remove: " && read remove && sudo apt remove $remove'], shell=True, check=True)
			elif 'ubuntu' in OS:
				run(['clear && printf "\t Please input the software you would like to remove: " && read remove && sudo apt remove $remove'], shell=True, check=True)
			elif 'fedora' in OS:
				run(['clear && printf "\t Please input the software you would like to remove: " && read remove && sudo dnf remove $remove'], shell=True, check=True)
			elif 'arch' in OS:
				run(['clear && printf "\t Please input the software you would like to remove: " && read remove && sudo pacman -R $remove'], shell=True, check=True)
			elif 'opensuse' in OS:
				run(['clear && printf "\t Please input the software you would like to remove: " && read remove && sudo zypper remove $remove'], shell=True, check=True)
			elif 'freebsd' in OS:
				run(['clear && printf "\t Please input the software you would like to remove: " && read remove && sudo pkg remove -y $remove'], shell=True, check=True)

		elif response == '2':
				break
		
def software():
	while True:
			
		print('\n\t Would you like to install some software, or go back?\n')
		print('\t 1: Install software')
		print('\t 2: Go back\n\t')
				
		response = input('\t Please input your selection: ')

		if response == '1':
		
			if 'debian' in OS:
				run(['clear && printf "\t Please input the software you would like to install: " && read install && sudo apt install -y $install'], shell=True, check=True)
			elif 'ubuntu' in OS:
				run(['clear && printf "\t Please input the software you would like to install: " && read install && sudo apt install -y $install'], shell=True, check=True)
			elif 'fedora' in OS:
				run(['clear && printf "\t Please input the software you would like to install: " && read install && sudo dnf install -y $install'], shell=True, check=True)
			elif 'arch' in OS:
				run(['clear && printf "\t Please input the software you would like to install: " && read install && sudo pacman -S --noconfirm $install'], shell=True, check=True)
			elif 'opensuse' in OS:
				run(['clear && printf "\t Please input the software you would like to install: " && read install && sudo zypper install -y $install'], shell=True, check=True)
			elif 'freebsd' in OS:
				run(['clear && printf "\t Please input the software you would like to install: " && read install && sudo pkg install -y $install'], shell=True, check=True)
					
		elif response == '2':
			break
