#from __future__ import division #This will always perform a float division when using the / operator and use // for integer division.
 
item = input("What is the cost of the item?")
tax = float(input("What is the sales tax in %?")) #different way is to make at least one number float, causes all remaining calculations to use floating numbers
t1 = tax / 100
t2 = item * t1
total = item + t2
 
#print tax / 100
#print item, tax, t1, t2, total
print "Your total price is", total, "$."
 