import os
from config import con, hu2, hp2, hi2

#  os.system(con + hu2 + hp2 + hi2)
cmd = con + ' -u ' + hu2 + " -p '" + hp2 + "' " + hi2
os.system(cmd)
