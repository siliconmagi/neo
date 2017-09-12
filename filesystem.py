# navigate/edit filesystem
import os

# change directory
os.chdir('/home/zeal/p/python')

# verify pwd
print(os.getcwd())

# print all files in pwd
for f in os.listdir():
    print(f)

# parse filename via tuple
for f in os.listdir():
    print(os.path.splitext(f))

# parse filename via tuple, return file_name
for f in os.listdir():
    # assign variables to split tuple
    f_name, f_ext = os.path.splitext(f)
    f_title, f_course, f_num = f_name.split(' ')
    # strip whitespace
    f_title = f_title.strip()
    f_course = f_course.strip()
    # strip beginning character and add '0' at beginning
    f_num = f_num.strip()[1:].zfill(2)
    # format placeholders with vars
    name = '{}-{}-{}{}'.format(f_num, f_course, f_num, f_ext)
    # take original file and rename to 'name'
    os.rename(f, name)
