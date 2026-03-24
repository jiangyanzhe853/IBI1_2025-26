a = 5080000
b = 5330000
c = 5550000
d = b-a
e = c-b
print(d)
print(e)
if d>e:
    print("increae slow down")
else:
    print("increase speed up")

X = True
Y = False
W = X or Y
print(W)

#truth table:
# X = True Y = True   W = True
# X = True Y = False  W = True
# X = False Y = True  W = True
# X = False Y = False W = False
