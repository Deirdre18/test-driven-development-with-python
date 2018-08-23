#   Let's demonstrate this with our simple function here. A function designed to count the number of uppercase characters in a message.

def count_upper_case(message):
    
#   So, it starts by setting a counter variable to zero. It then walks through the message and, if the character is an uppercase character, the counter is incremented.

    count = 0
    for c in message:
        if c.isupper():
            count += 1
#   Finally, when we've walked through the entire message, the total count is returned.

    return count
    #--AUTOMATION
#  Lets automate it, and we can automate it using assertions. So, let's try that now. We'll use the assert keyword to call our function and, to begin with, we'll pass in an empty string. We'd expect that this would return zero, since there are no uppercase characters.

#   What other tests could we do? Well, (1) we could send in one single uppercase character, which should return 1. So, let's do that now: one uppercase. We might worry, though, that it's actually just returning the length of the string that we've sent in, and is not actually counting the characters. (2) Let's try sending in one lowercase character just to confirm that. We would expect this to return zero. (3) Finally, let's try sending in something that's not letters at all just to see how the program copes with it. We'll send in some special characters this time and, also, we'd expect that to be zero

assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%%^") == 0, "Special characters"

#   testing this function. We might think that we could use a print statement - and we can. We can call our function using print. We can pass a message in, and then we can run it to see what we get back. Now, we get the number 2, which is what we would expect since there are two uppercase characters in the string that we passed in. 

#  Remember how the assert keyword works: if it throws an error then program execution stops at that point. So, if it passes all the tests then we can print at the end "all the tests passed". Let's run it again and see what we get. Happily we see that all of the tests were passed. Now, the tests that we've actually done here are very limited in scope. First of all, none of them fail! We don't actually know what will happen when one of the tests fails. And they're not really enough to convince us that the function is working as expected. So, have a look at the challenges below. See if you can modify one of the asserts to make it fail, and then see if you can add extra tests as well until you're confident that the function works as expected. In our next unit, we're going to have a look at testing before we write code. This is the foundation of Test-Driven Development.


#print (count_upper_case("Hello World"))
print ("All tests passed")