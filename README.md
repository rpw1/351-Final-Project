# **K-NN Number and Symbol Recognition CSCI-B351 Final Project**
By Ryan Williams and Carson Crick

## **Setup**
This repository uses a third party software called python-mnist.

The third party software can be installed by using the command:
```shell
$ pip install python-mnist
```

The PyPi page can by found [here][1] and the Github page for python-mnist is [here][2]

If there are issues with installing python-minst, we created a virtual environment to run the project using pipenv.
A guide to setup pipenv can be found [here][3]
Just go to the path of the repository using terminal or git and run:
```shell
$ pip install --user pipenv
$ cd 351-Final-Project
$ pipenv install
$ pipenv run python src/python_file
```

## **Data**
In this project, we use the [MNIST database][4] for our number testing and training data.

The training and testing data for our symbols:

* Multiplication (*)
* Division (*)
* Addition (+)
* Subtraction (-)

Each picture has a 28 x 28 grid filled with gray scale values from 0-255.
The python-mist package has a display function that prints out the grid with @ and dots.
The display function counts any gray scale value equal to or under 200 as noise.
Here is an example of testing/training data. This is a 9 from the MNIST database using the display function.

```shell
............................
............................
............................
.............@@@............
...........@@@@@@...........
.........@@@....@...........
.........@@........@@.......
........@@........@@........
........@.........@@........
........@.........@@........
.......@@........@@@........
.......@@........@@.........
.......@@.......@@@.........
........@@....@@@@@.........
.........@@@@@..@@..........
................@@..........
................@@..........
................@@..........
...............@@...........
...............@@...........
...............@@...........
...............@............
..............@@............
............................
............................
```

## **Using The Calculator**

* Enter one symbol/number at a time
* Only enter positive single digit numbers at a time (0-9)
* Acceptable symbols are for addition, subtraction, multiplication and division (+, -, *, /)
* To create a multiple digit number then enter numbers back to back
* Input 's' to have the program solve the inputted function
* Input 'r' to reset the equation
* Input 'd' to see a simple demo of the program
* Input 'e' to solve a random equation
* Input 'p' to print out your current list of arguments
* Input 'q' to quit the program
* Input 'c' to clear the terminal and list options again



[1]: https://pypi.org/project/python-mnist/

[2]: https://github.com/sorki/python-mnist

[3]: https://packaging.python.org/tutorials/managing-dependencies/

[4]: http://yann.lecun.com/exdb/mnist/
