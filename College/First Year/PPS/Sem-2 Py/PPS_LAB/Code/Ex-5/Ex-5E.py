# Write a python function to copy the content of one file into another file
def copyed(src_file, des_file):
    with open(f"{src_file}", "r") as srcfile:
        reada = srcfile.read()
        with open (f"{des_file}", "w") as desfile:
            desfile.write(reada)
            print(f"Successfully copyed the content of {src_file} into {des_file} file")

copyed("srcE.txt", "desE.txt")
print("╔═════════════╗\n║   Tanvik    ║\n║ URK23CS1261 ║\n╚═════════════╝")