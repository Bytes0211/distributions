# The PMF
The probability mass function (PMF) is a function that describes the probability of a discrete random variable taking on a particular value. For example, if we have a random variable X that represents the outcome of rolling a fair six-sided die, the PMF of X would assign a probability to each possible outcome (1, 2, 3, 4, 5, or 6).

One roll of a dice where x denotes the number that the dice lands on, then the PDF for the outcome<br/>
can be described as:

One roll of a dice where x denotes the number that the dice lands on, then the PDF for the outcome<br/>
can be described as: 

$P(x < 1) : 0 \\ \quad \\ P(x = 1) : \dfrac{1}{6} \\ \quad \\ P(x = 2) : \dfrac{1}{6} \\ \quad \\ P(x = 3) : \dfrac{1}{6} \\ \quad \\     P(x = 4) : \dfrac{1}{6} \\ \quad \\ P(x = 5) : \dfrac{1}{6} \\ \quad \\ P(x = 6) : \dfrac{1}{6} \\ \quad \\ P(x > 6) : 0$

Its important to note that x is a discrete variable in every instance. since x takes on only integer values.

<iframe src="https://bytes0211.github.io/distributions/bokeh/dice-roll-function1.html"
     sandbox="allow-same-origin allow-scripts"
     width="500%"
     height="400"
     scrolling="no"
     seamless="seamless"
     frameborder="0">
 </iframe>

<br>
The probability of rolling a 1 on a six sided dice is 1/6 or .167
<br>

## The PMF And The CDF 
Cumulative Probability Function (CDF) measures the odds(probability) of two, three or more events happening<br>
A CDF tells us the probability that a random variable takes on a value less than or equal to x. <br>
<br>
Example:<br/>
One roll of a dice where x denotes the number that the dice lands on, then the CDF for the outcome<br/>
can be described as: 

$P(x \leq 0) : 0 \\ \quad \\ P(x \leq 1) : \dfrac{1}{6} \\ \quad \\ P(x \leq 2) : \dfrac{2}{6} \\ \quad \\ P(x \leq 3) : \dfrac{3}{6} \\ \quad \\ P(x \leq 4) : \dfrac{4}{6} \\ \quad \\ P(x \leq 5) : \dfrac{5}{6} \\ \quad \\  P(x \leq 6) : \dfrac{6}{6} \\ \quad \\ P(x \geq 6) : 0$

Note that the probability that x is less than or equal to 6 is $\dfrac{6}{6} = 1 $<br/>
This is because the dice will land on either 1, 2, 3, 4, 5, or 6 with 100%  probability<br/>

This example uses a discrete random variable, however a CDF can also be used for a<br/>
continuous random variable. 

CDF have the following properties:

- The probability of a random variable takes on a value less than the smallest possible value is zero.<br/>
- Example: A dice landing on a value less than 1 is zero.

 The probability that a random variable takes on a value less than or equal to the largest possible value is one. 
<br><br>
This conveyed graphically below: 

<iframe src="https://bytes0211.github.io/distributions/bokeh/cumulative-dice-roll1.html"
     sandbox="allow-same-origin allow-scripts"
     width="500%"
     height="400"
     scrolling="no"
     seamless="seamless"
     frameborder="0">
 </iframe>
<br>

The probability of rolling a 1 on a six sided dice is $\frac{1}{6}$ or .167
<br>
Note that I also change the range to 0 - 1

## PMF Properties 
The PMF can only be used with discrete values. You cannot use continuous random values with PDFs directly, since the probability that x taking on any exact value iszero. For example, we want to know the probability that a burger from your favorite burger joint weigh:ws exactly a quarter of a pound (0.25 lbs) Since weight is a continuous variable, it can take on an infinite number of values. A burger may actually weigh 0.250001 lbs, or 0.24 lbs., or  0.24323 lbs. The probability that a burger weighs exactly 0.25 lbs is essentially zero.

Below is a graphical representative of PMF and CDF side by side. Again for the PMF **each** roll of the dice has a 1/6 probability<br> While the CDF expresses **multiple** probabilities which are "cumulative". 


<iframe src="https://bytes0211.github.io/distributions/bokeh/dice-roll-pmf-cdf.html"
     sandbox="allow-same-origin allow-scripts"
     width="500%"
     height="400"
     scrolling="no"
     seamless="seamless"
     frameborder="0">
 </iframe>

The probability of rolling a 1 on a six sided dice is $\frac{1}{6} $$ or .167$<br>

## PMF and CDF Exmaple

* The probability of rolling a 4 is $\frac{1}{6}$ or $16.7\%$ (PDF)
* The probability of rolling a 1, 2, 3, or 4 is $\frac{4}{6}$ or $66.8 %$ (CDF)

<iframe src="https://bytes0211.github.io/distributions/bokeh/dice-roll-pmf-cdf-ex.html"
     sandbox="allow-same-origin allow-scripts"
     width="500%"
     height="400"
     scrolling="no"
     seamless="seamless"
     frameborder="0">
 </iframe>
<br>
Lets pretend that the dice is rigged in such a way that you cannot roll a 3 or 4. <br>
This is what the discreet probability (PMF) and the cumulative probability (CDF) would look like<br>
<br>

On the left you the discreet probability with a rigged die that doesn't allow the roll of 3 or 4<br>
The probability of rolling a 1, 2, 5, or 6 is $P(X 1, 2, 5, 6) = \frac{1}{4}$ or $25.0 \%$
<br>

On the right you have the cumulative probability of rolling a 1, 2, 5 or 6 which is $\frac{4}{6}$ 
or $0.668 \%$<br>

$P(X \leq 4) = P(x = 1) + P(x = 2) + P(x = 3) + P(x = 4)$
<br><br>
Note that for the cumulative (CDF) the probability of getting 2 or less is the same for getting 3, 4 or less<br>
That is because there are no values for 3 or 4, so there is no cumulative effect<br
</span>
<p />

<iframe src="https://bytes0211.github.io/distributions/bokeh/dice-roll-pmf-cdf-unfair.html"
     sandbox="allow-same-origin allow-scripts"
     width="500%"
     height="400"
     scrolling="no"
     seamless="seamless"
     frameborder="0">
 </iframe>
<br>
On the left you the discreet probability with a rigged die that doesn't allow the roll of 3 or 4<br>
$P(X 1, 2, 5, 6) = \frac{1}{4}$ or $ 25.0 \%$
<br>
On the right you have the cumulative probability of rolling a 1, 2, 5 or 6 which is $\frac{4}{6}$
or $66.8 \%$<br>
<br>
$P(X \leq 4) = P(x = 1) + P(x = 2) + P(x = 3) + P(x = 4)$
<br><br>
Note that for the cumulative (CDF) the probability of getting 2 or less is the same for getting 3, 4 or less<br>
That is because there are no values for 3 or 4, so there is no cumulative effect<br>
:
## PMF Applications
Probability Mass Functions (PMFs) are used in various fields and applications to describe the distribution of discrete random variables. Here is a list of a few of the many applications of PMFs:

- <b>Statistics and Data Analysis</b>: PMFs are used to summarize and visualize the distribution of discrete data, helping in understanding the likelihood of different outcomes.

- <b>Quality Control and Manufacturing</b>: PMFs help in assessing the probability of defects in batches of products, enabling companies to maintain quality standards.

- <b>Finance and Risk Management</b>: PMFs are used to model the probability of discrete outcomes in financial scenarios, such as the number of defaults on loans or the occurrence of specific market conditions.

- <b>Health Sciences</b>: PMFs model the distribution of discrete outcomes in medical research and public health, such as the number of cases of a disease or the number of patients responding to a treatment.
