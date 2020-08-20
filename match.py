import re 
pat = re.compile(r'[a-z]+')
# m = pat.findall('tem12po')


m = pat.findall('tem12po')
print(m)
m = pat.match('tem12po')
print(m)
m = pat.search('tem12po')
print(m)