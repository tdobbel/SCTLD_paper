import numpy as np
import matplotlib.pyplot as plt
import os

data = np.load("indicators_v2.npy", allow_pickle=True).item()
indicators = ["WCL", "outdegree", "fraction_exchanged", "fraction_lost", "isolation"]
titles = ["WCL [km]", "Out-degree", "Fraction exchanged", "Fraction lost", "Isolation"]
labels = ["mean"+"\n"+"currents", "bottom"+"\n"+"currents", "surface"+"\n"+"currents"]
fig, _axs = plt.subplots(ncols=3, nrows=2, sharex=False)
axs = _axs.flat

meanpointprops = dict(marker='s', markeredgecolor='black', markerfacecolor='white', markersize=3)

colors = ['#1f77b4', '#ff7f0e', '#2ca02c']
for i in range(len(indicators)):
    indicator = indicators[i]
    vector = []
    axs[i].set_title(titles[i], fontsize=10)
    for mode in ["baro", "bbl", "sbl"]:
        alpha = 1 if indicator != "WCL" else 1e-3
        vector += [ data[mode,indicator]*alpha ]
    bp = axs[i].boxplot(vector, labels=labels, patch_artist=True, showmeans=True, meanprops=meanpointprops, flierprops=dict(markersize=2, linewidth=.1))
    icolor = 0
    for patch in bp['boxes']:
        patch.set_facecolor(colors[icolor])
        icolor += 1
    for patch in bp["medians"]:
        patch.set_color("black")
    if indicator not in ["WCL", "outdegree"]:
        axs[i].set_ylim(0,1)
    axs[i].tick_params(axis='both',labelsize=8)
axs[-1].set_visible(False)
fig.set_size_inches(11, 6)
plt.subplots_adjust(hspace=.4)
plt.savefig("connect_paper.png", dpi=300, bbox_inches="tight")
os.system("eog connect_paper.png")
# plt.show()
    
