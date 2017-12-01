import os
from config import con, hu1, hp3, hi3

#  os.system(con + hu2 + hp2 + hi2)
cmd = con + ' -u ' + hu1 + " -p '" + hp3 + "' " + hi3
os.system(cmd)
