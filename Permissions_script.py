#!/usr/bin/python
import stat, sys, os, string, commands

try:
	pattern = raw_input("Enter the file pattern to search for:\n")    #Take input from the user for a search pattern
	commandString = "find " + pattern                                 #Concatenate search pattern with find command
	commandOutput = commands.getoutput(commandString)                 #Run the command using commands module



	findResults = string.split(commandOutput, "\n")                   #Split the output based on new line character 
	#output find results, along with permissions
	print "Files:"													  	
	print commandOutput
	print "================================"
	for file in findResults:
		print stat.S_IMODE(os.lstat(file)[stat.ST_MODE])              #Iterate the list findResults have pattern matched file names
		mode=stat.S_IMODE(os.lstat(file)[stat.ST_MODE])				  
		print "\nPermissions for file ", file, ":"
		for level in "USR", "GRP", "OTH":
			for perm in "R", "W", "X":
				if mode & getattr(stat,"S_I"+perm+level):
					print level, " has ", perm, " permission"
				else:
					print level, " does NOT have ", perm, " permission"
except:
    print "There was a problem - check the message above"
