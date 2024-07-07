# Density1.py

from bokeh.plotting import figure, save, curdoc, output_file
from bokeh.layouts import row
import numpy as np
import pandas as pd
import data as dt
calc = dt.Data()

data = calc.make_data(N=2000, mu=0, sigma=3)

curdoc().theme = 'dark_minimal'

fig1 = figure(width=450,
              height=350,
              toolbar_location=None,
              title="Probability Density - 10 bins\n")


bin_count1 = 10

# Histogram1
bins1 = np.linspace(data['min'], data['max'], bin_count1)
hist1, edges = np.histogram(sorted(data['X']), density=True, bins=bins1)

fig1.quad(
        top=hist1,
        bottom=0,
        left=edges[:-1],
        right=edges[1:],
        fill_color="dodgerblue",
        alpha=0.5,
        line_color="white",
        legend_label=f"{bin_count1} bins")

fig2 = figure(width=450,
              height=350,
              toolbar_location=None,
              title="Probability Density - 2 bins\n")

bin_count2 = 3

# Histogram1
print(f'MIN: {data["min"]}, MAX: {data["max"]}')
bins2 = np.linspace(data['min'], data['max'], bin_count2)
hist2, edges = np.histogram(sorted(data['X']), density=True, bins=bins2)
fig2.quad(
        top=hist2,
        bottom=0,
        left=edges[:-1],
        right=edges[1:],
        fill_color="dodgerblue",
        alpha=0.5,
        line_color="white",
        legend_label=f"{bin_count2} bins")


output_file("../docs/bokeh/density1.html")
save(row(fig1, fig2))
