# Created By  : Braden Powell
# Created Date: May 19, 2022

# Hello World! Thanks for exploring the opportunity to join us at DataBased.
# We wish you the best with the assessment.
# Please complete and come prepared to present your solutions to the team.

# Instructions: Solve the problems listed below.
# There are more details about the problems in the provided README, we highly
# recommend reading through the README before solving the problems.

# In order to run the program install Python if not already installed.
# Then change your current directory to the same as the file
# Run the command `python DataBased_Python_Assessment.py` or `python3 DataBased_Python_Assessment.py`
# If you see 'PASSED' that means you passed the all test cases in the test function,
# it does not mean your solution is 100% correct. There may be edge cases you
# should add tests for on your own!

# PROBLEM 1 - Least Factorial
# Given an integer n, find the minimal k such that
# k = m! (where m! = 1 * 2 * ... * m) for some integer m; k ≥n. In other
# words, find the smallest factorial which is not less than n.

def leastFactorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact = fact * i
        if fact >= n:  # found k
            break
    return fact


def testLeastFactorial():
    print('-' * 20)
    print('Part 1: Least Factorial')

    assert leastFactorial(-2) == 1
    assert leastFactorial(0) == 1
    assert leastFactorial(1) == 1
    assert leastFactorial(2) == 2
    assert leastFactorial(5) == 6
    assert leastFactorial(6) == 6
    assert leastFactorial(17) == 24
    assert leastFactorial(106) == 120

    print('PASSED PROBLEM 1!')


# PROBLEM 2 - Reclying Lipstick
# You own a lipstick business. When a lipstick container is empty, there is actu-
# ally some leftover lipstick at the bottom that cannot be used because it is not
# accessible. Being an environmentally friendly business owner, you would like to
# recycle the leftover lipstick to make more. As a business, you know you need
# ‘numberOfLeftoversNeeded‘ to make a new lipstick. You have ‘numberOfLip-
# sticks‘ in your possession. What’s the total number of lipsticks you can sell
# assuming that each of your customers return their leftovers

def getTotalNumberOfLipsticks(numberOfLipsticks, numberOfLeftoversNeeded):
    # sell lipsticks we have, they all create leftovers
    totalSold = numberOfLipsticks
    leftovers = numberOfLipsticks
    while True:  # do while
        recycledLipsticks = leftovers // numberOfLeftoversNeeded  # make new lipsticks from leftovers
        totalSold += recycledLipsticks  # sell recycled lipsticks
        leftovers = (leftovers % numberOfLeftoversNeeded) + recycledLipsticks  # old + new leftovers

        if leftovers < numberOfLeftoversNeeded:
            break
    return totalSold


def testLipsticks():
    print('\n' + '-' * 20)
    print('Part 2: Lipsticks')
    assert getTotalNumberOfLipsticks(0, 2) == 0
    assert getTotalNumberOfLipsticks(1, 2) == 1
    assert getTotalNumberOfLipsticks(2, 3) == 2
    assert getTotalNumberOfLipsticks(5, 2) == 9
    assert getTotalNumberOfLipsticks(15, 5) == 18
    assert getTotalNumberOfLipsticks(100, 5) == 124
    # NOTE: numberOfLeftoversNeeded must be >= 2 otherwise we would be selling the same lipstick infinite times

    print('PASSED PROBLEM 2!')


# PROBLEM 3 - Students and Treats
# A school teacher wants to hand out treats to his students. The teacher de-
# cides the best way to divide the treats is to have the students sit in a circle of
# sequentially numbered chairs. A chair number will be drawn from a hat. Begin-
# ning with the student in drawn chair, one treat will be handed to each student
# sequentially going around the circle until all treats have been distributed.
# The teacher wants to have the students involved in sharing treats. He decides
# that whoever gets the very last treat, will be the student who makes the treats
# for the next game. Determine the chair number occupied by the student who
# will receive the last treat.

# For example, there are 4 students and 6 treats. The students arrange them-
# selves in seats numbered 1 to 4. Let’s suppose 2 is drawn from the hat. Students
# receive treats at positions 2,3,4,1,2,3. The student who gets the last treat is in
# chair number 3

def getLastStudent(numberOfStudents, treats, startingChair):
    chairsToShift = abs((treats % numberOfStudents) - 1)  # Ignore complete cycles. 1 remainder means we shift 0 seats
    endingChair = (startingChair + chairsToShift)
    if endingChair > numberOfStudents:  # if we are looping back to student 1
        endingChair -= numberOfStudents
    return endingChair


def testLastStudent():
    print('\n' + '-' * 20)
    print('Part 3: Students and Treats')
    assert getLastStudent(1, 1, 1) == 1
    assert getLastStudent(5, 2, 1) == 2
    assert getLastStudent(5, 2, 2) == 3
    assert getLastStudent(3, 7, 3) == 3
    assert getLastStudent(7, 19, 2) == 6
    assert getLastStudent(10, 15, 2) == 6
    assert getLastStudent(1000, 2777, 234) == 10

    print('PASSED PROBLEM 3!')


def getPairsOfShoes(listOfShoes):
    pairs = 0
    while len(listOfShoes):
        shoeToPair = listOfShoes[0]  # shoe we are finding matches for
        pairs += (len([shoe for shoe in listOfShoes if shoe == shoeToPair])) // 2
        listOfShoes = [shoe for shoe in listOfShoes if shoe != shoeToPair]  # remove shoe we have paired
    return pairs


# PROBLEM 4 - Pairs of Shoes
# Given an array of strings that represent a type of shoe, return how many matching
# pairs of shoes can be made?

def testPairsOfShoes():
    print('\n' + '-' * 20)
    print('Part 4: Pairs of Shoes')
    assert getPairsOfShoes(["red", "blue", "red", "green", "green", "red"]) == 2
    assert getPairsOfShoes(["green", "blue", "blue", "blue", "blue", "blue", "green"]) == 3
    assert getPairsOfShoes([1, 2, 1, 3, 3, 1, 4, 4, 3]) == 3
    assert getPairsOfShoes([[1, 1], [2, 1], [1, 1], [2, 3], [2, 1]]) == 2
    assert getPairsOfShoes([1, 2, 3, 4, 5, 6, 7]) == 0
    # NOTE: this does not treat "Green" and "green" as the same shoe. Should it? What about spaces in the string?

    print('PASSED PROBLEM 4!')
    print('\n\nCongratulations!!')


testLeastFactorial()
testLipsticks()
testLastStudent()
testPairsOfShoes()

