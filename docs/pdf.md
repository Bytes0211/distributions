# Probability Density Function
The Probability DensiPy Function (PDF) is a function that describes the likelihood of a continuous random variable taking on a particular value. The PDF is used with continuous random variables, which can take on any value within a continuous range. Key points about the PDF include:

- The PDF itself does not give probabilities directly. Instead, it describes the relative likelihood of the random variable being near a particular value.
- The probability of the random variable falling within a particular range is given by the integral of the PDF over that range.
- The area under the entire PDF curve equals 1, representing the total probability of all possible outcomes.

The PDF is crucial for understanding the distribution of continuous data and for calculating probabilities over intervals for continuous random variables.

## Probability Density Components
* **observation** - a data point in the sample
* **probability** - the likelihood of an outcome of an observation 
* **probability density** - the relationship between the observation and its probability 
* **probability distribution** - the overall shape of all the probability densities from the sample
* **Probability Density Function (PDF)** - performs calculations of probabilities for a specific outcomes of a random variable

## PDF Estimation
Given a random variable, we are interested in the density of its probabilities. For example, given a random sample of a variable, we might want to know things like the shape of the probability distribution, the most likely value, the spread of values, and other properties.<br><br>
Knowing the probability distribution for a random variable can help to calculate moments of the distribution, like the mean and variance, but can also be useful for other more general considerations, like determining whether an observation is unlikely or very unlikely and might be an outlier or anomaly.<br><br>
The problem is, we may not know the probability distribution for a random variable. We rarely do know the distribution because we don’t have access to all possible outcomes for a random variable. In fact, all we have access to is a sample of observations. As such, we must select a probability distribution<br><br>
This problem is referred to as <b>probability density estimation, or simply density estimation</b>, as we are using the observations in a random sample to estimate the general density of probabilities beyond just the sample of data we have available.<br><br>

## Density Visualization
<iframe src="https://bytes0211.github.io/distributions/bokeh/density1.html"
     sandbox="allow-same-origin allow-scripts"
     width="500%"
     height="400"
     scrolling="no"
     seamless="seamless"
     frameborder="0">
</iframe>
<br>

Reviewing a histogram of a data sample with a range of different numbers of bins will help to identify whether the density looks like a common probability distribution / normal distribution or not<br>
<br>
In most cases, you will see a unimodal distribution, such as the familiar bell shape of the normal, the flat shape of the uniform, or the descending or ascending shape of an exponential or Pareto distribution<br>
<br>
You might also see complex distributions, such as multiple peaks, with different numbers of bins, referred to as a **bimodal distribution**, or multiple peaks, referred to as a **multimodal distribution**. You might also see a large spike in density for a given value or small range of values indicating outliers, often occurring on the tail of a distribution far away from the mean / center of the density<br>
<br>

## Parametric Density Estimation

**Identify Distribution**
<br><br>
Get familiar with the common probability distributions as it will help you to identify a given distribution from a histogram<br>
<br>
Once identified, you can attempt to estimate the density of the random variable with a chosen probability distribution. This can be achieved by estimating the parameters of the distribution from a random sample of data<br>
<br>
For example, the normal distribution has two parameters:<br>

* mean
* standard deviation

 Given these two parameters, we now know the probability distribution function. These parameters can be estimated from data by calculating the sample mean and sample standard deviation<br>
 <br>
 **We refer to this process as parametric density estimation**<br>
 <br>
 Once we have estimated the density, we can check if it is a good fit. This can be done in many ways, such as:<br>
 <br>
 * Plotting the density function and comparing the shape to the histogram
 * Sampling the density function and comparing the generated sample to the real sample
 * Using a statistical test to confirm the data fits the distribution
<br>
<br>

We can generate a random sample of 1000 observations from a normal distribution with a mean of 50 and standard deviation of 5:


