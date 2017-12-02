import platform
import os
import logging
#  import subprocess
import pexpect

log = logging.getLogger(__name__)


def sudo_exec(cmdline, passwd):
    osname = platform.system()  # 1
    if osname == 'Linux':
        prompt = r'\[sudo\] password for %s: ' % os.environ['USER']
    elif osname == 'Darwin':
        prompt = 'Password:'
    else:
        assert False, osname

    child = pexpect.spawn(cmdline)
    idx = child.expect([prompt, pexpect.EOF], 3)  # 2
    if idx == 0:  # if prompted for the sudo password
        log.debug('sudo password was asked.')
        child.sendline(passwd)
        child.expect(pexpect.EOF)
    return child.before
