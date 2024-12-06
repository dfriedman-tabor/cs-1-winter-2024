# david friedman
# homework 1 example
# help from mr voci, cgpt, femi

numberRight = 0

answer1 = input("what is the biggest planet? ")

if answer1 == "jupiter":
    print("correct!")
    numberRight += 1
else:
    print("nope. the answer is jupiter")

answer2 = input("what team will win the super bowl? ")

if answer2 == "eagles":
    print("correct!")
    numberRight += 1
else:
    print("nope. go birds")

answer3 = input("what language is this written in? ")

if answer3 == "python":
    print("correct!")
    numberRight += 1
else:
    print("no, this is python")


print("You got " + numberRight + " correct")





