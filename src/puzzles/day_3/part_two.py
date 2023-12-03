from dataclasses import dataclass, field
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
    adjacent_parts: list = field(default_factory=list)

    def calculateGearRatio(self):
        if len(self.adjacent_parts) != 2:
            return -1
        return self.adjacent_parts[0].number * self.adjacent_parts[1].number


def getGearRatioSum():
    number_spots = {}
    symbol_spots = {}
    gear_ratios = []
    symbol_regex = re.compile(r"(?P<symbol>[*])")
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
                    row_key = createKey(j, k)
                    if row_key in symbol_spots:
                        symbol_spots[row_key].adjacent_parts.append(number_spot)
                    up_row_key = createKey(up, k)
                    if up_row_key in symbol_spots:
                        symbol_spots[up_row_key].adjacent_parts.append(number_spot)
                    down_row_key = createKey(down, k)
                    if down_row_key in symbol_spots:
                        symbol_spots[down_row_key].adjacent_parts.append(number_spot)
                    if value == 440:
                        pass
                    k += 1
        for _, symbol in symbol_spots.items():
            gear_ratio = symbol.calculateGearRatio()
            if gear_ratio != -1:
                gear_ratios.append(gear_ratio)
    return sum(gear_ratios)


if __name__ == "__main__":
    print(getGearRatioSum())
