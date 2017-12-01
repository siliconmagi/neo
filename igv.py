import os
from time import localtime, strftime
time = strftime("%Y-%m-%d %H:%M:%S", localtime())
cmd = 'git commit -m "' + time + '"'
print(os.getcwd())

# goto vim folder
os.chdir('/home/zeal/p/vim')
print(os.getcwd())

# push changes to github
os.system('git add -A')
os.system(cmd)
os.system('git push')
