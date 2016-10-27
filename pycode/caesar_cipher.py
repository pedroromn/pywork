# -*- coding: utf-8 -*-

##
# Implement a Caesar cipher that shifts all of the letters 
# in a message by an amount provided by the user. Use a 
# negative shift value to decode a message.

# Read the message and shift amount from the server
message = raw_input("Enter the message: ")
shift = int(raw_input("Enter the shift value: "))

# Process each character, constructing a new message
new_message = ""
for ch in message:
	if ch >= "a" and ch <= "z":
		# Process a lowercase letter by determining its
		# position in the alphabet( 0 - 25 ), computing
		# its new position, and adding it to the new 
		# message
		pos = ord(ch) - ord("a")
		pos = (pos + shift) % 26
		new_char = chr(pos + ord("a"))
		new_message = new_message + new_char
	elif ch >= "A" and ch <= "Z":
		pos = ord(ch) - ord("A")
		pos = (pos + shift) % 26
		new_char = chr(pos + ord("A"))
		new_message = new_message + new_char
	else:
		# if the character is not a letter then copy it into
		# the new message
		new_message = new_message + ch

print "The shifted message is: {}".format(new_message)
