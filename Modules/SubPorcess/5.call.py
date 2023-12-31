
"""
`subprocess.call()` is a function in the Python subprocess module that is used to run a 
command in a separate process and wait for it to complete. It returns the return code of 
the command, which is zero if the command was successful, and non-zero if it failed.


"""
import subprocess

return_code = subprocess.call(["python", "--version"])

if return_code == 0:
    print("Command executed successfully.")

else:

    print("Command failed with return code", return_code)