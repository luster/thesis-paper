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
	def phi(x, mu, sigma=1):
		return np.exp(-(x-mu)**2/sigma)

	return np.vstack([np.vstack([phi(x, m) for m in list(np.linspace(-3,3,6))]), np.ones(x.size)]).T

design = Phi(x)
print design.shape
print y.shape
w, _, _, _ = np.linalg.lstsq(design, y)
print 'w', w.shape 

print 'Phi(xs)', Phi(xs).shape
yhat = np.matmul(Phi(xs),w)
print 'yhat', yhat.shape	

fig, ((ax1, ax2), (ax3, ax4)) = plt.subplots(2,2, figsize=(9, 6), dpi=300)
ax1.locator_params(axis='x', nbins=4)
ax1.locator_params(axis='y', nbins=8)
ax1.plot(xs, np.sin(xs), '-', x,y, 'o', xs, yhat, '--')

ax1.set_xlabel('x')
ax1.set_title('Fit 1')
h = ax1.set_ylabel('y')
h.set_rotation(0)
ax1.set_ylim([-1.5,1.5])

ax2.locator_params(axis='x', nbins=4)
ax2.locator_params(axis='y', nbins=8)
ax2.plot(xs, Phi(xs))

ax2.set_title('Bases for Fit 1')
ax2.set_xlabel('x')
h = ax2.set_ylabel('y')
h.set_rotation(0)

def Phi(x):
    def phi(x, mu, sigma=3.2):
        return 1/(1+np.exp(-sigma*(x-mu)))

    return np.vstack([np.vstack([phi(x, m) for m in list(np.linspace(-3,3,6))]), np.ones(x.size)]).T

design = Phi(x)
print design.shape
print y.shape
w, _, _, _ = np.linalg.lstsq(design, y)
print 'w', w.shape 

print 'Phi(xs)', Phi(xs).shape
yhat = np.matmul(Phi(xs),w)
print 'yhat', yhat.shape

ax3.locator_params(axis='x', nbins=4)
ax3.locator_params(axis='y', nbins=8)
ax3.plot(xs, np.sin(xs), '-', x,y, 'o', xs, yhat, '--')

ax3.set_xlabel('x')
ax3.set_title('Fit 2')
h = ax3.set_ylabel('y')
h.set_rotation(0)
ax3.set_ylim([-1.5,1.5])

ax4.locator_params(axis='x', nbins=4)
ax4.locator_params(axis='y', nbins=8)
ax4.plot(xs, Phi(xs))

ax4.set_title('Bases for Fit 2')
ax4.set_xlabel('x')
h = ax4.set_ylabel('y')
h.set_rotation(0)

plt.tight_layout()
plt.savefig('sinewave.pdf', bbox_inches='tight')
