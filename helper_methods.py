# This method removes all the unwanted spaces from a string.
# It strips the spaces around the string and removes and double spaces
def remove_spaces(line: str):
    return " ".join(line.split())


# This method calculates the number of different characters in a string
def number_diff_chars(line: str):
    line = line.lower()
    chars = {}
    for c in line:
        if c in "abcdefghijklmnopqrstuvwxyz":
            chars[c] = 1

    return len(chars)


# This method translates the boolean expression into an expressino that python
# can evaluate and returns the number of inputs
def translate_input(bool_expression: str):
    bool_expression = remove_spaces(bool_expression)
    bool_expression = bool_expression.upper()
    bool_expression = bool_expression.replace("AND", "&")
    bool_expression = bool_expression.replace("OR", "|")
    bool_expression = bool_expression.replace("NOT", "~")
    bool_expression = bool_expression.replace("XOR", "^")

    num_inputs = number_diff_chars(bool_expression)
    input_info = {"expression": bool_expression, "inputs": num_inputs}

    return input_info
