import os, string, sys

def echo(commandTokens):
	try:
		print(commandTokens[1])
	except IndexError:
		print("")
	else:
		i = 2
		while(True):
			try:
				print(commandTokens[i])
			except IndexError:
				break
			i += 1
	return 0

def textToAscii(commandTokens):
	output = ""
	try:
		for t in commandTokens[1]:
			output += str(ord(t))
			output += " "
	except IndexError:
		print(output)
	else:
		i = 2
		while(True):
			try:
				output += "32 "
				for t in commandTokens[i]:
					output += str(ord(t))
					output += " "
			except IndexError:
				output = output[:-4]
				print(output)
				break
			i += 1
	return 0

def asciiToText(commandTokens):
	output = ""
	try:
		output += chr(int(commandTokens[1]))
	except IndexError:
		print(output)
	else:
		i = 2
		while(True):
			try:
				output += chr(int(commandTokens[i]))
			except IndexError:
				print(output)
				break
			i += 1
	return 0

def textToHex(commandTokens):
	output = ""
	try:
		for t in commandTokens[1]:
			output += str(hex(ord(t)))
			output += " "
	except IndexError:
		print(output)
	else:
		i = 2
		while(True):
			try:
				output += str(hex(32)) + " "
				for t in commandTokens[i]:
					output += str(hex(ord(t)))
					output += " "
			except IndexError:
				output = output[:-4]
				print(output)
				break
			i += 1
	return 0

def hexToText(commandTokens):
	output = ""
	try:
		output += chr(int(commandTokens[1], 16))
	except IndexError:
		print(output)
	else:
		i = 2
		while(True):
			try:
				output += chr(int(commandTokens[i], 16))
			except IndexError:
				print(output)
				break
			i += 1
	return 0

















