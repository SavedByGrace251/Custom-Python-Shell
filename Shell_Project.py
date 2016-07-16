#!python3
#
#Author: Jonathan Newell
#Date: 4-25-2016
#
#Shell Project for CS 321
#
# TODO:
#	

SHELL_VERSION = "0.1a"

import os, subprocess, pip, string, sys, types, re, inspect, io
import commands

COMMAND_LIST = inspect.getmembers(commands, inspect.isfunction)
os.system('clear')
print(COMMAND_LIST)

def executeCommand(commandTokens):
	returnCode = -1
	for cmd in COMMAND_LIST:
		if (commandTokens[0] == cmd[0]):
			returnCode = cmd[1](commandTokens)
	if './' == commandTokens[0][0:2]:
		returnCode = 0
		commandTokens[0] = commandTokens[0][2:]
	if 'listcmds' == commandTokens[0]:
		printString = ""
		for cmd in COMMAND_LIST:
			printString += " | " + cmd[0]
		print(printString.lstrip())
		returnCode = 0
	if (returnCode < 0):
		print('"' + commandTokens[0] + '" is not a command.')
		returnCode = 0
	return returnCode

def checkForRedirect(commandTokens):
	isCommand = True
	isFile = False
	command = []
	redirectLocation = []
	for t in commandTokens:
		if (t == '|'):
			isCommand = False
			continue
		elif (t == '>'):
			isCommand = False
			isFile = True
			continue
		if (isCommand):
			command.append(t)
		else:
			redirectLocation.append(t)
	return command, isFile, redirectLocation

def parseCommand(commandString):
	# split command into tokens
	commandTokens = re.findall('(?<=")[^"\\\\]*(?:\\\\.[^"\\\\]*)*(?=")|(?<=\')[^\'\\\\]*(?:\\\\.[^\'\\\\]*)*(?=\')|[!#-&(-~]+',commandString)
	# tokenization produces blank tokens in certain cases
	# clean blank tokens
	for i in range(len(commandTokens)):
		try:
			if (commandTokens[i].lstrip() == ''):
				del commandTokens[i]
				continue
		except IndexError:
			break

	#print(commandTokens)
	return checkForRedirect(commandTokens)

def main():
	EXIT_CODE = 0
	print("Shell Interpreter Terminal: v" + SHELL_VERSION + "\n")
	while(True):
		if (sys.version_info >= (3,0)):
			command = input(os.getcwd() + " >> ") # get command from user
		else:
			command = raw_input(os.getcwd() + " >> ") # get command from user
		if (command.lstrip() == ""): # if blank command, just continue
			continue
		command, isFile, redirect = parseCommand(command) # parse the command input
		if (command == []):
			continue
		if (redirect == []): # if no redirect exists
			EXIT_CODE = executeCommand(command) # execute the command
		else:
			if (isFile):
				sys.stdout = open(redirect[0], 'w')
				executeCommand(command)
			else:
				sys.stdout = io.StringIO()
				executeCommand(command)
				redirect.append(sys.stdout.getvalue())
				sys.stdout = sys.__stdout__
				executeCommand(redirect)
		if (EXIT_CODE != 0): # if the command returned an exit code, exit
			break
		sys.stdout = sys.__stdout__  # reset stdout 
	return EXIT_CODE

if __name__ == '__main__':
	exitCode = main()
	if (exitCode is not 0):
		print("\nExit with code " + str(exitCode))
	else:
		exit()