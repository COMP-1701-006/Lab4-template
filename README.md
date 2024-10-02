# Functions
![Points bar](../../blob/badges/.github/badges/points-bar.svg)

## Objectives
The goals of this lab are to learn about:
- Void functions
- Value-returning functions
- Printing vs. returning strings
- Breaking a problem into reusable pieces

## Part 1: Tracing and debugging
You and a friend are developing a recipe app where the user enters ingredients and quantities in grams. Your friend started writing the code, but there's a mysterious bug that they've asked you to fix.

1. Open the file `ingredients.py` and inspect the function header `add_ingredient`. What data types are should be passed as arguments? What type should be returned?
2. Trace the code **manually**. What data type is actually returned?
3. Run the code. Did it produce what you expected?
4. **Without modifying the `main` function**, fix the code so that it still prints the output, but doesn't print `None` anymore.

## Part 2: Writing functions
As part of the same recipe app, we're going to add a new file named `cooking_time.py`. Eventually this will have a number of functions related to cooking times, but for now we're just going to calculate time to bake a cake.

1. Create a new file named `cooking_time.py` in the same folder as `ingredients.py`.
2. Define the standard `main` function and call it at the bottom of the script.
3. Define a new function named `cake_time` that takes the following **arguments** and returns the baking time **rounded to the nearest 5 minutes**. Make sure to use descriptive variable names for your parameters.
   
   | Argument type | Description                 | Range     |
   | ------------- | --------------------------- | --------- |
   | `int`         | Oven temperature in °F      | 300 - 450 |
   | `float`       | Cake pan diameter in inches | 6 - 12    |

4. The time to bake a cake is calculated as follows[^*]:
   [^*]: This is a completely made up formula. Cake results not guaranteed.

   $$t = 20 + \frac{350 \times (area(d) - area(6))}{2 \times temp}$$

   where:
   - $t$ is the time being calculated
   - $area(d)$ is a function that calculates the area of a circle with a diameter $d$
   - $temp$ is the temperature in °F

   Note that you will have to define and implement an `area` function as well as `cake_time`! I also haven't shown you how to round to the nearest 5, so you may have to do some research on this. Make sure to cite any sources used.

5. In `main`, prompt your user to input the oven temperature and cake pan diameter. Remember that your user has no knowledge of the algorithm - you need to tell them what the numeric ranges are to avoid nonsensical values like 1000 °F!
6. Pass the user input values to `cake_time` and display the result. Your fully functioning program might look something like this, where **bold** text indicates user input:

   <pre>
   Enter the temperature in °F (between 300 and 450): <b>350</b>
   Enter the cake pan diameter in inches (between 6 and 12): <b>8.5</b>
   Your cake should take about 35 minutes to bake.</pre>

## Running tests
This lab has 4 tests: One for the debugging problem, and 3 for the cooking times. **You only need to pass 3 of the 4 tests** to pass the lab. However, GitHub only shows you a green check mark when *all* of the tests are passed. The extra test is provided for an extra challenge.

To check that you passed 3/4 on GitHub, I've added a progress bar to your README file that shows the number of tests passed on your repo homepage. This will automagically update when you push your changes.

If you can't run tests due to a "Test discovery error", use the following command based on your computer system:

| Computer            | Command                    |
| ------------------- | -------------------------- |
| Personal Windows PC | `pip install pytest`       |
| Personal macOS      | `pip3 install pytest`      |
| Lab computer        | `py -m pip install pytest` |

If it still isn't working, you may have different versions of Python installed. Try switching your interpreter by opening the "Command Palette" (`Ctrl + Shift + P`, or selecting the View Menu -> Command Palette), then typing "Python: Select Interpreter". Click on the version marked as "Global".


git commit -m "first commit"
git branch -M main
git remote add origin https://github.com/mru-comp1701-f24/lab_03_template.git
git push -u origin main