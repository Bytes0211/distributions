# Density1.py

from bokeh.plotting import figure, save, curdoc, output_file
import numpy as np
import pandas as pd


def make_data(N: int, loc: float = 0, scale: float = 2):
    rng = np.random.default_rng(246810)
    x = rng.normal(loc=loc, scale=scale, size=(N))

    df_x = pd.Series(x)
    min_val = df_x.min()
    max_val = df_x.max()
    x_bar = df_x.mean()
    std = df_x.std()
    new_data = {'min': min_val,
                'max': max_val,
                'mean': x_bar,
                'std': std,
                'data': df_x}
    return new_data


curdoc().theme = 'dark_minimal'

fig = figure(width=670,
             height=400,
             toolbar_location=None,
             title="Probability Density Tutorial\n")

data = make_data(1000, 0, 3)

bin_count = 10

# Histogram
bins = np.linspace(data['min'], data['max'], bin_count)
hist, edges = np.histogram(data['data'], density=True, bins=bins)

fig.quad(
        top=hist,
        bottom=0,
        left=edges[:-1],
        right=edges[1:],
        fill_color="dodgerblue",
        alpha=0.5,
        line_color="white",
        legend_label=f"{len(data['data'])} observatrions in {bin_count} bins")


output_file("../docs/bokeh/density1.html")
save(fig)
