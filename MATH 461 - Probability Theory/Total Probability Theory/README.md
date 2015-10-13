Original Date of Program: September 4th, 2015 (Based on Date Modified tag on file)

The Law of Total Probability tells us that the Probability of A is the sum of the Probability of A given B(i) times the Probability of B(i).

This small piece of code shows how the Law of Total Probability could be applied to determining the general likelihood of Hilary Clinton becoming president, based on the data from RealClearPolitics.com. In this case, the probability A we are looking for is the probability of Hilary Clinton winning presidency, while B(i) is the Probability of her opponents winning presidency and P(A|B(i)) is the probability that Hilary Clinton will specifically beat candidate B(i).

From RealClearPolitics.com we can gather the 2 pieces of data needed for this equation:
1. Poll data of the support for Hilary Clinton vs. each of the Republican candidates
2. Poll data of the support for each individual Republican candidate against each other for the Republican Primary bid.

For this example, I used only the top 8 republican candidates, then adjusted the probabilities of their support for the Republican Primary bid so that the sum of the 8 probabilities equals 1.


Coincidentally, I wrote this program at a time that was beginning to be interested in learning Ruby. This was the first program past "Hello World" that I wrote in Ruby.