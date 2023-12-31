import subprocess

result = subprocess.run(["/usr/bin/python3", "-c", "print('This is directly from a subprocess.run() function')"], capture_output=True, text=True)

#Standard Output:
print(result.stdout)

#Standard Error (if any):
print(result.stderr)
