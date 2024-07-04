# The PDF
The Probability Density Function (PDF) is a function that describes the likelihood of a random variable taking on a particular value. The PDF is used to specify theprobability of the random variable falling within a particular range of values, as opposed to taking on any one value. This probability is given by the integral of the variable’s PDF over that range — that is, it is given by the area under the density function but above the horizontal axis and between the lowest and greatest values of the range.

Some key properties of the PDF are:

- The PDF itself does not give probabilities directly. Instead, it describes the relative likelihood of the random variable taking on a particular value.

- The probability of the random variable falling within a particular range of values is given by the integral of the PDF over that range.

- The PDF is nonnegative everywhere, and its integral over the entire space is equal to 1, where 1 represents the entire space of possible values of the random variable.

The formula for the PDF is given by the derivative of the cumulative distribution function (CDF) with respect to the random variable. The CDF is the function that maps values of the random variable to their cumulative probability. The PDF is the derivative of the CDF, which means that the PDF is the rate of change of the CDF.

$PDF(x) = \frac{1}{\sigma\sqrt{2\pi}} \exp\left[-\frac{1}{2} \left(\frac{x-\overline{x}}{\sigma}\right)^2 \right]$

where:

- x is the value of the random variable

- $\overline{x}$ is the mean of the random variable

- $\sigma$ is the standard deviation of the random variable

## Continuous Random Variables 
Continuous variables can take on infinite number of possible values such as the height of a person, weight of an animal<br>
time required to run a mile. <br/>
<br>
Examples:

- a person's height can be 157.48 cm or 82.55 cm
 
- An animals can be be 22.4 Kg, 23.138 kg

A popular way of describing PDF with continuous variables is using weight or height. Here I will sample height of women to to describe PDF

- Height Statistics:<br><br>- $\text{ count: 1000}$<br><br>\- $\text{ standard deviation:  12.24}$<br><br>- $\text{ min:  131.36 }$<br><br>- $\text{ max:  206.14 }$<br>

<iframe src="./docs/bokeh/height-pdf.html"
     sandbox="allow-same-origin allow-scripts"
     width="500%"
     height="400"
     scrolling="no"
     seamless="seamless"
     frameborder="0">
 </iframe>
<br>

