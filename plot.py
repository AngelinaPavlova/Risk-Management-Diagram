import matplotlib.pyplot as plt
from matplotlib.lines import Line2D
import numpy as np
import sys

SRC = sys.argv[1]
BASE_SCATTER_SIZE = 100
SCATTER_STEP = 400
COLORS = ['red', 'orange', 'yellow', 'green', 'grey']
ALPHA = 0.9

data = {}
value_types = []
names = []

class Item:
    def __init__(self, value, value_type):
        self.value = value
        self.value_type = value_type
        self.mult = 0

with open(SRC, 'rt') as f:
    f.readline()
    for l in f:
        tmp = l.split(';')
        name = tmp[0]
        value = tmp[1]
        value_type = tmp[2]

        if name not in data:
            data[name] = []

        data[name].append(Item(int(value), value_type))

        if value_type not in value_types:
            value_types.append(value_type)
        if name not in names:
            names.append(name)

names.sort()
value_types.sort()

fig = plt.figure()
ax = plt.subplot(111)

for n, lst in data.items():
    by_values = {}
    for item in lst:
        if item.value not in by_values:
            by_values[item.value] = []
        by_values[item.value].append(item)

    for val, item_lst in by_values.items():
        for idx, item in enumerate(item_lst):
            idx = len(item_lst) - idx - 1
            scatter_size = BASE_SCATTER_SIZE + SCATTER_STEP*idx
            ax.scatter([names.index(n),], [item.value,], s=scatter_size,
                        color=COLORS[value_types.index(item.value_type) % len(COLORS)],
                        alpha=ALPHA, edgecolors='black')

ax.set_xticks([i for i in range(len(names))])
ax.set_xticklabels(names)

legend_elements = []
for n in value_types:
    legend_elements.append(Line2D([0], [0], marker='o', color='w',
                           markerfacecolor=COLORS[value_types.index(n) % len(COLORS)],
                           label=n, markersize=15, alpha=ALPHA))

box = ax.get_position()
ax.set_position([box.x0, box.y0, box.width * 0.8, box.height])

ax.legend(handles=legend_elements, loc='center left', bbox_to_anchor=(1, 0.5))

plt.grid(True)

plt.show()
