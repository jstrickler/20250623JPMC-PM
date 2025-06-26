a = [1, 2, 3]
b = open('DATA/mary.txt')
c = reversed(a)
d = (x * 10 for x in a)

for m in a:
    print(m)
print()

for m in b:
    print(m)
print()

print(c)
for m in c:
    print(m)
print()

for m in d:
    print(m)