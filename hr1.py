import os
from config import con, hu1, hp1, hi1

cmd = con + ' -u ' + hu1 + ' -p "' + hp1 + '" ' + hi1
os.system(cmd)
