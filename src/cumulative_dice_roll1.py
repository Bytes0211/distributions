# Description: This script will create a cumulative probability plot for a dice roll.
# cumulative_dice_roll1.py 

import numpy as np
from bokeh.plotting import curdoc, save, output_file
from bokeh.models import ColumnDataSource, Grid, LinearAxis, Plot, VBar

curdoc().theme = 'dark_minimal'

N_1 = 6

# 1 - 6 will be x ticks as well
x_1 = np.linspace(1, 6, N_1)
prob = 0.167
y_1 = [prob, prob * 2, prob * 3, prob * 4, prob * 5, prob * 6,] 

source_1 = ColumnDataSource(dict(x=x_1,top=y_1,))


plot_1 = Plot(
    title="Cululative Probabity (Decimal)\n", width=500, height=400,
    min_border=0, toolbar_location=None)

glyph_1 = VBar(x="x", top="top", bottom=0, width=.99, fill_color="dodgerblue")

plot_1.add_glyph(source_1, glyph_1)

# y ticks 
plot_1.y_range.start = 0
plot_1.y_range.end = 1


xaxis = LinearAxis()
plot_1.add_layout(xaxis, 'below')

yaxis = LinearAxis()
plot_1.add_layout(yaxis, 'left')


# add grids 
plot_1.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
plot_1.add_layout(Grid(dimension=1, ticker=yaxis.ticker))


plot_1.xaxis.axis_label = 'Dice Rolls'
plot_1.yaxis.axis_label = 'Probability'

curdoc().add_root(plot_1)

output_file('../docs/bokeh/cumulative_dice_roll1.html')
save(plot_1)

