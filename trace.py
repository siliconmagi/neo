import re

infile = './trace.txt'
p = re.compile(r'.*UID(\d+)')

with open('infile') as infile:
    for line in infile:
        m = p.match(line)
        if m:
            print(m.groups[0])
