enter = ""
l = []
while enter != "done":
        enter = input()
        try:
            int(enter)
            l.append(enter)
        except:
            print("invalid input")       
print(l)

    