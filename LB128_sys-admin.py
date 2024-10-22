"""
Lab 128 - Medina, Alejandro

"""

import os
import subprocess

os.system("ls | grep sys")

print("\n")

"""
Lista de Argumentos para subprocess.run:

subprocess.run(args, *, stdin=None, input=None, stdout=None, stderr=None, capture_output=False, shell=False, cwd=None, timeout=None, check=False, encoding=None, errors=None, text=None, env=None, universal_newlines=None)

"""

subprocess.run(["ls","-l"])
print("\n")


subprocess.run(["ls","-l","README.md"])

print("\n")

command="uname"
commandArgument="-a"
print(f'Gathering system information with command: {command} {commandArgument}')
subprocess.run([command,commandArgument])









