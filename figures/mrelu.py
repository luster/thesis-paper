from __future__ import division
import matplotlib.pyplot as plt
import numpy as np


plt.rc('text', usetex=True)
plt.rc('font', family='serif')
plt.rc('font', size=10)
params = {'legend.fontsize': 6,
          }
plt.rcParams.update(params)

n = np.linspace(-1, 1, 2000)
eps = 10**-5
x = np.piecewise(n, [n<eps, n>=eps], [lambda n: -eps/(n-1-eps), lambda n: n])

plt.figure(figsize=(4.5,3), dpi=300)
plt.xlabel('x')
plt.ylabel('y')#, rotation=0)
plt.title('Modified Rectified Linear Activation Function (mReLU)')
plt.plot(n, x)
plt.ylim(-.2,.8)
outfname = 'mrelu.pdf'
plt.tight_layout()
plt.savefig(outfname, format='pdf', bbox_inches='tight')
