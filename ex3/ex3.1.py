def right_justify(s):
    """ Takes a string named s as a parameter and prints the string with enough leading spaces so that the last letter of the string is in column 70 of the display.
    """
    result = ' '
    for i in range(70 - len(s)-1):
        result += ' '
    result = result + s
    print(result)
