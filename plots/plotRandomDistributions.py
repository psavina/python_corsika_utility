import matplotlib.pyplot as plt
import numpy as np
from matplotlib import colors
from matplotlib.ticker import PercentFormatter
import showerGenerator.randLib as rndL

nPoints = 3000000
nBins = 150

np.random.seed(19680801)
u = np.random.uniform(0.0, 1.0, nPoints)
v = np.random.uniform(0.0, 1.0, nPoints)
f = rndL()
f.spectralIndex = -3.0
f.thetaMax = 90
x = []
y = []
for i in u:
  x.append( f.generateEnergy(i) )
for i in v:
  y.append( f.generateTheta(i) )

fig, axs = plt.subplots(1, 2, sharey=True, tight_layout=True)
axs[0].hist(np.log10(x), bins=nBins)
axs[1].hist(y, bins=nBins)
plt.yscale('log')
plt.show()
