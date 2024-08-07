# Introductoin To Probability Distributions
A comprehensive look at probability distributions components, applications in Python

## Introduction
Probability distributions describe how the values of a random variable are distributed. They are fundamental in statistics and are categorized mainly into two types based on the nature of the random variable they describe:

In short a distribution is a the possible values a variable can take and how frequently they occur<br>
<br>
<b>Probability Distribution Notations:</b><br>

 - X,Y - random variables
 - x,y, i - regular variables (specific realizations of the random variables)
 - $E(X)$ - Expected value of X
 - $Var(X)$ - Variance of X
<br>

More notations will be introduced as we go along<br>

### Types of Probability Distributions
1. **Discrete Probability Distributions**: These apply to discrete random variables, which are variables that take on a countable number of distinct values. The distribution of a discrete random variable is described by a Probability Mass Function (PMF), which gives the probability that the random variable takes on a specific value.

2. **Continuous Probability Distributions**: These apply to continuous random variables, which can take on any value within a continuous range. The distribution of a continuous random variable is described by a Probability Density Function (PDF), which, when integrated over a range of values, gives the probability that the random variable falls within that range. The PDF itself does not give probabilities directly but rather the relative likelihood of the random variable being near a particular value.

Both types of distributions can be further characterized by their Cumulative Distribution Function (CDF), which gives the probability that the random variable is less than or equal to a certain value. For discrete random variables, the CDF is the cumulative sum of the PMF up to that value. For continuous random variables, the CDF is the integral of the PDF up to that value, representing the area under the PDF curve from negative infinity to that value.

### Random Variables
A random variable is a variable whose value is subject to variations due to chance. It can take on a set of possible values, each with an associated probability. Random variables can be classified as either discrete or continuous, depending on the nature of the values they can take.

A Random Variable in its simplest form is a function. In probability we often use random variables to represent random events. A Random Variable allows you to convert a real world experiment into a numerical value that we can perform some mathematics on.

#### Random Variable Example
Say you are sitting on a park bench, enjoying the nice weather as you people watch. You decide to count how many people walking by in a five minute period. You note the hair color and height of each person. One observation would be Person1 has brown hair and his height is 165 cm.<br>
<br>
After you complete this experiment you ask yourself a few questions:<br>

1. How many people walk passed ? <br>
&emsp;10 people passed so therefore the sample space is 10. This sample space is also referred to as the <b>outcome</b>:<br>
&emsp;&emsp;$\text{Outcome }\Rightarrow \Omega_1 = 10~people$<br>
<br>
&emsp;When working with the sample space in terms of distributons it is noted as a <b>random variable:</b><br>
&emsp;&emsp;$\text{Sample Space } \Omega_1 \Rightarrow \text{Random Variable}X_1 = 10$<br>
<br>

2. What was the average height of the people who walked pass?<br>
&emsp;&emsp;$\text{Outcome }\Rightarrow \Omega_2 = 165.32~cm$<br>
&emsp;&emsp;$\text{Random Variable }\Omega_2 \Rightarrow X_2(x) = 165.32$<br>
<br>

### Probabilites (Frequencies)
Probability Frequency Distributions more commonly referred to as <b>Probabilities</b> is the measure of the likelihood of an outcome based on how often it is featured in the sample space ($\Omega$). The probability of an event is a number between 0 and 1, where 0 indicates that the event will not occur and 1 indicates that the event will occur. The sum of the probabilities of all possible outcomes in the sample space is equal to 1.

The Frequency Distribution Table below details the roll of 2 dice. The Sum column is the sum of the roll of the two dice from 2 ( 1 + 1) to 12 (6 + 6) with the highest frequency being the sum of 7. There are 6 different ways to roll a 7 resulting in a probability of $\dfrac{1}{6}$. Each probability is equal to the Frequency divided by the Sample Space $\Omega$. For example the frequency for 7 is 6, resulting in $\dfrac{6}{36}$ or $\dfrac{1}{6}$.<br>
<br>
This is is the typical way to construct probabilities when we have a <b>Finite</b> amount of elements.<br>
<br>
<b>Frequency Distribution Table for the Sum of Rolling Two Dice:</b><br>

|  Sum  |  Frequency  |   Probability   |
|:-----:|:-----------:|:---------------:|
|   2   |      1      | $\dfrac{1}{36}$ |
|   3   |      2      | $\dfrac{1}{18}$ |
|   4   |      3      | $\dfrac{1}{12}$ |
|   5   |      4      | $\dfrac{1}{9}$  |
|   6   |      5      | $\dfrac{5}{36}$ |
|   7   |      6      | $\dfrac{1}{6}$  |
|   8   |      5      | $\dfrac{5}{36}$ |
|   9   |      4      | $\dfrac{1}{9}$  |
|  10   |      3      | $\dfrac{1}{12}$ |
|  11   |      2      | $\dfrac{1}{18}$ |
|  12   |      1      | $\dfrac{1}{36}$ | 

<br>

### Distribution Example
It helps me to start with an example when I am trying to grasp something that is not initially clear to me. So that is what I will do here with a Distribution.
With the use of a fair coin, I will perform 8 trials which will entail 3 tosses. These 8 trials will be represented with the random variable X. The possible outcomes of the three tosses are:<br>
<br>
<b>H = heads<br>
T = tails<br></b>

* HHH
* HHT
* HTH
* THH
* TTH
* THT
* HTT
* TTT

<b>The Possible Outcomes Of X:</b><br>
There are FOUR possible values for X for each trial:<br>

* you can flip THREE times and get ZERO Heads (TTT)
* you can flip THREE times and get ONE Heads (TTH, THT, HTT)
* you can flip THREE times and get TWO Heads (HTT, HTH, THH)
* you can flip THREE times and get THREE Heads (HHH)

<b>The Probabilities of the Possible Outcomes Of X $\bigg(\dfrac{\text{successful trial(s)}}{\text{total trials}}\bigg)$:</b><br>

* Probability of getting 0 Heads (TTT): $P(X = 0) = \dfrac{1}{8} = 0.125$
* Probability of getting 1 Heads (TTH, THT, HTT): $P(X = 3) = \dfrac{3}{8} = 0.3755$
* Probability of getting 2 Heads (HTT, HTH, THH): $P(X = 3) = \dfrac{3}{8} = 0.375$
* Probability of getting 3 Heads (HHH): $P(X = 3) = \dfrac{1}{8} = 0.125$
<br><br>

<b>Plot The Distribution Of X</b><br>

The plot below shows the distribution of X. The x-axis represents the possible values of X (0, 1, 2, 3) and the y-axis represents the probability of each value occurring. The distribution is symmetric around the mean value of 1.5, with the highest probability of $0.375$ occurring at X = 1 and X = 2 and a value of $0.125$ at X = 0 and X =3. The distribution is discrete, as the random variable X can only take on integer values.<br>

<iframe src="https://bytes0211.github.io/distributions/bokeh/dice-roll1.html"
    sandbox="allow-same-origin allow-scripts"
    width="500%"
    height="400"
    scrolling="no"
    seamless="seamless"
    frameborder="0">
</iframe>
<br><br>

### Conclusion
Probability distributions are a fundamental concept in statistics that describe how the values of a random variable are distributed. There are two main types of probability distributions: discrete and continuous, which apply to discrete and continuous random variables, respectively. Discrete probability distributions are described by Probability Mass Functions (PMFs), while continuous probability distributions are described by Probability Density Functions (PDFs). Both types of distributions can be further characterized by their Cumulative Distribution Functions (CDFs), which give the probability that the random variable is less than or equal to a certain value. Probabilities are a measure of the likelihood of an outcome based on how often it is featured in the sample space, with the sum of the probabilities of all possible outcomes equal to 1.            
<br><br>

<span style = 'color:crimson;font-style:bold;font-size:18px'>End of Introduction</span><br><br>


