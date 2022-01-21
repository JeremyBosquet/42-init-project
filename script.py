import os
import sys
import fileinput
from shutil import copyfile
from git import Repo
from datetime import datetime

path = os.path.abspath(os.getcwd())

print ("Project name ?")
projectName = raw_input("> ")
projectName = projectName.lower()
if (os.path.isdir(path + "/" + projectName)):
	print("Error: This project already exist")
	exit(0)

print ("Need additionnal flags ?")
flags = raw_input("> ")
if not flags:
	flags = "-Wall -Wextra -Werror"
else:
	flags = "-Wall -Wextra -Werror " + flags

# CREATE FOLDER AND FILES
os.mkdir(path + "/" + projectName)
os.mkdir(path + "/" + projectName + "/srcs")
os.mkdir(path + "/" + projectName + "/includes")
copyfile(os.path.dirname(os.path.realpath(__file__)) + "/templates/Makefile", path + "/" + projectName + "/Makefile")
copyfile(os.path.dirname(os.path.realpath(__file__)) + "/templates/header.h", path + "/" + projectName + "/includes/" + projectName + ".h")
copyfile(os.path.dirname(os.path.realpath(__file__)) + "/templates/main.c", path + "/" + projectName + "/srcs/main.c")
Repo.clone_from("https://github.com/JeremyBosquet/libft", path + "/" + projectName + "/libft")

# EDIT MAIN TEMPLATE
mainFile = open(path + "/" + projectName + "/srcs/main.c", "r+" )
for line in fileinput.input( path + "/" + projectName + "/srcs/main.c" ):
 	mainFile.write(line.replace("$INCLUDE", '#include "' + projectName + '.h"'))
mainFile.close()

# EDIT HEADER TEMPLATE
headerFile = open(path + "/" + projectName + "/includes/" + projectName + ".h", "r+" )
for line in fileinput.input( path + "/" + projectName + "/includes/" + projectName + ".h" ):
 	headerFile.write(line.replace("@@", projectName.upper() + "_H"))
headerFile.close()

# EDIT MAKEFILE TEMPLATE
makefileFile = open(path + "/" + projectName + "/Makefile", "r+" )
for line in fileinput.input(path + "/" + projectName + "/Makefile"):
	makefileFile.write(line.replace("_FLAGS", flags))
makefileFile.close()
makefileFile = open(path + "/" + projectName + "/Makefile", "r+" )
for line in fileinput.input(path + "/" + projectName + "/Makefile"):
	makefileFile.write(line.replace("$$", projectName))
makefileFile.close()

# CHANGE CREATION DATE ON 42 HEADERS
creationDate = datetime.now()
creationDate = creationDate.strftime("%Y/%m/%d %H:%M:%S")

mainFile = open(path + "/" + projectName + "/srcs/main.c", "r+" )
for line in fileinput.input( path + "/" + projectName + "/srcs/main.c" ):
 	mainFile.write(line.replace("DATE", creationDate))
mainFile.close()

headerFile = open(path + "/" + projectName + "/includes/" + projectName + ".h", "r+" )
for line in fileinput.input( path + "/" + projectName + "/includes/" + projectName + ".h" ):
 	headerFile.write(line.replace("DATE", creationDate))
headerFile.close()