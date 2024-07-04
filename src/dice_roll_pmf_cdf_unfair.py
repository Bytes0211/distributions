#
# dice_roll_pmf_cdf_unfair.py - This script will plot the PMF and CDF of a dice roll with a rigged die

import numpy as np
from bokeh.layouts import row
from bokeh.io import curdoc, save, output_file
from bokeh.models import ColumnDataSource, Grid, LinearAxis, Plot, VBar

curdoc().theme = 'dark_minimal'

N = 6

# 1 - 6 will be x ticks as well
x = np.linspace(1, 6, N)
prob2 = 0.25
y5 = [prob2, prob2, 0, 0, prob2,  prob2]

source5 = ColumnDataSource(dict(x=x,top=y5,))

p3 = Plot(
    title="PMF Of Rolling With Rigged Die\n", width=500, height=400,
    min_border=0, toolbar_location=None)

glyph5 = VBar(x="x", top="top", bottom=0, width=.99, fill_color="dodgerblue")

p3.add_glyph(source5, glyph5)

# y ticks 
p3.y_range.start = 0
p3.y_range.end = 1


xaxis = LinearAxis()
p3.add_layout(xaxis, 'below')

yaxis = LinearAxis()
p3.add_layout(yaxis, 'left')


# add grids 
p3.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
p3.add_layout(Grid(dimension=1, ticker=yaxis.ticker))


p3.xaxis.axis_label = 'Dice Rolls'
p3.yaxis.axis_label = 'Probability'

# curdoc().add_root(p3) and save are not compatible
# curdoc().add_root(p3)

# CUMULATIVE PLOT

N = 6

y6 = [prob2, prob2 * 2, prob2 * 2, prob2 * 2, prob2 * 3, prob2 * 4,] 

source5 = ColumnDataSource(dict(x=x,top=y6,))

p4 = Plot(
    title="CDF Of Rolling With Rigged Die\n", width=500, height=400,
    min_border=0, toolbar_location=None)

glyph6 = VBar(x="x", top="top", bottom=0, width=.99, fill_color="dodgerblue")

p4.add_glyph(source5, glyph6)

# y ticks 
p4.y_range.start = 0
p4.y_range.end = 1


xaxis = LinearAxis()
p4.add_layout(xaxis, 'below')

yaxis = LinearAxis()
p4.add_layout(yaxis, 'left')


# add grids 
p4.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
p4.add_layout(Grid(dimension=1, ticker=yaxis.ticker))

p4.xaxis.axis_label = 'Dice Rolls'
p4.yaxis.axis_label = 'Probability'

# curdoc().add_root(p4) and save are not compatible
# curdoc().add_root(p4)

output_file('../docs/bokeh/dice_roll_pmf_cdf_unfair.html')
save(row(p3, p4))


