#python subprocess Popen
"""
`subprocess.Popen` is a lower-level interface to running subprocesses, 
while subprocess.run is a higher-level wrapper around Popen that is intended to be more 
convenient to use.

Popen allows you to start a new process and interact with its standard input, 
output, and error streams. It returns a handle to the running process that can be 
used to wait for the process to complete, check its return code, or terminate it.


"""
import subprocess

p = subprocess.Popen(["python", "--help"], stdout=subprocess.PIPE,stderr = subprocess.PIPE , text = True )
output, errors = p.communicate()

print(output)