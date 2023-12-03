from dataclasses import dataclass
import re


def createKey(row, column):
    key = f"r:{row}c:{column}"
    return key


@dataclass
class NumberSpot:
    row: int
    number: int
    start: int
    end: int


@dataclass
class SymbolSpot:
    row: int
    index: int


def getEnginePartSum():
    symbol_spots = {}
    number_spots = {}
    part_numbers = []
    symbol_regex = re.compile(r"(?P<symbol>[^\d\w.])")
    number_regex = re.compile(r"(?P<number>\d+)")
    with open("src/input/day_three.txt") as file:
        blue_print = file.read()
        blue_print_lines = blue_print.split("\n")
        for i, line in enumerate(blue_print_lines, start=0):
            for symbol in symbol_regex.finditer(line):
                column_start = symbol.start()
                value = symbol.group("symbol")
                key = createKey(i, column_start)
                symbol_spot = SymbolSpot(i, column_start)
                symbol_spots[key] = symbol_spot
        for j, line in enumerate(blue_print_lines, start=0):
            for number in number_regex.finditer(line):
                column_start = number.start()
                column_end = number.end() - 1
                key = createKey(j, column_start)
                value = int(number.group("number"))
                number_spot = NumberSpot(j, value, column_start, column_end)
                number_spots[key] = number_spot

                up = j - 1
                down = j + 1
                left = column_start - 1
                right = column_end + 1
                k = left

                while k <= right:
                    if createKey(j, k) in symbol_spots:
                        part_numbers.append(value)
                        k += 1
                        continue
                    if createKey(j, k) in symbol_spots:
                        part_numbers.append(value)
                        k += 1
                        continue
                    if createKey(up, k) in symbol_spots:
                        part_numbers.append(value)
                        k += 1
                        continue
                    if createKey(down, k) in symbol_spots:
                        part_numbers.append(value)
                        k += 1
                        continue
                    k += 1
    return sum(part_numbers)


if __name__ == "__main__":
    print(getEnginePartSum())
