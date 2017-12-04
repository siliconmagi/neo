import re

text = 'gfgfdAAA1234ZZZuijjk<hi><there>'

try:
    found = re.search('<(.+?)>', text).group(1)
    print(found)
except AttributeError:
    found = 'Not Found'  # error handling
    print(found)
