# Номер посылки на контесте 14 фев 2024, 14:35:02 107341195
def coded_instr(symbol: str) -> str:
    stack: list = []
    multiply: int = 0
    result: str = ''

    for char in symbol:
        if char.isdigit():
            multiply = multiply * 10 + int(char)
        elif char == '[':
            stack.append((result, multiply))
            result = ''
            multiply = 0
        elif char == ']':
            prev_result, prev_multiply = stack.pop()
            result = prev_result + result * prev_multiply
        else:
            result += char

    return result


if __name__ == "__main__":
    instr = input()
    coded_instruction = coded_instr(instr)
    print(coded_instruction)
