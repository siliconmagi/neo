from pexpect import pxssh
from config import amo05
import re
#  import getpass

try:
    s = pxssh.pxssh()
    rootprompt = re.compile('.*[$#]')
    hostname = amo05.ip
    username = amo05.user
    password = amo05.pwd
    s.login(hostname, username, password)
    s.sendline("uptime")
    s.prompt()
    print(s.before)
    i = s.expect('assword.*: ')
    if i == 0:
        print('0')
    elif i == 1:
        print('1')
    else:
        print('none')
        s.logout()

except pxssh.ExceptionPxssh as e:
    print("pxssh failed on login.")
    print(e)
