# This method removes all the unwanted spaces from a string.
# It strips the spaces around the string and removes and double spaces.
def remove_spaces(line: str):
    return " ".join(line.split())


# This method returns a list with all the unique characters in the string.
def characters(line: str):
    line = line.upper()
    chars = set()
    for c in line:
        if c in "ABCDEFGHIJKLMNOPQRSTUVWXYZ":
            chars.add(c)
    return_chars = list(chars)
    return_chars.sort()
    return return_chars


# This method translates the boolean expression into an expressino that python
# can evaluate, returns the number of inputs, and the input characters.
def translate_input(bool_expression: str):
    bool_expression = remove_spaces(bool_expression)
    bool_expression = bool_expression.upper()
    bool_expression = bool_expression.replace("AND", "&")
    bool_expression = bool_expression.replace("OR", "|")
    bool_expression = bool_expression.replace("NOT", "~")
    bool_expression = bool_expression.replace("XOR", "^")

    input_chars = characters(bool_expression)
    input_info = {"expression": bool_expression, "num_inputs": len(input_chars), "input_chars": input_chars}

    return input_info
