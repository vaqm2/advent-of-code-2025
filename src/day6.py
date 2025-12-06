"""Day 6 solution."""

#!/usr/bin/env python3


def compute_result_human(worksheet: str) -> int:
    "Compute the result of the worksheet for a human."
    worksheet_list = [x.split() for x in worksheet.splitlines()]
    operands = worksheet_list[len(worksheet_list) - 1]
    result = [int(x) for x in worksheet_list[0]]
    for row in worksheet_list[1:-1]:
        row = [int(x) for x in row]
        for index, operand in enumerate(operands):
            if operand == "+":
                result[index] += row[index]
            elif operand == "*":
                result[index] *= row[index]
    return sum(result)


def compute_result_cephalopod(worksheet: str) -> int:
    "Compute the result of the worksheet for a cephalopod."
    worksheet_list = [list(x) for x in worksheet.splitlines()]
    operands = [x for x in worksheet_list[len(worksheet_list) - 1] if x != " "]
    cephalopod_list = ["" for _ in range(0, len(worksheet_list[0]))]
    for row in worksheet_list[:-1]:
        for index, value in enumerate(row):
            cephalopod_list[index] += value
    operand_index = 0
    results = [0 if x == "+" else 1 for x in operands]
    for value in cephalopod_list:
        if set(value) == {" "}:
            operand_index += 1
            continue
        if operands[operand_index] == "+":
            results[operand_index] += int(value)
        elif operands[operand_index] == "*":
            results[operand_index] *= int(value)
    return sum(results)


def main() -> None:
    """Reads the worksheet input file and prints results for both human and
    cephalopod computations."""
    with open("input_day6.txt", encoding="utf-8") as f:
        worksheet = f.read()
    print(compute_result_human(worksheet))
    print(compute_result_cephalopod(worksheet))


if __name__ == "__main__":
    main()
