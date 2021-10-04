# Class: 530-T301
# Instructor: Shankar Parajulee
# Student Name: Jerry Combs
# Date: 3-Oct-2021
# Week 5 assignment 5.2 Preparing for Exploratory Data Analysis

import scipy.stats

alpha = 1.7
xmin = 1       # meter
dist = scipy.stats.pareto(b=alpha, scale=xmin)
print("Median value = {}" .format(dist.median()))
print("The median height in the pareto world is {}" .format(dist.mean()))
print("The fraction of people who are shorter than the mean is {}" .format(dist.cdf(dist.mean())))
print("Out of 7 billion people, how many do we expect to be taller than 1 km is {}" .format((1 - dist.cdf(1000)) * 7e9, dist.sf(1000) * 7e9))
print("The tallest person is expected to be {}" .format(dist.ppf(1 - 1/7e9)))
