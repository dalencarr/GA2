# Dalen Carr–dcarr18@student.gsu.edu
# Matias Espinoza–mespinoza2@student.gsu.edu
# Elizabeth Poythress–epoythress3@student.gsu.edu

import string

string1 = input("Enter a string: ")
string2 = string1
print()

# define functionality of the program
print("Enter p if you'd like to delete all punctuation from the string. \n"
      "Enter c if you'd like to know the number of words in the string. \n"
      "Enter w, then type a word if you'd like to know whether that word is in the string. \n"
      "Enter r if you'd like to replace a word in the string, then enter the word you'd like to replace \n"
      "followed by the word you'd like to replace it with.\n"
      "Enter u to undo all changes.\n"
      "Enter q if you'd like to quit.\n")

# create terminal aesthetic using a 'carrot' and accept user input
command = input(">")

# quit immediately if user enters q
while command != 'q':
    #let user fix mistakes
    if command == 'u':
        string1 = string2
        print(string1)
    elif command == 'p':
    #remove punctuation 
        string1 = string1.translate(str.maketrans('', '', string.punctuation))
        print(string1)
    elif command == 'c':
    # print the number of words
        print(len(string1.split()))
    elif command == 'w':
    # tell whether a word is in the string
        word = input("Enter a word: ")
        if word.lower() in string1.lower():
            print("Yes, that word is in the string.")
        else:
            print(f'No, {word} is not in your string.')
    # let the user replace a word
    elif command == 'r':
        word = input("Enter the word you'd like to replace: ")
        replacement = input("Enter replacement word: ")
        if word in string1:
            string1 = string1.replace(word, replacement)
            print(string1)
        else:
            print("That was not found in the string.")

    command = input(">")
'''potential alternate implementation for quitting the program:
if command == 'q':
    print("Are you sure you want to quit the software? type Yes for confirmation.")
    choice = input(">")
    if choice == "yes" or "Yes":
        print("End of software.")'''
