from dataclasses import replace


def sanatize_input(input):
    possible_inputs = []
    possible_inputs.append(input)
    possible_inputs.append(input+" II")
    if input[0]=='O' or input[0]=='#':
        possible_inputs.append(input[1:])
    if input[0]=='#A':
        possible_inputs.append(input[2:])
    if ']' in input:
        possible_inputs.append(input.replace("]","J"))
    if 'Il' in input:
        possible_inputs.append(input[:-2]+"II")
    return possible_inputs