import os, string, sys, shutil

def ls(commandTokens):
	fileList = []
	try:
		fileList = os.listdir(commandTokens[1])
	except IndexError:
		fileList = os.listdir()
	printString = ""
	for f in fileList:
		printString += "  " + f
	print(printString.lstrip())
	return 0

def cd(commandTokens):
	try:
		os.chdir(commandTokens[1])
	except IndexError:
		os.chdir(os.path.expanduser('~'))
	except OSError:
		print('The directory "' + commandTokens[1] + '" does not exist.')
	return 0

def mkdir(commandTokens):
	try:
		os.mkdir(commandTokens[1])
	except IndexError:
		print("You must enter the name of the directory to create.")
	return 0

def rm(commandTokens):
	try:
		if os.path.isfile(commandTokens[1]) or os.path.isdir(commandTokens[1]):
			ans = input('Are you sure you want to remove "' + commandTokens[1] + '"? (Y or N):')
		else:
			print('The file "' + commandTokens[1] + '" cannot be found.')
			return 0
	except IndexError:
		print("You must enter the name of the directory/file to remove.")
	if ans.lower() in ['y','yes']:
		try:
			os.rmdir(commandTokens[1])
			print('deleted the directory "' + commandTokens[1] + '".')
		except NotADirectoryError:
			os.remove(commandTokens[1])
			print('deleted the file "' + commandTokens[1] + '".')
		except OSError:
			ans = input('The directory "' + commandTokens[1] + '" is not empty.\nDo you still want to remove it? (Y or N):')
			if ans.lower() in ['y','yes']:
				shutil.rmtree(commandTokens[1])
				print('directory "' + commandTokens[1] + '" deleted.')
	return 0