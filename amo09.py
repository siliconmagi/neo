from pexpect import pxssh
from config import amo09, amo10, amo05, amo07
import re


s = pxssh.pxssh()
cmd = "sudo mailq | grep Dec | awk '{print $7}' | sort | uniq -c | sort -rn"
cmd2 = "mailq | grep Dec | awk '{print $7}' | sort | uniq -c | sort -rn"


def date():
    s.sendline('date')       # run a command
    s.prompt()                # match the prompt
    print(s.before.decode('unicode_escape'))


def ssh(x):
    try:
        if x == 9:
            s.login(amo09.ip, amo09.user, amo09.pwd)
            date()
            s.sendline(cmd)         # run a command
        elif x == 10:
            s.login(amo10.ip, amo10.user, amo10.pwd)
            date()
            s.sendline(cmd)         # run a command
        elif x == 5:
            s.login(amo05.ip, amo05.user, amo05.pwd)
            date()
            s.sendline(cmd2)         # run a command
        elif x == 7:
            s.login(amo07.ip, amo07.user, amo07.pwd)
            date()
            s.sendline(cmd2)         # run a command
        else:
            print('Invalid Server number')
        #  s.expect('(?i)password.*:')  # match password prompt for sudo
        #  s.sendline(amo09.pwd)
        s.prompt()
        log = s.before.decode('unicode_escape')
        print(log)
        top = re.findall("\d.*?>", log)
        #  top = re.search('<(.*?)>', log).group(1)
        print(top)
        s.logout()
    except pxssh.ExceptionPxssh as e:
        print(e)
