# Author: Aaron Amran
# Creation Date: 05th November 2022
# Project: Convert string to ASCII and vice versa and return sum and calculate range between different ASCII characters


print("\nThis is a simple program to: ")
print("1) convert string to ASCII and return sum")
print("2) convert ASCII values (separated by space) to string (word)")
print("3) calculate the distance between ASCII values of a character ")

# important code section for validating user input
while True:
    user_number = input("\nPlease input a number to start: ")
    try:
        user_number = int(user_number)
    except:
        print('\nPlease enter a valid response.')
        continue

    # first condition section
    if user_number == 1:
        string_input = input("\nPlease input a string for ASCII conversion and sum: ")
        string_list = []

        # use loop and ord()
        for letter in string_input:
            string_list.append(letter)

        # convert string list to ascii values
        list_result = []
        for list_elements in string_list:
            # ord() converts a character into an integer that represents the Unicode code of that character
            list_result.extend(ord(num) for num in list_elements)  # num = numbers

        print("The ASCII value(s) of " + string_input + " in a list is " + str(list_result))

        string_sum = sum(list_result)
        print("The sum of ASCII value(s) in", string_input, "is", string_sum)
        # print output uses , and not + because of different data types (cannot concatenate)
        break

    # second condition section
    elif user_number == 2:
        ascii_input = input("\nPlease input ASCII value(s) separated by space to convert to word in string: ")
        # maybe input cannot directly be int because split() is for string

        # user input 99 97 116 (as string) - saved into ascii_list - each item in list is converted from
        # str to int - change items in list from int to char - append all chars into appended str
        # - user output is appended str
        ascii_list = ascii_input.split()
        print("The ASCII value(s) as a list: ", ascii_list)

        # convert each str item in list to int type
        # eval() evaluates the passed string as a Python expression and returns the result
        eval_list = [eval(i) for i in ascii_list]
        print("Updated ASCII list as integer elements is: ", eval_list)

        # convert each int item  to char type
        char_list = [chr(j) for j in eval_list]
        print("The ASCII list numbers replaced with char: ", char_list)

        # append all char from list into one output string
        new_string = ''.join(char_list)
        print("The result string is:", new_string)
        break

    # third condition section
    elif user_number == 3:
        print("\nPlease input two characters to determine their ASCII values and distance.")
        first_char = input("Your first character: ")
        second_char = input("Your second character: ")

        first_ascii = ord(first_char)
        second_ascii = ord(second_char)
        # python has no char type
        # int() is used as direct converter
        # but ord() is used to convert from string of length 1 to ascii
        print("The ASCII value of ", first_char, " is ", first_ascii)
        print("The ASCII value of ", second_char, " is ", second_ascii)

        # abs() is used to return absolute value / magnitude
        fc = int(first_ascii)
        sc = int(second_ascii)
        ascii_distance = abs(sc - fc)
        print("The distance between both values is ", ascii_distance)
        break

    else:
        print('\nPlease enter a valid response.')
        continue

    break




