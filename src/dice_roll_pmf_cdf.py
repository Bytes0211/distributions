# Visualizing the relationship between the probability mass function (PMF)
# and the cumulative distribution function (CDF) of a discrete random variable.
# The discrete random variable in this case is the sum of two dice rolls.
# dice_roll_pmf_cdf.py is a Python script that generates a bar plot of the
# PMF and a step plot of the CDF of the sum of two dice rolls.


import numpy as np
from bokeh.plotting import curdoc, save, output_file 
from bokeh.models import ColumnDataSource, Grid, LinearAxis, Plot, VBar
from bokeh.layouts import row

curdoc().theme = 'dark_minimal'

N_1 = 6

# 1 - 6 will be x ticks as well
x_1 = np.linspace(1, 6, N_1)
prob = 0.167
y_1 = [prob, prob * 2, prob * 3, prob * 4, prob * 5, prob * 6,] 

source_1 = ColumnDataSource(dict(x=x_1, top=y_1,))


plot_1 = Plot(
    title="Cululative Probabity (Decimal)\n", width=400, height=300,
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

# cannot us curdoc().add_root() and save() at the same time
# curdoc().add_root(plot_1)

# plot_

N_2 = 6

# 1 - 6 will be x ticks as well
x_2 = np.linspace(1, 6, N_2)
prob = 0.167
y_2 = [prob] * 6 

source_2 = ColumnDataSource(dict(x=x_2, top=y_2,))


plot_2 = Plot(
    title="Probabity Density(Decimal)\n", width=400, height=300,
    min_border=0, toolbar_location=None)

glyph_2 = VBar(x="x", top="top", bottom=0, width=.99, fill_color="dodgerblue")

plot_2.add_glyph(source_2, glyph_2)

# y ticks 
plot_2.y_range.start = 0
plot_2.y_range.end = 1


xaxis = LinearAxis()
plot_2.add_layout(xaxis, 'below')

yaxis = LinearAxis()
plot_2.add_layout(yaxis, 'left')


# add grids 
plot_2.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
plot_2.add_layout(Grid(dimension=1, ticker=yaxis.ticker))


plot_2.xaxis.axis_label = 'Dice Rolls'
# plot_2.yaxis.axis_label = 'Probability'

# cannot us curdoc().add_root() and save() at the same time
# curdoc().add_root(plot_2) 

output_file('../docs/bokeh/dice_roll_pmf_cdf.html')
save(row(plot_2, plot_1))

     

