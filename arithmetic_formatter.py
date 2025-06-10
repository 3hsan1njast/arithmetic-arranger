def arithmetic_arranger(problems, show_answers=False):
    if len(problems) > 5: return 'Error: Too many problems.'

    top_row = ""
    bottom_row = ""
    dashes = ""
    answers = ""

    for problemIndex in range(len(problems)):
        problem = problems[problemIndex].split(' ')
        num1 = problem[0]
        num2 = problem[2]
        if not str.isdigit(num1) or not str.isdigit(num2): return 'Error: Numbers must only contain digits.'
        if len(num1) > 4 or len(num2) > 4: return 'Error: Numbers cannot be more than four digits.'
        operator = problem[1]
        if operator not in ['+', '-']: return "Error: Operator must be '+' or '-'."
        width = max(len(num1), len(num2)) + 2
        for _ in range(0, width - len(num1)):
            top_row += " "
        top_row += num1
        bottom_row += operator
        for _ in range(1, width - len(num2)):
            bottom_row += " "
        bottom_row += num2
        for _ in range(0, width):
            dashes += "-"
        result = int(num1) + int(num2) if operator == "+" else int(num1) - int(num2)
        for _ in range(0, width - len(str(result))):
            answers += " "
        answers += str(result)
        if problemIndex != len(problems) - 1:
            top_row += "    "
            bottom_row += "    "
            dashes += "    "
            if show_answers: answers += "    "

    if not show_answers: return f'{top_row}\n{bottom_row}\n{dashes}'
    if show_answers: return f'{top_row}\n{bottom_row}\n{dashes}\n{answers}'
