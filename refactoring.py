#Now that our code is working we can start to clean things up a little bit. Using the DRY - Don't Repeat Yourself principle, we can have a look at our code and see if there's anything that's repetitive or redundant.  
      
# (2) Another place where we repeat ourselves in the code is where we check to see if a number is even. We could extract this into a little helper function which, again, would stop us repeating ourselves. We can define that. We'll call the function is_even, which takes a number as the argument and returns true or false depending whether the number is even or not. 
                
def is_even(number):
    return number % 2 == 0
    
    #This is how we can start to refactor our code using the DRY principle so that we're not repeating ourselves and still using our tests to make sure that they all pass. Finally, if you're comfortable with list comprehensions in Python then we can often reduce functions that have loops like this down to a line or two. This is known as Pythonic code or idiomatic Python. Let's clear out our entire function here and we can reduce it just to this. So, this is our first part of the loop that we were doing and now I return. Take a few moments just to have a look at it. Let's check to see whether all of our tests still pass and, indeed, they do. We've learned so far how to test before we write our program, to test after a program is written, and to use tests to build our code. Now that you're familiar with how to build tests, we're going to have a look in our next unit at building our own testing framework.

        
def even_number_of_evens(numbers):
  
  # (1) One thing that stands out straight away is our check for an empty list right at the beginning of the code. As we step through the code we can see that our check to see if evens equals zero should cover that, so we can take out the empty list check. If we're wrong our test will tell us.
 
    #if numbers == []:
     
     #   return False
    
    # If a number is sent in then let's initialize a variable to say that we have currently zero evens.
    
    #else: 
        #==REMOVING WHOLE FUNCTION--    
        #evens = 0
        
# And now, let's write a loop that's actually going to check each number and see if it's even. We can step through this using a for loop.

# If it is then it's an even number so we increment the number of evens and finally we return. So, this will return true if the number of evens is even and it will return false if it's not. Let's save that and run it and see what we get. Now, again, all tests are passing. Things are looking good, our function is generally working but there are still more tests, because we haven't tested what will happen if we send in any odd numbers yet!


        #==REMOVING WHOLE FUNCTION-- 
        #for n in numbers:
#(3) Here now instead of doing a check to see if it's zero, we just check to see if it returns true or false. 
            
            #==REMOVING WHOLE FUNCTION-- 
            #if is_even(n):
            #if n % 2 == 0:
            
                #evens += 1
                
# and then we can use the modulo operator to see if the remainder, when it's divided by two, is zero. 
       
        
        
#Well, as we see the problem is here with our return, because if you divide 2 by 0 the remainder is going to be 0 because the answer is 0! What we need to do here is add an if statement to say that if the number of evens is 0 then return false, . 

        #==REMOVING WHOLE FUNCTION-- 
        #if evens == 0:
            
           # return False
            
        # else:   
            
        # else we can return our previous statement
        
#(4) and same again here. If we're wrong on this, our tests will tell us.

        #==REMOVING WHOLE FUNCTION-- 
           #return is_even(evens)
       
            #return evens % 2 == 0 
        
# Now, when we run this all tests pass again. So now all of the tests from our challenge will pass. We've used Test-Driven Development to build our function incrementally and it works! It's not the prettiest, and it's maybe not written using the cleanest code, but now that we know that it works we can go ahead and refactor our code with confidence. In our second video that's exactly what we're going to do.        
        
    assert even_number_of_evens([]) == False, "No numbers"
    assert even_number_of_evens([2, 4]) == True, "Two even numbers"
    assert even_number_of_evens([2]) == False, "One even number"   

# Let's see what happens if we send in an odd number of odd numbers. Again, we would expect this to be false. Let's run ourprogram. Ah! Now, that means that our program was returning true when it should have been returning false. Just have a look at the code for a few minutes see if you can figure it out for yourselves why the code is returning true when it should be returning false. 
     
    assert even_number_of_evens([1, 3, 9]) == False, "Three odd numbers"



print ("all tests passed!")

