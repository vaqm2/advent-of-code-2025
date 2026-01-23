#!/usr/bin/env python3

class Dial:
    def __init__(self):
        self.position = 50
 
    def rotate(self, direction: str, steps: int) -> None:
        if direction == 'L':
            self.position -= steps
        elif direction == 'R':
            self.position += steps
        self.position %= 100


def main() -> None:
    password = 0
    with open('/input/input_day_1_1.txt', 'r') as file:
        clicks = [line.strip() for line in file.readlines()]
    dial = Dial()
    for click in clicks:
        direction = click[0]
        steps = int(click[1:])
        password += steps // 100
        start = dial.position
        dial.rotate(direction, steps)
        end = dial.position
        if direction == "R" and end <= start:
            password += 1
        elif direction == "L" and start > 0 and end >= start:
            password += 1
        elif end == 0:
            password += 1
    print(password)

if __name__ == "__main__":
    main()