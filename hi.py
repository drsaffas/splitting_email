import re

f = open('sheet', 'r')

for each in f :
    b = []
    a = re.split(r'(?:@#p|#m|%p|[@~+=])', each, 1)
    b = a[0]
    d = ''.join(b)
    print(d)

