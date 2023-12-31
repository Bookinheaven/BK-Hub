import subprocess
# Running Python scripts:
result = subprocess.run(["python", "/home/burn/Documents/GitHub/FIle--_-/My_Work/Python/Modules/SubPorcess/2.test-file.py"], capture_output=True, text=True)
print(result.stdout)