


Chapter 1.3: Making Predictions
================================

Predicting how things will play out in a given county if and only if things don’t change - 

One of the disadvantages of estimating COVID 19 infections using a metric that involves a rate is that it depends entirely on the amount of available data. For example, calculating infections using death rate and confirmed death counts will only yield an estimate for the number of infections 18 days prior to the latest death count. This metric does not provide a model for predicting future infections. And predicting how the virus will spread and affect different populations is crucial in flattening the curve. 

A tool that can be used to make these predictions is Curvefit in python's scipy package. In a nutshell, curvefit finds the line of best fit given a set of data points with a function input. In this case I chose a double logistic function, as almost none of the counties followed a perfect logistic curve. After finding a function to represent the infection estimates I calculated, I was able to find the upper limit value, or the maximum number of expected infections. 
