#Machine Learning
===============

##Table of Contents
=================
In progress table of contents.
* [Pandas](https://github.com/caromedellin/Python-notes/blob/master/pandas.pyc)
  <br> Imported Pandas to play with it.
* [Chapter 1: Reading from a CSV Pandas cookbook](http://nbviewer.ipython.org/github/jvns/pandas-cookbook/blob/master/cookbook/Chapter%201%20-%20Reading%20from%20a%20CSV.ipynb)
  <br> Reading your data into pandas is pretty much the easiest thing. Even when the encoding is wrong!

Compilation of notes from the Standford class given by Andrew Ng and other miscellaneous resources.

##What is Machine Learning? 
There are two main definitions of Machine Learning are offered. Arthur Samuel described it as: “the field of study that gives computers the ability to learn without being explicitly programmed (this is an older definition).
Tom Mitchell provides a more modern definition. “A computer is said to learn from experience E with respect to some class of tasks T and performance measure P, if its performance at tasks in T is measured by P, improves with experience E”.
```
Example: playing checkers.

E = the experience of playing many games of checkers
T = the task of playing checkers
P = the probability that the program will win the next game.
```
Machine Learning grew out of work in AI and it's a new capability for computers. Learning Algorithms can touch many problems. My personal interests are in Natural Language Processing, Database mining and self customizing programs.

As explained in the course by Andrew Ng, Machine Learning can be supervised and unsupervised.

## Supervised Learning

In supervised Learning we are given a data set and we already know what to expect from it, this means that we know what the correct output should look like. There is already an idea that there is a relationship between the input and the output.
The supervised learning problems are categorized in "regression" and "classification" problems
###Regression
In a regression problem we are trying to predict results within a continuous output, this means that we are trying to map input variables in to some continuous function.

####Example
Here we are given a dataset about the size of houses on the real estate market, with it we can try to predict their price. 

![Housing Prediction](pictures/housing-prediction.png)
"the write answers" being given means that we have examples for which we know what the actual price given a condition (or a set of variables) actually is in the real world.

With this knowledge there are different possible predictions or functions we can choose from, we want to minimize the cost function (square-error).

Supervised learning refers to the fact that e gave the algorithm a dataset in which for every example we told it what was the right price, and the toss of the algorithm was to produce more of the right answers. This is called a regression problem.  
Regression: refers to the fact that we try to predict it with continuous values attributes.

###Classification
In a classification problem we are trying to predict results within a discrete output, like yes or no, basically dividing in to categories (it can be more than 2).

