##--TEST DRIVEN DEVELOPMENT--

#In our last unit, we looked at how to perform automated testing after our function had already been written but, logically, there's nothing actually stopping you from writing tests before the function has been written. In fact, this is a really good way of thinking about your program specification and trying to figure out the kind of values that should be returned - even making assumptions about values that should be returned in ambiguous scenarios. In fact, just slowing down and figuring out what your program should do before you start writing it can be of great value, and can make it much easier to code.

#We've already seen how to write tests after your program is finished to verify its behaviour, and in our last unit we looked at how to write tests before you write the program in order to build the specification for your program. The final approach that we're going to consider, and this is one that we're going to discuss through this whole lesson, is test-driven development, which means we     write the tests while we write the program.



#Now, we already wrote one test as an example,but our function isn't very useful because any test which expects a false value is going to pass. With Test-Driven Development what we're actually looking for are valid tests that our function would fail. That's how we move things forward. So, in this case we're looking for a test that isn't wanting a true response. What kind of a test could we write? Well, how about if we send in two evens? This should equal true of course. If we run it, we know what's going to happen. Indeed, as we can see, we get an error there because it's expecting us to have    two even numbers, whereas our function just returns false.  
    

#def even_number_of_evens(numbers):
 #   return False
  
    
#assert even_number_of_evens([]) == False, "No numbers"
#assert even_number_of_evens([2, 4]) == True, "Two even numbers"
       
        
#print ("all tests passed!")

#What's the simplest way to make this pass without breaking our first test? Well, how about this? We could write if numbers is empty then return false else return true. Now, if we save and run this, all tests now pass.
    
#--CHANGE TO FUNCTION--    
    
#def even_number_of_evens(numbers):
  
  
    #if numbers == []:
    #   assert even_number_of_evens([]) == False, "No numbers"
    #   assert even_number_of_evens([2, 4]) == True, "Two even numbers"
        
#So, what we're looking to do each time is to find tests that our program is going to fail. Remember that all we're actually interested in doing is making the tests pass each time. It doesn't matter if the code looks wrong, it doesn't matter if it doesn't look pretty. Just think of a test that it should fail and, if it does, make it pass in the simplest way that you can. So, our function at the moment returns true for any amount of numbers that's passed into it. And that's fine, it passes the first two tests.

        
#def even_number_of_evens(numbers):
  
  
   # if numbers == []:
        # -- PASSES FIRST 2 TESTS --
        # assert even_number_of_evens([]) == False, "No numbers"
        # assert even_number_of_evens([2, 4]) == True, "Two even numbers"
                
        
# What's a test that it should fail? Well, how about if we send in just one even number? We'd expect this to return false. Now, we know what is going to happen here because the function is very simple. It either returns false if there are no numbers, or it returns true if there are any numbers at all.  So, our function is going to fail this test. 
        
        #assert even_number_of_evens([2]) == False, "One even number"
  
        #return False
    
    #else: 
            
        #return True
        
#print ("all tests passed!")

# --COUNTING NUMBER OF EVEN NUMBERS--
    
# We're at the stage now where we actually need to count the number of even numbers in the list and     then check if that number is itself even. Later on we're going to learn about how to slow down even more and make some very, very small changes  

def even_number_of_evens(numbers):
  
  # but right now, let's just write the code to make this test pass. 
    if numbers == []:
     
        return False
    
    # If a number is sent in then let's initialize a variable to say that we have currently zero evens.
    
    else: 
            
        evens = 0
        
# And now, let's write a loop that's actually going to check each number and see if it's even. We can step through this using a for loop.

# If it is then it's an even number so we increment the number of evens and finally we return. So, this will return true if the number of evens is even and it will return false if it's not. Let's save that and run it and see what we get. Now, again, all tests are passing. Things are looking good, our function is generally working but there are still more tests, because we haven't tested what will happen if we send in any odd numbers yet!

        for n in numbers:
            if n % 2 == 0:
            
                evens += 1
                
# and then we can use the modulo operator to see if the remainder, when it's divided by two, is zero. 
       
        
        
#Well, as we see the problem is here with our return, because if you divide 2 by 0 the remainder is going to be 0 because the answer is 0! What we need to do here is add an if statement to say that if the number of evens is 0 then return false, . 
    
        
        if evens == 0:
            
            return False
            
        else:   
            
        # else we can return our previous statement
       
            return evens % 2 == 0 
        
# Now, when we run this all tests pass again. So now all of the tests from our challenge will pass. We've used Test-Driven Development to build our function incrementally and it works! It's not the prettiest, and it's maybe not written using the cleanest code, but now that we know that it works we can go ahead and refactor our code with confidence. In our second video that's exactly what we're going to do.        
        
assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2]) == False, "One even number"   

# Let's see what happens if we send in an odd number of odd numbers. Again, we would expect this to be false. Let's run ourprogram. Ah! Now, that means that our program was returning true when it should have been returning false. Just have a look at the code for a few minutes see if you can figure it out for yourselves why the code is returning true when it should be returning false. 
     
assert even_number_of_evens([1, 3, 9]) == False, "Three odd numbers"



print ("all tests passed!")








#--FUNCTIONS--
#Write a function that accepts a list of numbers and returns True if the list contains an even number of even numbers.

#Here are some tests that might suffice for testing our new function.

#assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
#assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
#assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
#

#assert even_number_of_evens([]) == False, "No numbers"
#assert even_number_of_evens([2, 4]) == True, "Two even numbers"



#print ("all tests passed!")






    




