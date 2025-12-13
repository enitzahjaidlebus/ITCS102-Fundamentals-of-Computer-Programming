import os
import time
enter =input("To Open Program Press Enter:")
time.sleep(.3)
os.system("cls")
print("Opening Program........")
time.sleep(1)
os.system("cls")

print("---------------------------------")
print("    -Python Learning Program-    ")
print("---------------------------------")
name = input("\nWhat Is Your Name? ").upper()
course = input("\nCourse: ").upper()
section = input("\nSection: ").upper()
os.system("cls")

print("Loading........")
time.sleep(1)
os.system("cls")

while True:
    print("------------------------------------")
    time.sleep(.1)
    print("             -MAIN MENU-             ")
    time.sleep(.1)
    print("------------------------------------")
    time.sleep(.1)
    print("\nA - Print Statements")
    time.sleep(.1)
    print("B - Variables")
    time.sleep(.1)
    print("C - Operators")
    time.sleep(.1)
    print("D - Conditionals")
    time.sleep(.1)
    print("E - Loops")
    time.sleep(.1)
    print("F - Lists")
    time.sleep(.1)
    print("G - Funtions")
    time.sleep(.1)
    print("H - Try It Yourself")
    time.sleep(.1)
    print("X - Exit")
    print("\n------------------------------------")
    time.sleep(.1)
    pick = input(f"\nHello {name} from {course} - {section} !!!, Please Choose The One You Like To Learn - ").upper()
    os.system("cls")
    print("Loading.......")
    time.sleep(1)
    os.system("cls")

    if pick == "A":
        while True:
            print("----------------------------")
            print("Welcome To Print Statements")
            print("----------------------------")
            print("\nA - Lesson About Print Statements")
            print("B - Activity About Print Statements")
            print("C - Go Back To Main Menu")
            choice = input("\nPlease Choose The One You Will Take - ").upper()
            os.system("cls")
            
            print("Loading........")
            time.sleep(1)
            os.system("cls")

            if choice == "A":
                while True:
                    print("---------------------------------------------------")
                    print("A print statement is a command that displays text,\nvariables, or other data values to an output device, \ntypically the console or screen.")
                    print("\nFor Example:")
                    print("\nIf you type the command print() \nand put something inside like Hello World,\nthe output should produce Hello World\nImportant note when putting the statement inside\nprint() - use this --> \"\"")
                    print("---------------------------------------------------")
                    answer =input("Type B If You Want To Go Back: ").upper()
                    os.system("cls")
                    if answer == "B":
                        print("Please Wait........")
                        time.sleep(1)
                        os.system("cls")
                        break
                    else:
                        print("--Invalid Input, Please, Try Again--")
                        time.sleep(1)
                        os.system("cls")
                        continue
        
            elif choice == "B":
                while True:
                    print("----------------------------------------------")
                    print("INSTRUCTION")
                    print("\nFor your activity type print()\nand inside the parenthesis add the following:")
                    print("\nHello World\nHappy Coding\nPython Is Fun")
                    print("\nFormat: print(__) print(__) print(__)")
                    print("\nLeaving is prohibited you need to complete\nthe activity first to leave")
                    print("---------------------------------------------")
                    answer = input("\nType your code here - ")
                    os.system("cls")
                    if answer == "print(\"Hello World\") print(\"Happy Coding\") print(\"Python Is Fun\")":
                        print("\nYou Got It Right!!!")
                        time.sleep(1)
                        os.system("cls")
                        print("Leaving Activity........")
                        time.sleep(1)
                        os.system("cls")
                        break
                    else:
                        print("You Got It Wrong, Please Try Again")
                        time.sleep(1)
                        os.system("cls")
                        continue

            elif choice == "C":
                print("Going Back to Main Menu........")
                time.sleep(1)
                os.system("cls")
                break   
            else:
                print("--Invalid Input, Please Try Again--")
                time.sleep(1)
                os.system("cls")
            continue  

    elif pick == "B":
        while True:
            print("---------------------")
            print("Welcome To Variables")
            print("---------------------")
            print("\nA - Lesson About Variables")
            print("B - Activity About Variables")
            print("C - Go Back To Main Menu")
            choice = input("\nPlease Choose The One You Will Take - ").upper()
            os.system("cls")
            
            print("Loading........")
            time.sleep(1)
            os.system("cls")

            if choice == "A":
                while True:
                    print("--------------------------------------------------")
                    print("variables refer to displaying the value currently\nstored in a variable to a standard output device,\ntypically the console or screen. This action is \nperformed using a specific function or statement \nprovided by the programming language. ")
                    print("\nFor Example:\nname = John \nage = 30\n\nprint(\"Name:\", name, \"Age:\", age)\nthe output should be:\n\nName: John Age: 30")
                    print("--------------------------------------------------")
                    answer =input("Type B If You Want To Go Back: ").upper()
                    os.system("cls")
                    if answer == "B":
                        print("Please Wait........")
                        time.sleep(1)
                        os.system("cls")
                        break
                    else:
                        print("--Invalid Input, Please, Try Again--")
                        time.sleep(1)
                        os.system("cls")
                        continue
        
            elif choice == "B":
                while True:
                    print("------------------------------------------------")
                    print("INSTRUCTION\n\nFor your activity answer the following\nquestions by putting the correct letter")
                    print("------------------------------------------------")
                    
                    print("\n1.What is the output if x=hello?\na.hello\nb.HELLO\nc.hi\nd.Error")
                    q1 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q1 == "a":
                        print("Correct")
                    else:
                        print("wrong")
                    
                    print("\n2.Can a variable’s value be changed after it is created?\na.yes\nb.no\nc.maybe\nd.none of the above")
                    q2 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q2 == "a":
                        print("Correct")
                    else:
                        print("wrong")
                    
                    print("\n3.Can a variable store a number?\na.yes\nb.no\nc.maybe\nd.none of the above")
                    q3 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q3 == "a":
                        print("Correct")
                    else:
                        print("wrong")

                    print("\n4.Can a variable store text?\na.yes\nb.no\nc.maybe\nd.none of the above")
                    q4 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q4 == "a":
                        print("Correct")
                    else:
                        print("wrong")

                    print("\n5.Do variables help make programs easier to understand?\na.yes\nb.no\nc.maybe\nd.none of the above")
                    q5 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q5 == "a":
                        print("Correct")
                        print("\nYou've Answer All The Questions")
                        time.sleep(1)
                        os.system("cls")
                        print("Leaving Activity........")
                        time.sleep(1)
                        os.system("cls")
                    else:
                        print("wrong")
                        print("\nYou've Answer All The Questions")
                        time.sleep(1)
                        os.system("cls")
                        print("Leaving Activity........")
                        time.sleep(1)
                        os.system("cls")    
                    break
            elif choice == "C":
                print("Going Back to Main Menu........")
                time.sleep(1)
                os.system("cls")
                break   
            else:
                print("--Invalid Input, Please Try Again--")
                time.sleep(1)
                os.system("cls")
            continue

    elif pick == "C":
        while True:
            print("---------------------")
            print("Welcome To Operators")
            print("---------------------")
            print("\nA - Lesson About Operators")
            print("B - Activity About Operators")
            print("C - Go Back To Main Menu")
            choice = input("\nPlease Choose The One You Will Take - ").upper()
            os.system("cls")
            
            print("Loading........")
            time.sleep(1)
            os.system("cls")

            if choice == "A":
                while True:
                    print("--------------------------------------------------------------------")
                    print("Operators are special symbols or keywords that perform operations\non variables and values, known as operands. They are fundamental\nbuilding blocks that enable data manipulation,\ncomparison, and control of program flow.")
                    print("For Example:\n\nArithmetic Operators:\nPerform mathematical calculations. + Addition, - Subtraction,\n* Multiplication, / Division, % Modulus, returns remainder, \n** exponentiation, power, and // Floor Division, returns \ninteger part of quotient")
                    print("\nAssignment Operators:\nAssign values to variables, including compound assignments that\ncombine an operation and assignment (e.g., +=, -=, *=).")
                    print("\nComparison (Relational) Operators:\nCompare two values and return a Boolean result (True or False).\n== (Equal to), != (Not equal to),\n> (Greater than), < (Less than), >= (Greater than or equal to),\n<= (Less than or equal to).")
                    print("--------------------------------------------------------------------")
                    answer =input("Type B If You Want To Go Back: ").upper()
                    os.system("cls")
                    if answer == "B":
                        print("Please Wait........")
                        time.sleep(1)
                        os.system("cls")
                        break
                    else:
                        print("--Invalid Input, Please, Try Again--")
                        time.sleep(1)
                        os.system("cls")
                        continue
        
            elif choice == "B":
                while True:
                    print("------------------------------------------------")
                    print("INSTRUCTION\n\nFor your activity answer the following\nquestions by putting the correct letter")
                    print("------------------------------------------------")
                    
                    print("\n1.What is an operator in programming?\na) A type of variable\nb) A symbol that performs an operation\nc) A data type\nd) A function")
                    q1 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q1 == "b":
                        print("Correct")
                    else:
                        print("wrong")
                    
                    print("\n2.Which operator is used for addition?\na) -\nb) *\nc) +\nd) /")
                    q2 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q2 == "c":
                        print("Correct")
                    else:
                        print("wrong")
                    
                    print("\n3.What is the result of 5 * 2?\na) 7\nb) 10\nc) 52\nd) 3")
                    q3 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q3 == "b":
                        print("Correct")
                    else:
                        print("wrong")

                    print("\n4.Which operator is used to compare two values for equality?\na) =\nb) !=\nc) ==\nd) >")
                    q4 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q4 == "c":
                        print("Correct")
                    else:
                        print("wrong")

                    print("\n5.Which operator is used to check if one value is greater than another?\na) <\nb) ==\nc) >=\nd) >")
                    q5 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q5 == "d":
                        print("Correct")
                        print("\nYou've Answer All The Questions")
                        time.sleep(1)
                        os.system("cls")
                        print("Leaving Activity........")
                        time.sleep(1)
                        os.system("cls")
                    else:
                        print("wrong")
                        print("\nYou've Answer All The Questions")
                        time.sleep(1)
                        os.system("cls")
                        print("Leaving Activity........")
                        time.sleep(1)
                        os.system("cls")    
                    break

            elif choice == "C":
                print("Going Back to Main Menu........")
                time.sleep(1)
                os.system("cls")
                break   
            else:
                print("--Invalid Input, Please Try Again--")
                time.sleep(1)
                os.system("cls")
            continue  

    elif pick == "D":
        while True:
            print("-----------------------")
            print("Welcome To Conditionals")
            print("-----------------------")
            print("\nA - Lesson About Conditionals")
            print("B - Activity About Conditionals")
            print("C - Go Back To Main Menu")
            choice = input("\nPlease Choose The One You Will Take - ").upper()
            os.system("cls")
            
            print("Loading........")
            time.sleep(1)
            os.system("cls")

            if choice == "A":
                while True:
                    print("--------------------------------------------------------------------------------")
                    print("Conditionals are programming constructs that allow a program to make decisions\nand execute different blocks of code based on whether a specific\ncondition evaluates to True or False.\nThey are a fundamental part of a program's control flow,\nenabling dynamic and responsive behavior.\n\nCore Concept\nDecision Making:\nConditionals enable the program to choose between\nmultiple courses of action, much like real-life\ndecision-making (e.g., \"If it is raining, take an umbrella;\notherwise, wear sunglasses\").\n\nTypes Of Conditional:\nif statement: The simplest form, which executes a\nblock of code only if its condition is True.\nExample\nage = 20\nif age >= 18: \n   print(\"You are eligible to vote.\")\n\nif-else statement: This provides an alternative block\nof code to execute if the if condition is False.\nExample\nnum = -5\nif num > 0:\n   print(\"The number is positive.\")\nelse:\n   print(\"The number is not positive.\")")
                    print("--------------------------------------------------------------------------------")
                    answer =input("Type B If You Want To Go Back: ").upper()
                    os.system("cls")
                    if answer == "B":
                        print("Please Wait........")
                        time.sleep(1)
                        os.system("cls")
                        break
                    else:
                        print("--Invalid Input, Please, Try Again--")
                        time.sleep(1)
                        os.system("cls")
                        continue
        
            elif choice == "B":
                while True:
                    print("------------------------------------------------")
                    print("INSTRUCTION\n\nFor your activity answer the following\nquestions by putting the correct answers")
                    print("------------------------------------------------")
                    
                    print("\n1.Conditionals are used to make decisions in a program.(True/False)")
                    q1 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q1 == "true":
                        print("Correct")
                    else:
                        print("wrong")
                    
                    print("\n2.The else statement runs only when the if condition is true.(True/False)")
                    q2 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q2 == "false":
                        print("Correct")
                    else:
                        print("wrong")
                    
                    print("\n3.Conditionals can compare numbers.(True/False)")
                    q3 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q3 == "true":
                        print("Correct")
                    else:
                        print("wrong")

                    print("\n4.Complete the conditional so the program works correctly.\nChoose the correct operator: >, <, >=, ==\nscore = 75\nif score ___ 60:\n    print(\"Pass\")\nelse:\n    print(\"Fail\")")
                    q4 = input("\nAnswer: ")
                    time.sleep(.5)
                    if q4 == ">=":
                        print("Correct")
                    else:
                        print("wrong")

                    print("\n5.What will the program print?\nage = 16\nif age >= 18:\n    print(\"You are an adult\")\nelse:\n    print(\"You are a minor\")")
                    q5 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q5 == "you are a minor":
                        print("Correct")
                        print("\nYou've Answer All The Questions")
                        time.sleep(1)
                        os.system("cls")
                        print("Leaving Activity........")
                        time.sleep(1)
                        os.system("cls")
                    else:
                        print("wrong")
                        print("\nYou've Answer All The Questions")
                        time.sleep(1)
                        os.system("cls")
                        print("Leaving Activity........")
                        time.sleep(1)
                        os.system("cls")    
                    break

            elif choice == "C":
                print("Going Back to Main Menu........")
                time.sleep(1)
                os.system("cls")
                break   
            else:
                print("--Invalid Input, Please Try Again--")
                time.sleep(1)
                os.system("cls")
            continue  

    elif pick == "E":
        while True:
            print("-----------------")
            print("Welcome To Loops")
            print("-----------------")
            print("\nA - Lesson About Loops")
            print("B - Activity About Loops")
            print("C - Go Back To Main Menu")
            choice = input("\nPlease Choose The One You Will Take - ").upper()
            os.system("cls")
            
            print("Loading........")
            time.sleep(1)
            os.system("cls")

            if choice == "A":
                while True:
                    print("------------------------------------------------------------------")
                    print("Loops is a programming construct that allows a block of code\nto be repeatedly executed. Loops are essential for automating \nrepetitive tasks, processing data collections efficiently,\nand controlling the flow of a program.\nTypes of Loops:\n\nFor Loops\nA for loop is used to iterate over a sequence(such as a list,\ntuple, string, or range) and executes a block of code once for\neach item in the sequence. They are typically used when you know\nthe number of iterations in advance.\nExample:\nfruits = [\"apple\",\"banana\",\"cherry\"]\nfor fruit in fruits:\n   print(fruit)\nthe output will be:\napple\nbanana\ncherry\n\nWhile Loops\nA while loop repeatedly executes a block of code as long as\na specified condition remains True. This type of loop is useful\nwhen the number of iterations is not known beforehand\nand depends on a dynamic condition.\nExample:\ncount = 0\nwhile count < 3:\n   print(count)\n   count += 1\nthe output will be:\n0\n1\n2")
                    print("------------------------------------------------------------------")
                    answer =input("Type B If You Want To Go Back: ").upper()
                    os.system("cls")
                    if answer == "B":
                        print("Please Wait........")
                        time.sleep(1)
                        os.system("cls")
                        break
                    else:
                        print("--Invalid Input, Please, Try Again--")
                        time.sleep(1)
                        os.system("cls")
                        continue
        
            elif choice == "B":
                while True:
                    print("------------------------------------------------")
                    print("INSTRUCTION\n\nFor your activity answer the following\nquestions by putting the correct answers")
                    print("------------------------------------------------")
                    print("\n1.Find the output of the given below. Use space when you have multiple answer.\nfor i in range(1,6):\n   print(i)")
                    q1 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q1 == "1 2 3 4 5":
                        print("Correct")
                    else:
                        print("wrong")

                    print("\n2.Complete the loop so it prints numbers from 1 to 5.\nfor i in range(___):\n   print(i)")
                    q2 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q2 == "1,6":
                        print("Correct")
                    else:
                        print("wrong")

                    print("\n3.What will the program print? Use space when you have multiple answer.\nfor i in range(2, 8, 2):\n   print(i)")
                    q3 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q3 == "2 4 6":
                        print("Correct")
                        print("\nYou've Answer All The Questions")
                        time.sleep(1)
                        os.system("cls")
                        print("Leaving Activity........")
                        time.sleep(1)
                        os.system("cls")
                    else:
                        print("wrong")
                        print("\nYou've Answer All The Activity,")
                        time.sleep(1)
                        os.system("cls")
                        print("Leaving Activity........")
                        time.sleep(1)
                        os.system("cls")    
                    break
            elif choice == "C":
                print("Going Back to Main Menu........")
                time.sleep(1)
                os.system("cls")
                break
            else:
                print("--Invalid Input, Please Try Again--")
                time.sleep(1)
                os.system("cls")
            continue  

    elif pick == "F":
        while True:
            print("-----------------")
            print("Welcome To Lists")
            print("-----------------")
            print("\nA - Lesson About Lists")
            print("B - Activity About Lists")
            print("C - Go Back To Main Menu")
            choice = input("\nPlease Choose The One You Will Take - ").upper()
            os.system("cls")
            
            print("Loading........")
            time.sleep(1)
            os.system("cls")

            if choice == "A":
                while True:
                    print("---------------------------------------------------------------------------------------------------------------------------------------")
                    print("List is a built-in, versatile data structure used to store a collection\nof items in a single variable. Lists are defined by\nenclosing elements within square brackets [] and are\none of Python's most fundamental and widely used data types.")
                    print("\nKey Characteristics of Python Lists\nOrdered:\nThe elements in a list maintain their specific insertion order, which will not change unless explicitly modified.\nMutable (Changeable):\nYou can change, add, or remove items from a list after it has been created, using various methods like append(), insert(), remove(), \nor direct assignment to an index.\nAllow Duplicates:\nBecause lists are indexed, they can contain multiple items with the same value.\nHeterogeneous (Mixed Data Types):\nA single list can store elements of different data types simultaneously, such as integers, strings, booleans, and even other lists.\nZero-Indexed:\nElements are accessed using a numerical index, starting from 0 for the first item.\nExample:\n\nfruits = [\"apple\",\"banana\",\"cherry\"]\n\nfirst_item = fruits[0]\n\nlast_item = fruits[-1]\n\nprint(first_item,\"and\",last_item)\n\nthe output will be:\n\n\"apple\" and \"cherry\"\n\nCommon List Methods\nappend(item): Adds an item to the end of the list.\ninsert(index, item): Inserts an item at a specified index.\nremove(item): Removes the first occurrence of a specific value.\npop(index): Removes and returns the item at a given index (or the last item if no index is specified).\nsort(): Sorts the list in place in ascending order.\nlen(): A built-in function (not a method) used to get the number of items in the list.")
                    print("---------------------------------------------------------------------------------------------------------------------------------------")
                    answer =input("Type B If You Want To Go Back: ").upper()
                    os.system("cls")
                    if answer == "B":
                        print("Please Wait........")
                        time.sleep(1)
                        os.system("cls")
                        break
                    else:
                        print("--Invalid Input, Please, Try Again--")
                        time.sleep(1)
                        os.system("cls")
                        continue
        
            elif choice == "B":
                while True:
                    print("------------------------------------------------")
                    print("INSTRUCTION\n\nFor your activity answer the following\nquestions by putting the correct answers")
                    print("------------------------------------------------")
                    print("\n1.What will the program print?\nfruits = [\"apple\", \"banana\", \"cherry\"]\nprint(fruits[1])")
                    q1 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q1 == "banana":
                        print("Correct")
                    else:
                        print("wrong")
                    
                    print("\n2.Complete the code to add \"orange\" to the list:\nfruits = [\"apple\", \"banana\", \"cherry\"]\nfruits.____(\"orange\")\nprint(fruits)")
                    q2 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q2 == "append":
                        print("Correct")
                    else:
                        print("wrong")
                    
                    print("\n3.What command in list that accend the items in order?\na.append()\nb.pop()\nc.sort()\nd.insert()")
                    q3 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q3 == "c":
                        print("Correct")
                        print("\nYou've Answer All The Questions")
                        time.sleep(1)
                        os.system("cls")
                        print("Leaving Activity........")
                        time.sleep(1)
                        os.system("cls")
                    else:
                        print("wrong")
                        print("\nYou've Answer All The Questions")
                        time.sleep(1)
                        os.system("cls")
                        print("Leaving Activity........")
                        time.sleep(1)
                        os.system("cls")
                    break    

            elif choice == "C":
                print("Going Back to Main Menu........")
                time.sleep(1)
                os.system("cls")
                break   
            else:
                print("--Invalid Input, Please Try Again--")
                time.sleep(1)
                os.system("cls")
            continue  

    elif pick == "G":
        while True:
            print("---------------------")
            print("Welcome To Functions")
            print("---------------------")
            print("\nA - Lesson About Functions")
            print("B - Activity About Functions")
            print("C - Go Back To Main Menu")
            choice = input("\nPlease Choose The One You Will Take - ").upper()
            os.system("cls")
            
            print("Loading........")
            time.sleep(1)
            os.system("cls")

            if choice == "A":
                while True:
                    print("----------------------------------------------------------------------------------------------------------------")
                    print("Function is a named, reusable block of code that performs a specific task when called.\nIt is a fundamental building block of organized, modular programming that\nallows developers to break down complex problems into smaller,\nmanageable pieces, making code easier to read, test, debug, and maintain./n/nKey Concepts\n\nModularity:\nFunctions divide a large program into smaller, independent modules, each with a specific responsibility.\n\nReusability:\nOnce a function is defined, it can be called multiple times from different parts of a program,\neliminating the need to write the same code repeatedly (adhering to the \"Don't Repeat Yourself\" principle).\n\nAbstraction:\nFunctions hide the internal implementation details of an operation.\nYou only need to know what a function does and how to use\nits interface (inputs and outputs), not how it works internally.\n\nScope:\nVariables defined inside a function have a local scope,\nmeaning they are separate from variables with the same name outside the function.\nThis prevents accidental data interference.")
                    print("\nExample:\n\ndef add_numbers(a, b):\n-Adds two numbers and returns the sum\nsum_result = a + b\nreturn sum_result\n\n-Call the function and store the result\nresult = add_numbers(5, 3)\n\n-Print the resul\nprint(\"The sum is:\" result)\n\n-Output\nThe sum is: 8")
                    print("----------------------------------------------------------------------------------------------------------------")
                    answer =input("Type B If You Want To Go Back: ").upper()
                    os.system("cls")
                    if answer == "B":
                        print("Please Wait........")
                        time.sleep(1)
                        os.system("cls")
                        break
                    else:
                        print("--Invalid Input, Please, Try Again--")
                        time.sleep(1)
                        os.system("cls")
                        continue
        
            elif choice == "B":
                while True:
                    print("------------------------------------------------")
                    print("INSTRUCTION\n\nFor your activity answer the following\nquestions by putting the correct letter")
                    print("------------------------------------------------")
                    
                    print("\n1.What is a function?\na) A type of variable\nb) A block of code that performs a task\nc) A data type\nd) A loop")
                    q1 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q1 == "b":
                        print("Correct")
                    else:
                        print("wrong")
                    
                    print("\n2.Why are functions used in programs?\na) To make programs longer\nb) To repeat code without writing it again\nc) To slow down programs\nd) To store data")
                    q2 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q2 == "b":
                        print("Correct")
                    else:
                        print("wrong")
                    
                    print("\n3.Which keyword is used to define a function in Python?\na) function\nb) define\nc) def\nd) func")
                    q3 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q3 == "c":
                        print("Correct")
                    else:
                        print("wrong")

                    print("\n4.What is a parameter in a function?\na) The value a function returns\nb) A variable used inside a function\nc) A value passed into a function\nd) The name of the function")
                    q4 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q4 == "c":
                        print("Correct")
                    else:
                        print("wrong")

                    print("\n5.What does a function return?\na) Only numbers\nb) Only text\nc) The result of the function\nd) The function name")
                    q5 = input("\nAnswer: ").lower()
                    time.sleep(.5)
                    if q5 == "c":
                        print("Correct")
                        print("\nYou've Answer All The Questions")
                        time.sleep(1)
                        os.system("cls")
                        print("Leaving Activity........")
                        time.sleep(1)
                        os.system("cls")
                    else:
                        print("wrong")
                        print("\nYou've Answer All The Questions")
                        time.sleep(1)
                        os.system("cls")
                        print("Leaving Activity........")
                        time.sleep(1)
                        os.system("cls")    
                    break
            elif choice == "C":
                print("Going Back to Main Menu........")
                time.sleep(1)
                os.system("cls")
                break   
            else:
                print("--Invalid Input, Please Try Again--")
                time.sleep(1)
                os.system("cls")
            continue  

    elif pick == "X":   
        print("Exiting Program........")
        time.sleep(1)
        os.system("cls")
        print(f"Thank You {name} For Using \"Python Learning Program\" ")
        time.sleep(1)
        break

    elif pick == "H":
       while True:
        print("---------------------------")
        print("Welcome To Try It Yourself")
        print("---------------------------")        
        print("Remider always save before closing notepad (ctrl + s)")
        try_code = input("A - Try Code\nB - Edit Code\nC - Result\nX - Exit\nChoose: ").lower()
        os.system("cls")

        print("Loading........")
        time.sleep(1)
        os.system("cls")

        if try_code == "a":
            os.system("type nul > try.py")
            os.system("notepad try.py")
            input("Enter to go back")
            os.system('cls')
            continue
        elif try_code == "b":
            file_path = "try.py"
            with open("try.txt", "r") as file:
                content = file.read()
                print(content)
        elif try_code == "c":
            os.system("cls")
            os.system("python try.txt")
            time.sleep(3)
            os.system("cls")
            continue
        elif try_code == 'x':
            print("Going Back to Main Menu........")
            time.sleep(1)
            os.system("cls")
            break   
        else:
            print("--Invalid Input, Please Try Again--")
            time.sleep(1)
            os.system("cls")
            continue  
    
    else:
        print("Invalid Input, Try Again........")
        time.sleep(1)
        os.system("cls")
        continue