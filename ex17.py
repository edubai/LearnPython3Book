from sys import argv
from os.path import exists

script, from_file, to_file = argv

print(f"Copying from {from_file} to {to_file}")

# we could do these two on one line, how ?
from_file = open(from_file)
indata= in_file.read()

#exist() will check if the file exists and will return True.
print(f"Does the output file exist? {exists(to_file)}")
print("Ready, hit RETURN to continue, CTRL-C to abort.")
#input is used here to wait for ctrl c or retrun to continue.
input()

# w is used to give persmission to write to a file.
out_file = open(to_file, 'w')
out_file.write(indata)

print("Alright, all done.")

out_file.close()
in_file.close()
