import subprocess

#Running shell commands:
result = subprocess.run(["dir"], shell=True, capture_output=True, text=True)
print(result.stdout)