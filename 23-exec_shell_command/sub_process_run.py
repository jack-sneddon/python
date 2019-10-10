# start new applications from within the python application
import subprocess

# run() returns a CompletedProcess object if it was successful
# errors in the created process are raised here too
process = subprocess.run(['ls','-lha'], check=True, stdout=subprocess.PIPE, universal_newlines=True)
output = process.stdout
print(output)

# get return code
cp = subprocess.run(["cp"])
output = cp
print(f"Expecting an error from cp: \n\t{output}")

# force exception of there is an error
# subprocess.run(["ls","foo bar"], check=True)

# store output and error in a string
print("\n===subprocess.run() ")
cp = subprocess.run(["ls","-lha"], universal_newlines=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
print(f"stdout =  + {cp.stdout}")
print(f"stderr =  + {cp.stderr}")
print(f"returncode =  + {cp.returncode}")
