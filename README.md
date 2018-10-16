[Transcript below taken from Code Institute Online Tutorials]

## What is Test Driven Development?

In this unit, we're going to look at test-driven development - a method of
software development that uses automated tests to guide the development process.

Test-driven development involves identifying the next piece of
functionality that needs to be built. We then write a test, which verifies that
feature. The test should fail initially. Then we implement the feature, which
makes the test pass. After that, we write our next test. This, too, should fail. 

We then implement the code, get the test to pass and, hopefully, keep all the
previous tests passing as well. Using this method it ensures the code is built
incrementally, and developers always have confidence that changes to the code
aren't going to break existing features because all of the previous tests
continue to pass. 

The learning outcomes for this lesson include: 
(1) Understanding assertions (2) writing tests before, after and while the program is being written.
(3) We're then going to build our own rudimentary unit testing framework and in our walkthrough project, we're going to use that testing framework to develop a reasonably complex program.
End of transcript. Skip to the start.
   
   
## Assertions
 
- What is it?

An assertion is a special type of statement in Python


- What does it do?

It allows us to assert that certain values should be set.


- How do you use it?

By including the assert keyword in our functions, we can build our own testing framework.

Walkthrough
 

What is an assertion? Well, think of it as like a sanity check in your program.
It's a handy way of debugging your code and checking in case some unexpected
internal issue arises. At its simplest, it's just a line of code that contains a
boolean expression - you remember that a boolean expression is one that can be
either true or false. In this case, if it returns true, then our program just
continues running as normal. If it returns false, though, then we throw an
error and the program execution is halted. Let's demonstrate that using a
very simple Python script. We have one here called assert.py. As you
can see all we've done is assign to the variable X with the value of 1, the
variable Y with the value of 2, and then we print X plus Y. So, what we would
expect is that 3 is printed when we run this program. Let's just confirm, first of
all, to make sure that is the case. Good! That goes as expected, but let's say,
for instance, that we didn't know what the values of X and Y were going to be;
or, rather, that we wanted to perform a test on those values and throw an error
if a specific condition wasn't met. We can do that using the assert keyword in
Python. As we said, this statement should return true and, if it does, the program
will execute as normal. So, let's insert one here before our print statement. Assert X
is less than Y, and then we can put a message here in case the assert
statement fails. So we can say that X should be less than Y. Now, when we run it
of course the assert statement will return true because X is less than Y, 1
is less than 2. Let's just test that to make sure that it does what we expect.
Good! Everything seems to work as normal. Let's try making
the test fail. Because, if the assertion is false then an error is
thrown and will never actually get to our print statement. We can do that by
changing the values of X and Y. Let's just switch them around, so that now X is
equal to 2 and Y is equal to 1. This time, when we run our script, it should fail
and we should get an error message. Do you see there that we get an assertion
error telling us that X should be less than Y? That's not the
friendliest error in the world, we can make it a little bit friendlier if we
insert values into the assert message. So, let's do that now. We put those in the
braces and return X and Y. Now, when we run it (I'll just clear the terminal first)
we get a much more useful error message that tells us the value of 2 should be less
than 1. This is just a very simple example, but asserts have many many uses.
We can include them in our programs to throw errors if an invalid argument or
an invalid value is passed to a function. Plus, stopping our program and throwing
an error as close as possible to where the problem originates makes debugging
an awful lot easier. What we're going to do in this lesson is use asserts in a
different way. We're going to use asserts for Test-Driven Development and write tests
to check the correctness of our programs. Then, we're going to go a bit further and
we're going to write tests before we write our code so that our tests can
actually help us with coding.
End of transcript. Skip to the start.
View Source Code   

## Test After

- What is it?

Writing tests after our function has been written.

- What does it do?

It shows how, using asserts, we can test a completed function.

How do you use it?

- Create tests using the assert keyword, and check that the function performs as expected.

Video transcript

    In our last unit we looked at the concept of assertions, and you learned
    how to use the Python assert keyword. When you understand this, then you know
    enough to be able to begin writing your own automated tests. Often we manually
    test a program. We write it and then we act as the end user. We supply certain
    input values, and we wait to see that the output values and what we would expect.
    As its name suggests, an automated test is a test that automates this process. It
    executes just part of your program - usually just a single function. It passes
    in some input values and then it asserts that the value returned by the function
    is what we would expect. Let's demonstrate this with our simple
    function here. This is designed to count the number of uppercase characters in a
    message. So, it starts by setting a counter variable to zero. It then walks
    through the message and, if the character is an uppercase character, the counter is
    incremented. Finally, when we've walked through the entire message, the total
    count is returned. So, think for a minute about how you would go about testing
    this function. We might think that we could use a print statement - and we can.
    We can call our function using print. We can pass a message in, and then we can
    run it to see what we get back. Now, we get the number 2, which is what we
    would expect since there are two uppercase characters in the string that
    we passed in. That's all well and good, but it's not really an automated test
    because, as well as passing the data in, we have to sit and look and compare the
    output with the data that we passed in to make sure that it's working. We could
    do this a lot better if we automated it, and we can automate it using assertions.
    So, let's try that now. We'll use the assert keyword to call our function and,
    to begin with, we'll pass in an empty string. We'd expect that this would
    return zero, since there are no uppercase characters.
    What other tests could we do? Well, l we could send in one single uppercase
    character, which should return 1. So, let's do that now: one uppercase. We might
    worry, though, that it's actually just returning the length of the string that
    we've sent in, and is not actually counting the characters. Let's try
    sending in one lowercase character just to confirm that. We would expect this to
    return zero. Finally, let's try sending in something that's not letters
    at all just to see how the program copes with it. We'll send in some special
    characters this time and, also, we'd expect that to be zero. Remember
    how the assert keyword works: if it throws an error then program execution
    stops at that point. So, if it passes all the tests then we can print at the end
    "all the tests passed". Let's run it again and see what we get. Happily we
    see that all of the tests were passed.
    Now, the tests that we've actually done here are very limited in scope. First of
    all, none of them fail! We don't actually know what will happen when one
    of the tests fails. And they're not really enough to convince us that the
    function is working as expected. So, have a look at the challenges below. See if you
    can modify one of the asserts to make it fail, and then see if you can add extra
    tests as well until you're confident that the function works as expected. In
    our next unit, we're going to have a look at testing before we write code. This
    is the foundation of Test-Driven Development.
    End of transcript. Skip to the start.

View Source Code

Challenge
Challenge
Hint

    Modify one of the asserts to make it fail.
    Add more tests until you are confident that the code is correct.
    Test the following version of the function and see if it is correct:

def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
    
## Test Before

Test Before

- What is it?

It performs tests before we write a function.

- What does it do?

It shows how writing tests before writing the function can help us to create expected behaviour.

- How do you use it?

By using the assert keyword to help build functionality.
Walkthrough


    Start of transcript. Skip to the end.
    In our last unit, we looked at how to perform automated testing after our
    function had already been written but, logically, there's nothing actually
    stopping you from writing tests before the function has been written. In fact,
    this is a really good way of thinking about your program specification and
    trying to figure out the kind of values that should be returned - even making
    assumptions about values that should be returned in ambiguous scenarios. In fact,
    just slowing down and figuring out what your program should do before you start
    writing it can be of great value, and can make it much easier to code
    later on. This is true, as well, in interview situations. If you're given a
    challenge and asked to write it, don't rush straight into coding. Sit back,
    stop, and think about exactly what it is that the code is supposed to produce.
    Even write out the specification or tests because it will make it much
    easier to code later on. It also demonstrates though interviewers that
    you know what you're talking about, and that you know what you're doing.
    Let's have a look at the challenge that we have here, for instance, to write a
    function that accepts a list of numbers and returns true if the list contains an
    even number of even numbers. There are still many questions that could arise
    about this particular scenario. The description just says we need to return
    true, but what do we return the rest of the time? We could assume that it's false,
    but maybe that's not correct for the specification. What should the program
    return if there are no even numbers - or no
    numbers at al? Well, what we can do is convert our questions - and the
    specification - into a series of tests to make things clearer. We can clarify
    assumptions, and we can use them as tests to verify that our program works. Our
    challenge defines a number of tests that are based
    on the problem specifications, and also on some assumptions that we've made as
    to how the function should operate. So how do you go about coding something
    that would pass all of these tests? Well, we don't do it all at once!
    The principle of Test-Driven Development is to develop incrementally, writing only
    enough code to pass each test in order without breaking the preceding test. To
    demonstrate how this works, let's define the function and pass the first test
    together. So, we're just going to comment out all the rest of the tests here.
    Now we'll define our function at the top. It's called even_number_of_evens and
    takes "numbers" as an argument. What's the easiest possible way that we
    could get this test to pass? Well, as you can see, it's expecting False, so the
    easiest possible way that we could get this test to pass is just by returning
    false. If we save that and run it then, hopefully, we'll see that all tests have
    passed. Exactly. It's still a long way from a finished function, but it does
    pass our first test. Your challenge for this unit is to complete the function.
    Build it incrementally making sure that it passes each test in order without
    breaking any of the preceding tests. As you create your challenge files remember
    to add and commit to git regularly. Get into the habit of doing this
    particularly when you're adding a major piece of functionality. Don't worry too
    much if you can't solve every single part of this challenge, or that you can't
    get every single test to pass. We're going to go through this in more detail
    in the next unit. We're also going to look at how test-driven development can
    help us to get code running very quickly, and how it can help us to refactor it so
    that we get much cleaner code as well.
    End of transcript. Skip to the start.

View Source Code

Challenge
Challenge
Hint

Write a function that accepts a list of numbers and returns True if the list contains an even number of even numbers.

Here are some tests that might suffice for testing our new function.

assert even_number_of_evens([]) == False, "No numbers"
assert even_number_of_evens([2]) == False, "One even number"
assert even_number_of_evens([2, 4]) == True, "Two even numbers"
assert even_number_of_evens([2, 3]) == False, "Two numbers, only one even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8]) == False, "Multiple numbers, three are even"
assert even_number_of_evens([2, 3, 9, 10, 13, 7, 8, 5, 12]) == True, "Multiple numbers, four are even"
assert even_number_of_evens([1, 3, 9]) == False, "No even numbers"

## Test Driven Development

- What is it?

A method of driving our development using tests.

- What does it do?

It allows us to build and refactor our code using tests.

- How do you use it?

We think about and write tests to drive the behaviour of an individual function. We can then use extra tests to refactor and add extra functionality.

Video transcript

    Start of transcript. Skip to the end.
    We've already seen how to write tests after your program is finished to verify
    its behaviour, and in our last unit we looked at how to write tests before you
    write the program in order to build the specification for your program. The final
    approach that we're going to consider, and this is one that we're going to
    discuss through this whole lesson, is test-driven development, which means we
    write the tests while we write the program. Test-driven development involves
    writing a test that verifies some expected behavior, and then we write just
    enough code to make the test pass. Even if the code doesn't look right or it's
    not how it's going to be in its finished form, we write just enough to make the
    test pass. We don't try to write the entire function all at once. As we
    mentioned before, we build the function incrementally. Let's see this in practice
    using the challenge from the last unit. We're going to solve this now using
    Test-Driven Development. We're going to build it incrementally, and we're going
    to use the tests to write our code. Now, we already wrote one test as an example,
    but our function isn't very useful because any test which expects a false
    value is going to pass. With Test-Driven Development what we're actually looking
    for are valid tests that our function would fail. That's how we move things
    forward. So, in this case we're looking for a test that isn't wanting a true
    response. What kind of a test could we write? Well, how about if we sent in two
    evens?
    This should equal true of course. If we run it, we know what's going to happen.
    Indeed, as we can see, we get an error there because it's expecting us to have
    two even numbers, whereas our function just returns false. What's the
    simplest way to make this pass without breaking our first test? Well, how about
    this? We could write if numbers is empty then return false else return true.
    Now, if we save and run this, all tests now pass. 
    
    So, what we're looking to do each time is to find tests that our program is going to fail. Remember that all we're actually interested in doing is making the tests pass each time.
    It doesn't matter if the code looks wrong, it doesn't matter if it doesn't look pretty.
    Just think of a test that it should fail and, if it does, make it pass in the
    simplest way that you can. So, our function at the moment returns true for any
    amount of numbers that's passed into it. And that's fine, it passes the first two
    tests. What's a test that it should fail? Well, how about if we send in just
    one even number? We'd expect this to return false. Now, we know what
    is going to happen here because the function is very simple. It either returns
    false if there are no numbers, or it returns true if there are any numbers at
    all. So, our function is going to fail this test. We're at the stage now
    where we actually need to count the number of even numbers in the list and
    then check if that number is itself even. Later on we're going to learn about
    how to slow down even more and make some very, very small changes, but right now,
    let's just write the code to make this test pass. If a number is sent in then
    let's initialize a variable to say that we have currently zero
    evens. And now, let's write a loop that's actually going to check each number and
    see if it's even. We can step through this using a for loop, and then we can
    use the modulo operator to see if the remainder, when it's divided by two, is
    zero. If it is then it's an even number so we increment the number of
    evens and finally we return. So, this will return true
    if the number of evens is even and it will return false if it's not.
    Let's save that and run it and see what we get. Now, again, all tests are
    passing. Things are looking good our function is generally working but there
    are still more tests because we haven't tested what will happen if we send in
    any odd numbers yet! Let's see what happens if we send in an odd number of
    odd numbers. Again, we would expect this to be false. Let's run our
    program. Ah! Now, that means that our program
    was returning true when it should have been returning false. Just have a look at
    the code for a few minutes see if you can figure it out for yourselves why the
    code is returning true when it should be returning false. Well, as we see the
    problem is here with our return, because if you divide 2 by 0 the remainder is
    going to be 0 because the answer is 0! What we need to do here is add an if
    statement to say that if the number of evens is 0 then return false, else we can
    return our previous statement. Now, when we run this all tests
    pass again. So now all of the tests from our challenge will pass. We've used
    Test-Driven Development to build our function incrementally and it works! It's
    not the prettiest, and it's maybe not written using the cleanest code, but now
    that we know that it works we can go ahead and refactor our code with
    confidence. In our second video that's exactly what we're going to do.
    End of transcript. Skip to the start.

## Refactoring
 
- What is it?

A method of driving our development using tests.


- What does it do?

It allows us to build and refactor our code using tests.


- How do you use it?

We think about and write tests to drive the behaviour of an individual function. We can then use extra tests to refactor and add extra functionality.

Now that our code is working we can start to clean things up a little bit.
Using the DRY - Don't Repeat Yourself principle, we can have a look at our code
and see if there's anything that's repetitive or redundant. One thing that
stands out straight away is our check for an empty list right at the beginning
of the code. As we step through the code we can see that our check to see if
evens equals zero should cover that, so we can take out the empty list check. If
we're wrong, then our tests will tell us. So, let's try that. We'll save it and
we'll run it. We see that it still passes all the tests. Another place where
we repeat ourselves in the code is where we check to see if a number is even. We
could extract this into a little helper function which, again, would stop us
repeating ourselves. We can define that. We'll call the function is_even,
which takes a number as the argument and returns true or false depending whether the number is even or not. Then, here, instead of doing a check to see if it's zero, we just check to see if it returns true or false. And, the same here as well. Again, if we're wrong on this then our tests will tell us. Let's check that and, stil,l all the tests pass. This is how we can start to refactor our code using the DRY principle so that we're not repeating ourselves and still using our tests to make sure that they all pass. Finally, if you're comfortable with list comprehensions in Python then we can often reduce functions that have loops like this down to a line or two. This is known as Pythonic code or idiomatic Python
Let's clear out our entire function here and we can reduce it just to this.
So, this is our first part of the loop that we were doing and now I return.
Take a few moments just to have a look at it. Let's check to see whether all of
our tests still pass and, indeed, they do. We've learned so far how to test
before we write our program, to test after a program is written, and to use
tests to build our code. Now that you're familiar with how to build tests, we're
going to have a look in our next unit at building our own testing framework.
End of transcript. Skip to the start.
View Source Code
     
     
## Build Your Own Test Framework
 
- What is it?

Build your own reusable testing framework.


- What does it do?

Gives us a series of tests that we can use with our own functions.


- How do you use it?

LESSON:

Import the byotest module, which we will create in this lesson.

In this unit we're going to bring everything that we've learned together
and we're going to build our own testing framework. So far the tests that we've
written have just been simple assertions. If they fail we see an error message
associated with that assertion, but we don't see the actual value that our
function returned. All we got is an error message to tell us it was the wrong value. We can improve on this by wrapping our assertion in a function. Have a look at this, for example. We're going to define a function called "test are equal" and that takes two arguments. The actual value and the expected value. Then we use assert to see if the expected and the actual are equal. If they're not we return an error message. But this time what we're going to do, as we did before, is put values into our error message to make it more understandable; and you remember we do that using the format function. So let's see this in practice. Above it we'll define a very simple function we'll call it "number of evens" like we did before. It expects to take "numbers" as an argument, but this time we're just going to put return 0. Now we can call our testing function by typing test_are_equal, so what are we expecting to come back?

Well, let's pass in a value to our number_of_evens. We'll pass in an array of 1 2 3 4 5. So we're expecting, then, to get back the number two because there are two
even numbers in there. Of course we know this isn't going to work because we're
returning 0, but let's save it and see what happens.
As you can see our tests worked. We have an assertion error at the end there, but
this time it's much more verbose. It's telling us that we're we expected
to get the value of 2, but we actually got 0. We can see that
by what we passed in to the test_are_equal function we sent in the
actual and we also sent in what we would expect. The function then performed the
test for us and gave us the error message.
Now, when you understand how this works, then you can write other tests as
well. For instance, we could write another one and call it test_not_equal. This time, for ease, we'll just use a and b. So again we can assert now that a, our expected, does not equal b - our actual. We have to change our error message as well.

It doesn't end there! There is almost any number of tests that we can write.
For example, we could write one to see if an item is in a collection. Let's just
move the window down a little bit to get a bit more space and then we're going to
write a function called "test_is_in". That will pass in a collection and an
item, and then we're going to assert that the item is in the collection. If it's
not then the error message tells us that our collection name does not contain the
item that we sent in. Again our format method takes the collection and item. So take a few minutes to look over these tests and understand how they work. Then try the challenges that are at the bottom of this page. Firstly, try writing some tests that fail the tests_not_equal and the test_is_in methods to make sure you
understand how to use them properly. Then, try writing some new test methods. Create one called "test_not_in" which checks that an item is not in a collection. Then create "test_between" which tests that a value is between a lower and upper limit inclusive. Finally, just as we've done here,
save your test methods in a Python file called byotest.py. BYO stands for "build
your own". Then, when you want to perform testing on your own projects, you can
import byotest.py. We're going to use this test framework in the upcoming mini
project. Remember, before you create your byotest.py file, to initialize a git
repository and then to add and commit your files to it as we go along. In our
next unit, we'll have a look at our mini project for this section.

End of transcript. Skip to the start.

View Source Code
 Challenge 1
 Challenge Hint
Write some tests that fail the test_not_equal, and test_is_in test methods. Verify that the message is correct for the values given.

 Challenge 2
 Challenge Hint
Write test methods for test_not_in which tests than an item is not in a collection, and test_between which tests that a value is between a lower and upper limit, inclusive.

 Challenge 3
 Challenge Hint
Put your test methods in a python file called byotest.py (byo stands for 'build your own'). You should now be able to import byotest when you want to write tests. We will use your new test framework in the upcoming Mini Project.

       
## Vending Machine Project - Part1

(lesson below extracted from Code Institute lesson)

# What is it?

A vending machine function for determining the correct amount of change.


# What does it do?

Given an amount, it determines the change to be returned. We will build it using test-driven development.

# How do you use it?

Use the testing framework we built in the last lesson to add functionality to the vending machine module.

##LESSON:

In our final unit for this lesson, our mini project will walk you through
building a relatively complicated program. We're going to build a function
that will calculate the coins that should be returned by a vending machine
to make the correct change. So here's our specification: Given an amount of change
that needs to be paid, we want to generate the list of coins that should
be given to the customer. Our function should pay the minimum number of coins
possible, and the available coin denominations are 100,50,20,10,5,2 and 1.
Bringing together everything that we've learned in our previous units, we're
going to build the function incrementally using test-driven
development. 

So let's start by initializing an empty git repository and now that's done, remember to add and commit your file to it as we go through this project. Now we can create a new Python file (ie) vending_machine.py. 

Now that we've done that we can import our byotest framework and create the "all tests pass" message. So let's do that now. From our byotest.py file we want to import everything, and then print our "all tests pass" message. 

Now let's write our first test. When the amount of change that we require is zero, then we should get no coins back so we can do this by using our test_are_equal function calling our, currently non-existent, get_change
function. And we expect, where we've provide zero change, to get an empty list
back. What's the easiest way of making that test work? Well, simply to return an
empty list. Here's the complete code. Let's write our function get_change that takes amount as an argument, and right now we're going to return an empty list. When we save that and we run it then we should be able to see that all of the tests pass, which indeed they do. So, for the next test we can deal with the situation where the amount required is represented by a single coin. Now, remember to put our tests in here before the print "all tests pass" statement and after our function. So, again we'll call test_are_equal with get_change, and this time we'd expect one to be returned. Now, we need a simple way to make this pass while, not breaking our first test. This might look a little strange, but we need to put an if statement in to make sure that our first test doesn't break, then we're simply just going to return 1. 

The if statement means that 0 results in no coins and 1 makes our second test pass. But, that means that 1 is returned for any amount other than 0, so what about our next test, then, when we try to send in a different coin? This time we'll pass the value of 2. We would expect 2 to come back. Now, this is
fairly easy to change. All we need to do is return "amount" instead of just a 1
cent coin. Now that we've done that, we can actually write tests that will
pass for every single one of our coin denominations. Let's save that and run it
just to make sure that our tests pass. And they do! But, now let's add another
test. What happens if we need change with more than one coin? What happens if it's not a nice even denomination? So let's pass this time into our get_change
function the value of 3. We would then expect to have 2 and 1 coming back as
change. How can we make this test pass? Well, again we can use an if statement in
here, and the if statement - if you remember - protects the existing tests.
Then, once we've done that we can return exactly the value that will make the
test pass. In this case, we're expecting a list to come back of 2,1 and this will
make our test pass. So, we're back to a situation now where our code will work
for a certain amount, but not for others. Now what we need to do is test it
with a different amount to force us to make the function more general. It's a
well-known adage of Test-Driven Development that, as the tests become
more specific, the code and the function become more general. So, add this test.
This time, we're going to pass in 7 and we would expect to get back 5 and 2 now.
Obviously, we know what's going to happen. This test is going to fail, but let's
just try it anyway so we can see our error message. As we can see there, we
expected coins 5 and 2 in value, but we got a 2 cent and a 1 cent coin back. To
make it pass we need to look at how we calculate change made up of multiple
coins. Let's just rearrange the code a little bit before we tackle this new
test. We're going to create another empty list and call it "change", and then we're going to use the append function to add values onto that list. Now this
small change that we're making might not seem that significant, but it shows we
can individually add coins to the change that we return. The question is: how do
we know which coins we need to add? Well, when we think about it we can see that
if the coin is less than or equal to the amount we need to return, we should add
it to the change. So, let's take those two lines out and rewrite our function.
This time we're going to step through each of the coin denominations and if
the coin value is less than or equal to the amount that we passed in then we're
going to add that onto our change. Then finally we return the change list. So,
this will get us past that hard-coded 2,1 that the function previously
returned. Is it correct? Well, let's run it and see.

No. We can see that what we got back was 5,2,1 where we expected to get 5,2.
The function, as it stands, adds every coin less than 7 whether it is needed or
not. 5,2 should have been enough, but the function carried on. We need to modify it again to keep track of how much change there is left to pay after the coins have been added. Fortunately this is a fairly trivial change to make to our function. All we need to do is deduct the amount of the coin from the amount that we sent in. This time if we try it, you'll see that all of our tests pass. In our next video we'll complete our function and refactor our code.

# Vending Machine Project-Part2

## What is it?

A vending machine function for determining the correct amount of change.


## What does it do?

Given an amount, it determines the change to be returned. We will build it using test-driven development.


## How do you use it?

Use the testing framework we built in the last lesson to add functionality to the vending machine module.
      
      
LESSON: 

In our last video, we built our function incrementally and tested to make sure
that it was working, but there's one scenario that we haven't tested for yet,
which is when we might need more than one of a particular denomination of coin.
Let's write a test to check for this scenario. This time, we're going to pass
into our get_change function the value of 9. We'd expect to get back change
of 5 cents 2 cents and 2 cents. What happens, then, if we save and run our
function as it is now? Well, as we can see, it fails. We expected to get 5, 2 and
2, but what we actually got was a 5 cent a 2 cent
and a 1 cent. The problem is that our function adds the 5 and the 2, but then
we still have the outstanding amount of 2. The next coin is 1, which is less than
the amount and so is added. We should have had the functionality to add
another 2 cent coin rather than move on. Fortunately, this is a fairly trivial
repair to make. We just need to change our "if" statement for a "while".

Now, as long as the coin is less than or equal to the amount, it will carry on adding it and only when it's not will it move on or return the change. So, now we have a fully functioning program. We also have a suite of tests so we can refactor our code. The first thing we might notice in refactoring is that we have a duplicate list of coin denominations. We need to change that. We don't want to repeat ourselves, so we can add a variable called coins and give this our list ofcoi n denominations. Now we just need to go down to our if statement here and change it from the list to our variable "coins", and the same as well for our for loop. As we look at it too, though, we might realise that our if statements are now no longer required. The code itself is general enough to cover all of the scenarios that the if statements were previously covering, so we can remove
those. Great! We now have a fully working and refactored function. 

Let's just run it and test it to make sure that everything works...and it does. But even more - the tests that we have allow us to add new features with confidence. For instance, let's add the ability now to be able to override the coin denominations. Here's a new test. So this time into our get_change function we're going to pass the value of 35 and a second argument that currently doesn't exist. We'll say we expected to get back 25 and 10. To get this test to pass we need to define the list of US coins, and we also need to add an optional argument to our get_change function. Let's go do that now. At the top here we can define a new list. We'll call it usd_coins and we'll put in the US coin denominations, which uses a quarter rather than 20 cents . We'll change the name of this one to eur_coins. Now we add our optional second argument into our get_change function. By putting the equals there it means that, if we don't supply the argument, it will default to using eur_coins. Now if we save and run our program again, we'll see that all of our tests pass including the one that has the optional second argument. So, we've completed our program built using Test-Driven Development. Now have a look at the challenges below.

Change the function that we wrote so that instead of a list of coins it works with a dictionary that contains the coin denominations and the quantity of each coin available. Start with 20 of each coin. We'll give the option to override this by passing a dictionary to the function as we did with the US coins option. If a coin that would normally be used to make the change isn't available, then the program should attempt to use smaller coins to make up the change. If you can't make up the change at all with any of the coins available, then raise an error. Secondly, think how you could write a test that checks for a particular error. What kind of problems does that cause? We'll return to that in later lessons. So that concludes our Test-Driven Development unit. Well done, and don't forget to commit everything to git!

       
       

    



