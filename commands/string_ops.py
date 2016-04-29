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