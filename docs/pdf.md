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

