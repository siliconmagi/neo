# navigate/edit filesystem
import os

# change directory
os.chdir('/home/xeno/p/neo')

# verify pwd
print(os.getcwd())

# print all files in pwd
for f in os.listdir():
    print(f)
