# We’re going to build a function that will calculate the coins that should be returned by a vending machine to make the correct change. So here’s our specification: Given an amount of change that needs to be paid, we want to generate the list of coins that should be given to the customer. Our function should pay the minimum number of coins possible, and the available coin denominations are 100,50,20,10,5,2 and 1. Bringing together everything that we’ve learned in our previous units, we’re going to build the function incrementally using test-driven development. 

# Now that we've done that we can import our byotest framework and create the "all tests pass" message. So let's do that now. From our byotest.py file we want to import everything, and then print our "all tests pass" message. 

from byotest import *

# Now let's write our first test. When the amount of change that we require is zero, then we should get no coins back so we can do this by using our test_are_equal function calling our, currently non-existent, get_change function.

# And we expect, where we've provide zero change, to get an empty list back. What's the easiest way of making that test work? Well, simply to return an empty list. Here's the complete code.

# Let's write our function get_change that takes amount as an argument, and right now we're going to return an empty list. When we save that and we run it then we should be able to see that all of the tests pass, which indeed they do. 

def get_change(amount):
    
    return []

test_are_equal(get_change(0),[])

print ("All tests passed!")

#from byotest import *


#def get_change(amount):
    #"""
   #Takes the payment amount and returns the change
    #`amount` the amount of money that we need to provide change for
    #Returns a list of coin values
    #"""
    #if amount == 0:
     #   return []
    
    #if amount in [100, 50, 20, 10, 5, 2, 1]:
     #   return [amount]
    
    #change = []
    #for coin in [100, 50, 20, 10, 5, 2, 1]:
     #   if coin <= amount:
     #       amount -= coin
      #      change.append(coin)

    #return change


#  Write our tests for our code
#test_are_equal(get_change(0), [])
#test_are_equal(get_change(1), [1])
#test_are_equal(get_change(2), [2])
#test_are_equal(get_change(5), [5])
#test_are_equal(get_change(10), [10])
#test_are_equal(get_change(20), [20])
#test_are_equal(get_change(50), [50])
#test_are_equal(get_change(100), [100])
#test_are_equal(get_change(3), [2, 1])
#test_are_equal(get_change(7), [5, 2])

#print("All tests pass!")

