# popen is used for more complex applications
import os
import subprocess
from subprocess import Popen

# block until process is done
p = subprocess.Popen(["ls","-lha"])
p.wait()

# error message in a string
p = subprocess.Popen(["ls","-lha"], stdout=subprocess.PIPE, stderr=subprocess.PIPE, universal_newlines=True)
output, errors = p.communicate()

print("\n=== Error message in a string" + output)

# Redirect to a file
output_file = "out.txt"

myoutput = open(output_file,'w+')
p = Popen(["ls","-lha"], stdout=myoutput, stderr=subprocess.PIPE, universal_newlines=True)

output, errors = p.communicate()

# stdout has been written to this file
with open(output_file,"r") as f:
    print(f.read())

# cleanup
os.remove(output_file) 

