biggest = 0
cash = 0 
smallest = None
for i in [45,3,22,134,23,600,76,90]:
    if smallest is None or i < smallest:
        smallest = i
    if i > biggest:
        biggest = i

print("smallest ",smallest)
print("biggest", biggest)