# -*- coding: utf-8 -*-

"""
Date: 28/08/2015
author: peyoromn
"""

import os

currentDirectoryPath = os.getcwd()
print currentDirectoryPath
listofFileNames = os.listdir(currentDirectoryPath)
print
for name in listofFileNames:
	if os.path.isfile(currentDirectoryPath + "/" + name): 
		if ".py" in name:
			print ">> " + name
	else:
		print ">> << {} >>".format(name)
