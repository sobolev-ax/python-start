poem = '''There was a young lady named Bright,
Whose speed was far faster than light;
She started one day
In a relative way,
And returned on the previous night.'''
# write
fout = open('relativity', 'wt')
fout.write(poem)
fout.close()
# print
fout = open('relativity', 'wt')
print(poem, file=fout, sep='', end='')
fout.close()
# chunks
fout = open('relativity', 'wt')
size = len(poem)
offset = 0
chunk = 100
while True:
    if offset > size:
        break
    fout.write(poem[offset: offset + chunk])
    print(poem[offset: offset + chunk])
    offset += chunk
fout.close()
# exception
try:
    fout = open('relativity', 'xt')
    fout.write('La la lend')
except FileExistsError:
    print('File already exists')
fout.close()
# read
fet = open('relativity', 'rt')
poem = fet.read()
fet.close()
print(len(poem))
# chunks
poem = ''
chunk = 100
fin = open('relativity', 'rt')
while True:
    fragment = fin.read(chunk)
    if not fragment:
        break
    poem += fragment
fin.close()
# итератор
poem = ''
fin = open('relativity', 'rt')
for line in fin:
    poem += line
fin.close()
# lines = fin.readlines()
