import os
from time import localtime, strftime
time = strftime("%Y-%m-%d %H:%M:%S", localtime())
cmd = 'git commit -m "' + time + '"'

# rsync dotfiles to folder
os.system('rsync -avz ~/.config/fish/config.fish ~/p/dotfiles')
os.system('rsync -avz ~/.tmux.conf.local ~/p/dotfiles')
os.system('rsync -avz ~/.bashrc ~/p/dotfiles')
os.system('rsync -avz ~/.vimrc ~/p/dotfiles')
os.system('rsync -avz ~/.config/alacritty/alacritty.yml ~/p/dotfiles')
os.system('rsync -avz ~/.profile ~/p/dotfiles')
os.chdir('/home/xeno/p/dotfiles')
print(os.getcwd())

# push changes to github
os.system('git add -A')
os.system(cmd)
os.system('git push')
