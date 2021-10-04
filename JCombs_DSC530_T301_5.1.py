# Class: 530-T301
# Instructor: Shankar Parajulee
# Student Name: Jerry Combs
# Date: 3-Oct-2021
# Week 5 assignment 5.1 Preparing for Exploratory Data Analysis

import scipy.stats

mu = 178
sigma = 7.7
dist = scipy.stats.norm(loc=mu, scale=sigma)
type(dist)

print("Mean: {}; Standard Deviation: {}" .format(dist.mean(), dist.std()))
print("How many people are more than one standard deviation below the mean? Answer {}" .format(dist.cdf(mu-sigma)))

below = dist.cdf(177.8)    # 5'10"
above = dist.cdf(185.4)   # 6'1"

print("Approx {} of the population will below 5'10; Approx {} of the population will be above 6'1;\nPercentage that could join the blue man group is: {}".format(below, above, above-below))

