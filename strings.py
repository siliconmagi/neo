# strings
m1 = 'Hello Plane Earth'
greeting = 'Hello'
name = 'Silicon Magi'

# concat strings
m2 = '\n' + greeting + ', ' + name + ' and Welcome!'

# fstrings
m3 = '\n{}, {}. Welcome!'.format(greeting, name)
m4 = f'\n{greeting}, {name.upper()}. Welcome!'

print(m1, m2, m3, m4)

# slice
print(m1[0:5])
print(m1[6:])

# lowercase
print(m1.lower())
print(m1.upper())

# count
print(m1.count('Hello'))
print(m1.count('l'))

# find message index
print(m1.find('Plane'))
# unknown values return '-1'
print(m1.find('Globe'))

# replace
fe = m1.replace('Plane', 'Flat')
print(fe)

# print methods
print(dir(name))

# print help
#  print(help(str))

# dictionary
person = {'name': 'Silicon Magi', 'age': 12}
scroll = 'My name is {} and I am {} years old'.format(person['name'],
                                                      person['age'])
scroll2 = '\nMy name is {0} and I am {1} years old'.format(person['name'],
                                                           person['age'])
tag = 'h1'
text = 'Python HTML'
scroll3 = '\n<{0}>{1}<{0}>'.format(tag, text)
scroll4 = ''
