#   So, have a look at the challenges below. See if you can modify one of the asserts to make it fail, and then see if you can add extra tests as well until you're confident that the function works as expected. In our next unit, we're going to have a look at testing before we write code. This is the foundation of Test-Driven Development.

# One version of the function (tested and works)
def count_upper_case(message):
    return sum([1 for c in message if c.isupper()])
    
    
# Another version of the function (tested and works)
#def count_upper_case(message):
 #   count = 0
  #  for c in message:
   #     if c.isupper():
    #        count += 1
    #return count

assert count_upper_case("") == 0, "Empty string"
assert count_upper_case("A") == 1, "One upper case"
assert count_upper_case("a") == 0, "One lower case"
assert count_upper_case("£$%%^") == 0, "Special characters"
assert count_upper_case("AaAaQ") == 3, "Multiple Upper Case characters"



print("All the tests passed")