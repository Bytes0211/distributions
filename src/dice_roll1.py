
import numpy as np

from bokeh.plotting import curdoc
from bokeh.io import export_png
from bokeh.models import ColumnDataSource, Grid, LinearAxis, Plot, VBar, TeX

curdoc().theme = 'dark_minimal'

x = list(range(0, 4))
y = [1, 3, 3, 1]

source = ColumnDataSource(dict(x=x,top=y,))

plot = Plot(
    title="Discrete Distribution\nFor Random Variable X"
    , width=500
    , height=400
    , min_border=0
    , toolbar_location=None
)


glyph = VBar(x="x", top="top", bottom=0, width=1, fill_color="dodgerblue")
plot.add_glyph(source, glyph)

xaxis = LinearAxis()
plot.add_layout(xaxis, 'below')

yaxis = LinearAxis()
plot.add_layout(yaxis, 'left')

plot.add_layout(Grid(dimension=0, ticker=xaxis.ticker))
plot.add_layout(Grid(dimension=1, ticker=yaxis.ticker))


plot.yaxis.ticker = [0, 0.5, 1, 1.5, 2, 2.5, 3]
plot.yaxis.major_label_overrides = {
    0: TeX(r"\dfrac{1}{8}"),
    0.5: TeX(r""),
    1: TeX(r"\dfrac{1}{8}"),
    1.5: TeX(r""),
    2: TeX(r"\dfrac{1}{4}"),
    2.5: TeX(r""),
    3: TeX(r"\dfrac{3}{8}"),
}

plot.yaxis.axis_label = 'Probabilities'
plot.xaxis.axis_label = 'Coin Tosses'

curdoc().add_root(plot)
export_png(plot, filename="../docs/dice_roll1.png")
