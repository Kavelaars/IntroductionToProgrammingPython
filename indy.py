# IK
# indy.py
# MIT A Gentle Introduction to Programming Using Python
# https://ocw.mit.edu/courses/electrical-engineering-and-computer-science/6-189-a-gentle-introduction-to-programming-using-python-january-iap-2011/
# 28 June, 2017 
print "Samenvatting - Hoofdstuk 1, 2 en 4.12"
print "Basic instructions programming languages"
print "- Input, get data example; keyboard"
print "- Output, display data example; to screen"
print "- Math, basic mathematical operations"
print "- Conditional excution, check conditions and excute appropriately"
print "- Repetition, Perform action reapetdly with some variation"
print "Two kinds of programs processes high-level into low level languages"
print "1. Interpreters, sourcecode -> output. processes al little at a time"
print "2. Compilers, translates sourcecode completely before running to objectcode/executable. Once compiled it can run without translation"
print "Different Errors"
print "1. Semantic errors, program will run but does not do what you want it to do"
print "2. Runtime errors, program will not run, are also called exceptions, rare in simple programs"
print "3. Syntax errors, code is not correctly formatted"
print "Programming languages are formal languages that have been designed to express computations"
print "Exercise 1.4: 1. l"
print "Sol1.4_1 - This is @ well structured sentence, but wi|h unrecognizable characters in it."
print "Sol1.4_2 - This is not well a structured. sentence"
print "Parsing, figuring out what a sentence means"
print type("Hello, World")
print type(0)
print type(3.2)
print 1,000,000
who = "The cool kid"
message = "Well hello!"
print message
print "Keywords: and def exec if not return assert del finally import or try break elif for in pass while class else from is print yield continue except global lambda raise"
print "sol 2.5 - put the keyword print before the values"
print "Operators special symbols, operands are the values"
print "Minute variable assigned to 59(int)"
minute = 59
print minute/60 #Int devision
print minute//60 #Double slash means I know this is a integer devision, and it is correct!
print minute*100/60 #You can also put comments at the at of a line
print "not a floating point devision"
what = " doing some Python"
print who + what + " concatination and having, " + "Fun! "*3
# This is a comment and is not visible when the program is executed
print "Chapter 4.12 keyboard input"
#name = raw_input ("What ... is your name? ")
#print name
#prompt = "How fast is a cheata? km/h \n" # \n means newLine, input needs to be int
#speed = input(prompt)
print "Sections 4.1, 4.2, 4.4-4.7, and 6.1-6.2"
quotient = 7/3 
print quotient #Anwser = 2
remainder = 7%3
print remainder #Anwser = 1 left over
print "Exellent for checking if a number is divisible if x % y is zero, this is true"
x = 8
test = x % 2
print test
print "Returns True / False"
print "x == y" # is equel, 
print "x != y" # x is not equal to y
print "x > y" # x is greater than y
print "x < y" # x is less than y
print "x >= y" # x is greater than or equal to y
print "x <= y" # x is less than or equal to y
if x > 0:
    print "x is positive"
print "'pass' statement as a place keeper, for unwritten code"
print "Next:4.5 Alternative execution"
def printParity(x):
    if x%2 == 0:
        print x, "is even"
    else:
        print x, "is odd"
printParity(17)
printParity(quotient)
def makeChoice(choice):
    if choice == 'A':
        functionA()
    elif choice == 'B':
        functionB()
    elif choice == 'C':
        functionC()
    else:
        print "Invalid choice."
choice = 'D'
makeChoice(choice)
print x
if 0 < x:
    if x < 10:
        print "x is a single positive digit AND same as following"
if 0 < x and x < 10:
    print "x is a single positive digit AND same as following"
if 0 < x < 10:
    print "x is is a single positive digit AND semanticly the same as above"
print "multiple assignment, first a = 1 now a = 2, this is not a sign of equality"
print "While statement, count down"
def countdown(n):
    while n > 0:
        print n
        n = n-1
    print "Done!"
countdown(3)
def sequence(m):
    while m != 1:
        print m,
        if m%2 == 0:    #n is even
            m = m/2
        else:
            m = m*3+1
sequence(3)
