import os, string, sys, shutil, glob, re

def cat(commandTokens):
	try:
		if os.path.isfile(commandTokens[1]):
			file = open(commandTokens[1])
			print(file.read())
		else:
			print('The file "' + commandTokens[1] + '" cannot be found.')
	except IndexError:
		print("")
	return 0

def grep(commandTokens):
	foundFile = False
	for file in glob.iglob(commandTokens[2]):
		foundFile = True
		for line in open(file, 'r'):
			if (re.search(commandTokens[1], line)):
				print(line)
	if not foundFile:
		for line in commandTokens[2].split('\n'):
			if (re.search(commandTokens[1], line)):
				print(line)
	return 0

def cp(commandTokens):
	try:
		file = commandTokens[1]
		dest = commandTokens[2]

		if os.path.isfile(file):
			shutil.copy(file, dest)
		else:
			print('The file "' + commandTokens[1] + '" cannot be found.')
	except IndexError:
		print("ERROR: You must provide both a source file and destination location")
	return 0

def mv(commandTokens):
	try:
		file = commandTokens[1]
		dest = commandTokens[2]

		if os.path.isfile(file):
			shutil.move(file, dest)
		else:
			print('The file "' + commandTokens[1] + '" cannot be found.')
	except IndexError:
		print("ERROR: You must provide both a source file and destination location")
	return 0

def touch(commandTokens):
	try:
		file = commandTokens[1]
		outFile = open(file, 'w')
		outFile.write('')
	except IndexError:
		print("ERROR: You must provide a file name")
	return 0