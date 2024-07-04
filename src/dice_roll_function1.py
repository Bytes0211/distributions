
# dice_roll_function1.py

import numpy as np
from bokeh.layouts import column
from bokeh.plotting import curdoc, show, output_file, save 
from bokeh.models import ColumnDataSource, Grid, LinearAxis, Plot, VBar, Div, TeX

curdoc().theme = 'dark_minimal'

N = 6

# 1 - 6 will be x ticks as well
x = np.linspace(1, 6, N)
y = [.167] * 6

source = ColumnDataSource(dict(x=x,top=y,))

plot = Plot(
    title="PMF - Dice Role Probabity (Fractions)\n", width=500, height=400,
    min_border=0, toolbar_location=None)

glyph = VBar(x="x", top="top", bottom=0, width= 1, fill_color="dodgerblue")
plot.add_glyph(source, glyph)

# y ticks
plot.y_range.start = 0
plot.y_range.end = .668


xaxis = LinearAxis()
plot.add_layout(xaxis, 'below')

yaxis = LinearAxis()
plot.add_layout(yaxis, 'left')


# add grids
plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))

curdoc().add_root(plot)

plot.xaxis.axis_label = "Number of Dice Rolls"
plot.yaxis.axis_label = "Dice Roll Probabilities"

# for some reason major_label_overrides is not working in this notebook.
plot.yaxis.ticker = [0, 0.1, 0.2, 0.3, 0.4, 0.5, 0.6]
plot.yaxis.major_label_overrides = {
    0: TeX(r"0"),
    0.1: TeX(r"0.10"),
    0.2: TeX(r"0.20"),
    0.3: TeX(r"0.30"),
    0.4: TeX(r"0.40"),
    0.5: TeX(r"0.50"),
    0.6: TeX(r"0.60"),
}


div = Div(text=r"""
<p>
PMF<br>
The probability of rolling a 1 on a six sided dice is 1/6 or .167
<p />
<br>

""")

# show(column(plot, div))
output_file("../docs/bokeh/dice_roll_function1.html")
save(plot)


