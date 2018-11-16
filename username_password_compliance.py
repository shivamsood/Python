#!/usr/bin/python

import pwd

#initialize counters
erroruser = []
errorpass = []

#get password database
passwd_db = pwd.getpwall()

try:
	for entry in passwd_db:
		username = entry[0]
		password = entry[1]

		if len(username) < 6:
			erroruser.append(username)
		if len(password) < 8:
			errorpass.append(username)
	print "The following users have an invalid userid (less than six characters):"

	for item in erroruser:
		print item

	print "\nThe following users have invalid password(less than eight characters):"
	for item in errorpass:
		print item

except:
    print "There was a problem running the script."
