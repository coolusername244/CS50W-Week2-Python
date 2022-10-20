# create an empty set
s = set()

# add elements to set
s.add(1)
s.add(2)
s.add(3)
s.add(4)
# this wont be printed as sets dont print duplicates
s.add(3)
print(s)

s.remove(2)
print(s)

print(f"The set has {len(s)} elements")