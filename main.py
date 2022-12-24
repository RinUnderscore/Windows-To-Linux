import os
quit = False

# Manually Convert Functions
def ls():
	os.system('dir')

def cd(perm):
	try:
		os.chdir(perm)
	except FileNotFoundError:
		os.chdir('..')

# Listening for Commands
def listeningfunc():
	# Process Command -Specifics Filter
	try:
		cmd = listening.split(" ", 1)[0]
	except:
		cmd = listening
	# Specific Commands
	if cmd == "ls":
		ls()
	elif cmd == "q" or cmd == "quit":
		quit = True
	elif cmd == "cd":
		try:
			cd(listening.split(" ", 1)[1])
		except IndexError:
			cd('')
	else:
		print(f'WTL: {cmd}: command not found')

# Main Control Loop
if __name__ == "__main__":
	print("Windows to Linux (WTL) [Version 0.1.2a]")
	while not quit:
		listening = input(f"{os.getcwd()}:$ ")
		listeningfunc()
