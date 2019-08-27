import matplotlib.pyplot as plt

inp = open("../showerGenerator/stations.dat")

x = []
y = []

for line in inp:
  if "#" in line:
    continue
  st = line.split(" ")
  x.append(int(st[1]))
  y.append(int(st[2]))

plt.scatter(y, x)
plt.show()
