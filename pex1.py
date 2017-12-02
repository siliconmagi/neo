from config import amo05
import re
from pexpect import pxssh
#  import getpass

try:
    s = pxssh.pxssh()
    rootprompt = re.compile('.*[$#]')
    hostname = amo05.ip
    username = amo05.user
    password = amo05.pwd
    s.login(hostname, username, password)
    s.sendline("sudo su -")
    s.prompt()
    print(s.before)
    i = s.expect([rootprompt, 'assword.*: '])
    if i == 0:
        print('0')
        pass
    elif i == 1:
        print('1')
    else:
        print('none')

except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)
