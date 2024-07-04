# Purpose: To demonstrate the probability mass function and cumulative distribution function of rolling a dice
# rol_dice_pmf_cdf_ex.py
import numpy as np
from bokeh.layouts import row 
from bokeh.io import curdoc, save, output_file
from bokeh.models import ColumnDataSource, Grid, LinearAxis, Plot, VBar

curdoc().theme = 'dark_minimal'

N = 6

# 1 - 6 will be x ticks as well
x = np.linspace(1, 6, N)
prob = 0.167
y1 = [prob, prob, prob, 0, prob, prob]
y2 = [0, 0, 0, prob, 0, 0]

source1 = ColumnDataSource(dict(x=x,top=y1,))
source2 = ColumnDataSource(dict(x=x,top=y2,))

p1 = Plot(
    title="PMF - Discrete Probabaility Or Rolling a 4\n", width=500, height=400,
    min_border=0, toolbar_location=None)

glyph1 = VBar(x="x", top="top", bottom=0, width=.99, fill_color="dodgerblue")
glyph2 = VBar(x="x", top="top", bottom=0, width=.99, fill_color="firebrick", fill_alpha = 0.6)

p1.add_glyph(source1, glyph1)
p1.add_glyph(source2, glyph2)

# y ticks 
p1.y_range.start = 0
p1.y_range.end = 1


xaxis = LinearAxis()
p1.add_layout(xaxis, 'below')

yaxis = LinearAxis()
p1.add_layout(yaxis, 'left')


# add grids 
p1.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
p1.add_layout(Grid(dimension=1, ticker=yaxis.ticker))


p1.xaxis.axis_label = 'Dice Rolls'
p1.yaxis.axis_label = 'Probability'

# curdoc().add_root(p1) and save function are not compatible
# curdoc().add_root(p1)

# CUMULATIVE PLOT

N = 6

prob = 0.167
y3 = [prob, prob * 2, prob * 3, 0 , prob * 5, prob * 6,] 
y4 = [0, 0, 0, prob *4, 0, 0 ] 

source3 = ColumnDataSource(dict(x=x,top=y3,))
source4 = ColumnDataSource(dict(x=x,top=y4,))


p2 = Plot(
    title="Cumulative Probability Of Rolling a 4 OR Less\n", width=500, height=400,
    min_border=0, toolbar_location=None)

glyph3 = VBar(x="x", top="top", bottom=0, width=.99, fill_color="dodgerblue")
glyph4 = VBar(x="x", top="top", bottom=0, width=.99, fill_color="firebrick", fill_alpha = 0.6)

p2.add_glyph(source3, glyph3)
p2.add_glyph(source4, glyph4)

# y ticks 
p2.y_range.start = 0
p2.y_range.end = 1


xaxis = LinearAxis()
p2.add_layout(xaxis, 'below')

yaxis = LinearAxis()
p2.add_layout(yaxis, 'left')


# add grids 
p2.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
p2.add_layout(Grid(dimension=1, ticker=yaxis.ticker))


p2.xaxis.axis_label = 'Dice Rolls'
p2.yaxis.axis_label = 'Probability'

# curdoc().add_root(p2) and save function are not compatible
# curdoc().add_root(p2)

output_file('../docs/bokeh/dice_roll_pmf_cdf_ex.html')
save(row(p1, p2))


