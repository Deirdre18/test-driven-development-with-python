# We’re going to build a function that will calculate the coins that should be returned by a vending machine to make the correct change. So here’s our specification: Given an amount of change that needs to be paid, we want to generate the list of coins that should be given to the customer. Our function should pay the minimum number of coins possible, and the available coin denominations are 100,50,20,10,5,2 and 1. Bringing together everything that we’ve learned in our previous units, we’re going to build the function incrementally using test-driven development. 

# Now that we've done that we can import our byotest framework and create the "all tests pass" message. So let's do that now. From our byotest.py file we want to import everything, and then print our "all tests pass" message. 

from byotest import *

# Now let's write our first test. When the amount of change that we require is zero, then we should get no coins back so we can do this by using our test_are_equal function calling our, currently non-existent, get_change function.

# And we expect, where we've provide zero change, to get an empty list back. What's the easiest way of making that test work? Well, simply to return an empty list. Here's the complete code.

# Let's write our function get_change that takes amount as an argument, and right now we're going to return an empty list. When we save that and we run it then we should be able to see that all of the tests pass, which indeed they do. 
def get_change(amount):
    if amount == 0:  
        return []
   
#How can we make this test pass? Well, again we can use an if statement in here, and the if statement - if you remember - protects the existing tests. Then, once we've done that we can return exactly the value that will make the test pass. In this case, we're expecting a list to come back of 2,1 and this will make our test pass. 

    if amount in [100, 50, 20, 10, 5, 2, 1]:
        return [amount]
        
#So, we're back to a situation now where our code will work for a certain amount, but not for others. Now what we need to do is test it with a different amount to force us to make the function more general. It's a well-known adage of Test-Driven Development that, as the tests become more specific, the code and the function become more general. So, add this test. This time, we're going to pass in 7 and we would expect to get back 5 and 2 now.    

#Obviously, we know what's going to happen. This test is going to fail, but let's just try it anyway so we can see our error message. As we can see there, we expected coins 5 and 2 in value, but we got a 2 cent and a 1 cent coin back. To make it pass we need to look at how we calculate change made up of multiple coins. Let's just rearrange the code a little bit before we tackle this new test. We're going to create another empty list and call it "change", and then we're going to use the append function to add values onto that list. 

#Now this small change that we're making might not seem that significant, but it shows we can individually add coins to the change that we return. The question is: how do we know which coins we need to add? Well, when we think about it we can see that if the coin is less than or equal to the amount we need to return, we should add it to the change. So, let's take those two lines out and rewrite our function. This time we're going to step through each of the coin denominations and if the coin value is less than or equal to the amount that we passed in then we're going to add that onto our change. Then finally we return the change list. So, this will get us past that hard-coded 2,1 that the function previously returned. Is it correct? Well, let's run it and see. No. We can see that what we got back was 5,2,1 where we expected to get 5,2. The function, as it stands, adds every coin less than 7 whether it is needed or not. 5,2 should have been enough, but the function carried on. We need to modify it again to keep track of how much change there is left to pay after the coins have been added. Fortunately this is  to do is deduct the amount of the coin from the amount that we sent in. This time if we try it, you'll see that all of our tests pass. In our next video we'll complete our function and refactor our code.

    change = []
    for coin in [100, 50, 20, 10, 5, 2, 1]:
   
       if coin <= amount:
           amount -= coin
           change.append(coin)

    return change
    
#So, for the next test we can deal with the situation where the amount required is represented by a single coin. Now, remember to put our tests in here before the print "all tests pass" statement and after our function. So, again we'll call test_are_equal with get_change, and this time we'd expect 1 to be returned.

#Now, we need a simple way to make this pass while, not breaking our first test. This might look a little strange, but we need to put an if statement in to make sure that our first test doesn't break, then we're simply just going to return 1. The if statement means that 0 results in no coins and 1 makes our second test pass. But, that means that 1 is returned for any amount other than 0, so what about our next test, then, when we try to send in a different coin? This time we'll pass the value of 2. We would expect 2 to come back. Now, this is fairly easy to change. All we need to do is return "amount" instead of just a 1 cent coin. Now that we've done that, we can actually write tests that will pass for every single one of our coin denominations. 

# Write our tests for our code

#test_are_equal(get_change(0), [])
#test_are_equal(get_change(1), [1])
#test_are_equal(get_change(2), [2])
#test_are_equal(get_change(5), [5])
#test_are_equal(get_change(10), [10])
#test_are_equal(get_change(20), [20])
#test_are_equal(get_change(50), [50])
#test_are_equal(get_change(100), [100])

# Let's save that and run it just to make sure that our tests pass. And they do! But, now let's add another test. What happens if we need change with more than one coin? What happens if it's not a nice even denomination? So let's pass this time into our get_change function the value of 3. We would then expect to have 2 and 1 coming back as change.

#test_are_equal(get_change(3), [2, 1])
test_are_equal(get_change(7), [5, 2])

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

#So, we're back to a situation now where our code will work for a certain amount, but not for others. Now what we need to do is test it with a different amount to force us to make the function more general. It's a well-known adage of Test-Driven Development that, as the tests become more specific, the code and the function become more general. So, add this test. This time, we're going to pass in 7 and we would expect to get back 5 and 2 now.

test_are_equal(get_change(7), [5, 2])

#print("All tests pass!")

