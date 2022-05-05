#!/usr/bin/env python3
################################################################################
# say.py
#
# This is a quick and dirty program to say the command-line arguments.
# example:
# 	python3 say.py this is a test
################################################################################

import sys
import os
import json

if len(sys.argv) < 2:
	print ("Give me something to say.")
	print ("example:")
	print ("	python3 " + sys.argv[0] + " this is a test")
	exit()


with open("vocabulary.json") as f:
	vocabulary = json.loads( f.readline() )


words = sys.argv[1:]

command_string = "play "

words_available   = []
words_unavailable = []

for word in words:
	if word in vocabulary.keys():
		words_available.append(word)
		command_string += "d/" + vocabulary[word] + ".wav "
	else:
		words_unavailable.append(word)

print ("words_available   = " + str(words_available  ))
print ("words_unavailable = " + str(words_unavailable))

if words_available:
	os.system (command_string)
else:
	print ("Nothing to say.")

