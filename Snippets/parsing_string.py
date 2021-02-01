txt = 'From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008'
fpos = txt.find('@')
print(fpos)

spos = txt.find(' ',fpos)
print(spos)

fin_string = txt[fpos+1:spos]
print(fin_string)

for i in [2,1,5]:
    print(i)
