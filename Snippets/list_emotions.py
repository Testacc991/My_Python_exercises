import random
emo = []
f = open("emotions.txt", "r")
for x in f:
  emo.append(x)
f.close()

while len(emo)>0:
    if input():
        rndom_number = random.randrange(0, len(emo))
        print(emo[rndom_number])
        emo.pop(rndom_number)
        print(len(emo))