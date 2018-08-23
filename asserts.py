#x = 2
#y = 1

 #assert x < y, "{0} should be less than {1}".format(x, y)

#print(x + y)

#let's say,for instance, that we didn't know what the values of X and Y were going to be;
#or, rather, that we wanted to perform a test on those values and throw an error
#if a specific condition wasn't met. We can do that using the assert keyword in
#Python. As we said, this statement should return true and, if it does, the program
##will execute as normal. So, let's insert one here before our print statement. Assert X
# less than Y, and then we can put a message here in case the assert
#statement fails. So we can say that X should be less than Y. Now, when we run it
#of course the assert statement will return true because X is less than Y, 1
#is less than 2. Let's just test that to make sure that it does what we expect.
#Good! Everything seems to work as normal. 

#x = 1
#y = 2

#assert x < y, "x should be less than y"

#print(x + y)

#Let's try making
#the test fail. Because, if the assertion is false then an error is
#thrown and will never actually get to our print statement. We can do that by
#changing the values of X and Y. Let's just switch them around, so that now X is
#equal to 2 and Y is equal to 1. This time, when we run our script, it should fail
#and we should get an error message. Do you see there that we get an assertion
#error telling us that X should be less than Y? That's not the
#friendliest error in the world, we can make it a little bit friendlier if we
#insert values into the assert message. So, let's do that now. 

#x = 2
#y = 1

#assert x < y, "x should be less than y"

#print(x + y)

#Let's try making the test fail. Because, if the assertion is false then an error is
#thrown and will never actually get to our print statement. We can do that by
#changing the values of X and Y. Let's just switch them around, so that now X is
#equal to 2 and Y is equal to 1. This time, when we run our script, it should fail
#and we should get an error message. Do you see there that we get an assertion
#error telling us that X should be less than Y? That's not the
#friendliest error in the world, we can make it a little bit friendlier if we
#insert values into the assert message. So, let's do that now. 


x = 2
y = 1

assert x < y, "{0} should be less than {1}".format(x, y)

print(x + y)

