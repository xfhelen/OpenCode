# -*- coding: utf-8 -*-
"""
Created on Mon Dec 19 21:28:46 2016

@author: xfhelen
#############matplotlib###############
"""
import matplotlib.pyplot as plt
import numpy as np

fig = plt.figure()
ax1 = fig.add_subplot(2,2,1)
ax2 = fig.add_subplot(2,2,2)
ax3 = fig.add_subplot(2,2,3)
ax4 = fig.add_subplot(2,2,4)
ax1.hist(np.random.randn(100), bins = 20, color = 'k', alpha = 0.3)
ax2.scatter(np.arange(30), np.arange(30)+3*np.random.randn(30))
x = np.linspace(0, 1)
y = np.sin(4 * np.pi * x) * np.exp(-5 * x)
ax3.fill(x, y, 'r')

### subplot ####
# fake data
np.random.seed(937)
data = np.random.lognormal(size=(37, 4), mean=1.5, sigma=1.75)
labels = list('ABCD')
fs = 10  # fontsize

# demonstrate how to toggle the display of different elements:
fig, axes = plt.subplots(nrows=2, ncols=3, figsize=(6, 6))
axes[0, 0].boxplot(data, labels=labels)
axes[0, 0].set_title('Default', fontsize=fs)
axes[0, 1].boxplot(data, labels=labels, showmeans=True)
axes[0, 1].set_title('showmeans=True', fontsize=fs)
axes[0, 2].boxplot(data, labels=labels, showmeans=True, meanline=True)
axes[0, 2].set_title('showmeans=True,\nmeanline=True', fontsize=fs)
axes[1, 0].boxplot(data, labels=labels, showbox=False, showcaps=False)
axes[1, 0].set_title('Tufte Style \n(showbox=False,\nshowcaps=False)', fontsize=fs)
axes[1, 1].boxplot(data, labels=labels, notch=True, bootstrap=10000)
axes[1, 1].set_title('notch=True,\nbootstrap=10000', fontsize=fs)
axes[1, 2].boxplot(data, labels=labels, showfliers=False)
axes[1, 2].set_title('showfliers=False', fontsize=fs)
for ax in axes.flatten():
    ax.set_yscale('log')
    ax.set_yticklabels([])
fig.subplots_adjust(hspace=0.4)
plt.show()

#### subplot_adjust ####
fig2, axes2 = plt.subplots(2 , 2, sharex=True, sharey=True)
for i in range(2):
    for j in range(2):
        axes2[i , j].hist(np.random.randn(500), color = 'b', bins = 50, alpha = 0.5)
plt.subplots_adjust(wspace=0, hspace=0)

fig3 = plt.figure()
axes4 = plt.plot(np.random.randn(500), linestyle = '--', color = 'r', marker = 'o')
plt.axis([0 , 500 , -5, 5])


