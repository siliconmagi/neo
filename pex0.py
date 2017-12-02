import pexpect
from config import mypass
child = pexpect.spawn('sudo su -')
child.expect('assword.*: ')
child.sendline(mypass)
child.expect('root')
child.sendline('sudo whoami')
print(child.before)   # Print the result of the ls command.
child.interact()     # Give control of the child to the user.
#  child.expect(pexpect.EOF, timeout=5)
