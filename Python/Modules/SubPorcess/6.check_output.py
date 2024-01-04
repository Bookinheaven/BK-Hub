"""
check_output is a function in the subprocess module that is similar to run(), 
but it only returns the standard output of the command, and raises a CalledProcessError 
exception if the return code is non-zero.
"""


import subprocess

try:

    output = subprocess.check_output(["python", "--version"], text=True)

    print(output)

except subprocess.CalledProcessError as e:

    print(f"Command failed with return code {e.returncode}")
