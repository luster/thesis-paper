#!/bin/python2

import numpy as np
import matplotlib.pyplot as plt
import matplotlib.font_manager as fm
import matplotlib
# plt.style.use('ggplot')

font = {'family' : 'Adobe Caslon Pro',
        'size'   : 10}

matplotlib.rc('font', **font)



x = np.linspace(-2, 2, 20)
xs = np.linspace(-2, 2, 100)

t = -1 + 0.3*x + 1*x**2 + 0.1*x**3
y = t + np.random.randn(*t.shape)*0.5

w = np.polyfit(x, y, 2)
w2 = np.polyfit(x, y, 14)


fig, (ax1, ax2) = plt.subplots(1,2, figsize=(9, 2.5), dpi=300)
ax1.locator_params(axis='x', nbins=4)
ax1.locator_params(axis='y', nbins=8)
ax1.plot(x, t, '-', x,y, 'o', xs, np.polyval(w, xs), '--')

ax1.set_xlabel('x')
ax1.set_title('Polynomial Fit 1')
h = ax1.set_ylabel('y')
h.set_rotation(0)

ax2.locator_params(axis='x', nbins=4)
ax2.locator_params(axis='y', nbins=8)
ax2.plot(x, t, '-', x,y, 'o', xs, np.polyval(w2, xs), '--')

ax2.set_title('Polynomial Fit 2')
ax2.set_xlabel('x')
h = ax2.set_ylabel('y')
h.set_rotation(0)
plt.savefig('tex_demo.pdf', bbox_inches='tight')
