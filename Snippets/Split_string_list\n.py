txt = """
vasya
Passed
vera
ded
"""
txt = txt.split("\n")

fin = []
for i in txt:
    if i == "Not Passed" or i == "Passed":
        pass
    else:
        fin.append(i)
print("\n".join(fin))        