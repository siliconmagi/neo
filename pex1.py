from pexpect import pxssh
from config import amo09

user = amo09.user
host = amo09.ip

try:
    s = pxssh.pxssh()
    s.login(amo09.ip, amo09.user, amo09.pwd)
    s.sendline('date')       # run a command
    s.prompt()                # match the prompt
    print(s.before)           # print everything before the prompt.
    s.sendline('sudo whoami')  # run a command
    s.expect('(?i)password.*:')  # match password prompt for sudo
    s.sendline(amo09.pwd)
    s.prompt()
    print(s.before)
    s.logout()
except pxssh.ExceptionPxssh as e:
    print(e)
