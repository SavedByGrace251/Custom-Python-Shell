import os, string, sys, glob, re

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
	return 0

def mv(commandTokens):
	return 0