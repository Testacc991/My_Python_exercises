import re
f = open("com.txt", "r")
f = str(f.read())
x = re.findall("[a-z-' ]+", f)
for i in x:
    print(i," ")