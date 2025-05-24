"""
1.  Basic: Explain the purpose of the unittest framework's setUp and tearDown methods. When would you use them in a test suite?

The unittest framework's setUp and tearDown methods are methods that are called each time a test case is handled. Each time a test case is handled, setUp is initially called which is utilized to setup the variables and objects needed to test on for each test case and once each test has finished, tear down gets called which is used to clean up any lingering artifacts so that there aren't any outside factors affecting the test cases. You would use setUp when you need to initialize or set up the same objects between the multiple different test cases. You would use tearDown when you need to likewise destroy or clean up any objects or variables that you've created. If working on networks or files you can also use the tear down section to close up any opened files/network connections.

2. Intermediate: Given the following code snippet, write a complete test case that tests all of the functionality of the Rectangle class:
"""


class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def area(self):
        return self.width * self.height

    def perimeter(self):
        return 2 * (self.width + self.height)


import unittest
from practice_quiz import Rectangle


class TestRectangle(unittest.TestCase):
    def setUp(self):
        self.rectangle = Rectangle(2, 5)

    def test_area(self):
        self.assertEqual(10, self.rectangle.area())

    def test_perimeter(self):
        self.assertEqual(14, self.rectangle.perimeter())


if __name__ == "__main__":
    unittest.main()

"""
3. Intermediate: What is the SEAT approach in testing? Provide a simple example of how you would structure a test following this approach.

The SEAT approach is an acryonym which describes a set of steps to follow in testing. The acronym stands for
S - Set up necessary objects required for testing
E - Execute code against objects that we are testing
A - Assert that executed code worked correctly
T - Tear down and clean any lingering artifacts

A simple example of how I would structure a test would be testing if my Number class correctly add together right. I would begin with setting up the necessary number objects. Next I would execute my code against my number objects by adding two number objects together with the plus operator. Then I would assert if the resulting number is equal to the number it should be. Lastly I would think about tearing down and cleaning any lingering artifacts which for this scenario I wouldn't have to do since it's a pretty simple example.

5. Basic: Describe the standard project directory layout for a Python package. What files are typically included and what purpose does each serve?

The standard project directory layout typically consists of your main package directory containing a src directory, a tests/resources directory, a LICENSE file, a pyproject.toml file, and a README.md

The src directory is where your source code goes which contains all of the project's files as well as an __init__.py file which tells python that this directory contains a package.

The tests/resources directory contain all of the tests and extra resources/files that you used for your project.

The License file describes how other users may use your package.

The pyproject.toml file provides the project metadata to PyPI and build suistem requirements like any dependecies required to install the package.

The Readme.md file is a markdown file that is displayed on the package's PyPI page that describes what the package is used for

6. Intermediate: Explain the difference between a module and a package in Python. How would you create a package that contains multiple modules?
A module is a python file dedicated to providing useful methods for any other python file to import and utilize. Similarily a python script is also a python file with the main difference being that python scripts are meant to be executed and for code to be executed in. Packages in python are just a collection of modules. Packages can contain multiple modules as well as other file types and directories. Packages can be thought up as a the toolbox, with modules being the different tools inside of the toolbox. To create a package that contains multiple modules you would just create a folder containing all of your python module files, and add a __init__.py file to tell python that this directory is a package. Then you can import the package like a module and grab individual modules be indexing from the package in the import statement.
Example:
import package.module_a as module_a
import package.module_b as module_b

Here we are importing two modules from the same package

8. Intermediate:
What is code coverage in the context of testing? How would you measure code coverage for a Python project, and what are some limitations of relying solely on code coverage metrics?

Code coverage is a metric describing the amount of code in your project that has been tested over. You can measure code coverage for a python project by installing the coverage package through pip, and running the coverage command over your project to determine how much of your code you've tested. Some limitations on code coverage metrics is that they are not 100% accurate, and can miss indirect or subtle test cases when it comes to your code.
"""
