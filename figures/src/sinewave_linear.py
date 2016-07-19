#!/bin/python2

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib
# plt.style.use('ggplot')

font = {'family' : 'Adobe Caslon Pro',
        'size'   : 10}

matplotlib.rc('font', **font)

x = np.linspace(-np.pi, np.pi, 20)
xs = np.linspace(-4, 4, 120)

t = np.sin(x)
y = t + np.random.randn(*t.shape)*0.2

def Phi(x):

	return np.vstack([x, np.ones(x.size)]).T

design = Phi(x)
print design.shape
print y.shape
w, _, _, _ = np.linalg.lstsq(design, y)
print 'w', w.shape 

print 'Phi(xs)', Phi(xs).shape
yhat = np.matmul(Phi(xs),w)
print 'yhat', yhat.shape	

fig, ax1 = plt.subplots(1,1, figsize=(4.5, 3), dpi=300)
ax1.locator_params(axis='x', nbins=4)
ax1.locator_params(axis='y', nbins=8)
ax1.plot(xs, np.sin(xs), '-', x,y, 'o', xs, yhat, '--')

ax1.set_xlabel('x')
ax1.set_title('Linear Fit')
h = ax1.set_ylabel('y')
h.set_rotation(0)
ax1.set_ylim([-1.5,1.5])


plt.tight_layout()
plt.savefig('sinewave_lin.pdf', bbox_inches='tight')
