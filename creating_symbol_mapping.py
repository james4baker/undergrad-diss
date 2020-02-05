import random
x = 62
t = {}
for p in range(50):
	for i in range(x):
		t[i] = chr(97+random.randint(0,25))
	print(t)
	print()
input()