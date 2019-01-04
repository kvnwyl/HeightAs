# HeightAs :cake:

>Ever wanted to know how many biscuits tall you are? How about your height in tennis balls? With `HeightAs`, this - and more - is all possible.

`HeightAs` is a humorous module to calculate your height as a quantity of a variety of different objects.

# Usage :cake:

Create an instance of the `HeightAs` class and pass in keyword args of the desired height. Currently feet, inches, m, cm and mm are supported.

The `objects.json` file is populated with a number of different items and their height in millimetres. When a new instance of the `HeightAs` class is created, the height entered is converted into mm and then is simply divided by the height of the object.

Example:

```
x = HeightAs(feet=6, inches=2)  # Sets height.
x.biscuit()                     # Prints height in all biscuits.
x.biscuit("Hob Nob")            # Prints height in Hob Nobs.
```

# Origin :cake:

Originally inspired by a mid-game bonus round on the Channel 4 show '8 out of 10 Cats Does Countdown' whereby the contestants were asked which is taller; comedienne Victoria Coren Mitchell or a tower of Victoria sponges. `HeightAs` was originally designed to calculate height against a number of different foodstuffs and confectionary items but as it progressed and evolved, it seemed natural to permit the comparison of height to any object.

# Notes :cake:
For each key in the `objects.json` file, a method with the same name is created within the class which can be called with no parameters (in which case, all keys are returned) or with a specific key (in which case only the single value will be returned).
