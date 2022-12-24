import subprocess
quit = False

# Manually Convert Functions
def ls():
	subprocess.run('dir')

def cd(perm):
	try:
		subprocess.run(f'cd {perm}')
	except FileNotFoundError:
		subprocess.run('cd ..')

def mv(perm):
	subprocess.run(f'ren {perm}')

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
	elif cmd == "mv":
		mv(listening.split(' ', 1)[1])
	else:
		print(f'WTL: {cmd}: command not found')

# Main Control Loop
if __name__ == "__main__":
	print("Windows to Linux (WTL) [Version 0.1.2a]")
	while not quit:
		loc = str(subprocess.run('pwd'))
		listening = input(loc + ":$ ")
		listeningfunc()
