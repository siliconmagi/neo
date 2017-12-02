from pexpect import pxssh
from config import amo05
import re
#  import getpass

s = pxssh.pxssh()
hostname = amo05.ip
username = amo05.user
password = amo05.pwd
s.login(hostname, username, password)


def sudo(s, password):
    rootprompt = re.compile('.*[$#]')
    s.sendline('sudo -s')
    s.prompt()
    print(s.before)
    i = s.expect([rootprompt, 'assword.*: '])
    if i == 0:
        print("didnt need password!")
        pass
    elif i == 1:
        print("sending password")
        s.sendline(password)
        j = s.expect([rootprompt, 'Sorry, try again'])
        if j == 0:
            pass
        elif j == 1:
            raise Exception("bad password")
    else:
        raise Exception("unexpected output")
