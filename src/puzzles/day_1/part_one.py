def get_digits(line):
    digits = [int(char) for char in line if char.isdigit()]
    return digits


def get_calibration_value(digits):
    first_digit = str(digits[0])
    last_digit = str(digits[-1])
    calibration_value = int(first_digit + last_digit)
    return calibration_value


def getSum():
    with open("lib/input/day_one.txt") as file:
        total = 0
        for line in file:
            digits = get_digits(line)
            calibration_value = get_calibration_value(digits)
            total = total + calibration_value
        return total


if __name__ == "__main__":
    print(getSum())
