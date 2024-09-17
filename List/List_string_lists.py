a='spam'
b=list(a)
print(b)

a='spam spam spam'
b=a.split()
print(b)

a='spam-spam-spam'
b=a.split('-')
print(b)

a='spam-spam-spam'
delimeter='a'
b=a.split(delimeter)
print(b)
print(delimeter.join(b))