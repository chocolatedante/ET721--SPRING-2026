Dante Vanderpool
Huixin Wu
ET721
4/12/26

# Report: The Benefits of Comprehensive Testing in Software Development

## Before and After: Results Summary

* What was the initial test coverage?  
The initial test coverage was incomplete because some of the unit tests in test_models.py were not implemented. This meant that some parts of the code were not being tested.

* What is the final test coverage you were able to achieve?  
After completing the missing tests, the test coverage improved. The major functionalities of the Fruit model and FruitMetrics class were tested, including valid and invalid inputs.

* How many tests did you end up having?  
I ended up with multiple unit tests that covered different scenarios such as valid fruit creation, invalid inputs, and calculation methods like total fruits, average quantity, and most common fruit.

---

## Untested Code: Effects

* Were you able to understand all features and different use cases of the code without the tests?  
Without the tests, it was harder to fully understand all the features and edge cases. Some things were not immediately clear just by reading the code.

* What did you think of having to test the API manually?  
Testing the API manually was helpful for basic understanding, but it was time consuming and not very efficient compared to automated testing.

* What was the result of having few tests on your understanding of the API?  
Having fewer tests made it harder to know if the code would work. There was no quick way to verify that everything worked correctly after making changes, which made things slower.

---

## Adding Tests

* How did you go about adding more tests to the code?  
I added tests by completing the missing sections in test_models.py. I tested both normal cases and edge cases, such as invalid names, negative quantities, and non-integer values.

* What is the difference between a unit test and an API test? Do they bring different values?  
A unit test checks individual parts of the code, like a single function or method, to make sure it works correctly. An API test checks how the application responds to HTTP requests. Both are good because unit tests verify if the code works, while API tests verify how the application functions from a user perspective.

---

## Automation

* What were the benefits of automating test coverage?  
Automating tests made it much easier to verify the code quickly. Using pytest allowed me to run all tests at once and immediately see if anything was needed to be changed or fixed which saves time.

---

## New Features

* What was your experience like having to add new features when you tested baseline code?  
Working with baseline code made it easier to understand how everything worked. It also made adding new features less confusing since the tests showed what was expected.

* Did it give you any feeling of security when trying out new features?  
Yes because the tests acted as a safety net. If something was wrong, the tests would detect it immediately.

---

## Future

* What do you hope to takeaway from the experience having to write tests?  
From this experience, I learned that testing helps you understand your code on a deeper level. It made me realize that just writing code isn’t enough—you need to make sure it works in different situations. In the future, I want to use testing as a way to improve both my coding skills and my problem-solving approach.