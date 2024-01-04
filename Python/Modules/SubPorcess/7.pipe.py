"""
Python subprocess module provides a way to create and interact with child processes, 
which can be used to run other programs or commands. One of the features of the 
subprocess module is the ability to create pipes, which allow communication between 
the parent and child processes.
"""
import subprocess

ls_process = subprocess.Popen(["ls"], stdout=subprocess.PIPE, text=True)

grep_process = subprocess.Popen(["grep", "BK"], stdin=ls_process.stdout, stdout=subprocess.PIPE, text=True)

output, error = grep_process.communicate()

print(output)

print(error)