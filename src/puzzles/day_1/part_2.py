def get_calibration_value(first_digit, last_digit):
    calibration_value = int(first_digit + last_digit)
    return calibration_value


def get_digits(text):
    number_values = {
        "1": "1",
        "2": "2",
        "3": "3",
        "4": "4",
        "5": "5",
        "6": "6",
        "7": "7",
        "8": "8",
        "9": "9",
        "one": "1",
        "two": "2",
        "three": "3",
        "four": "4",
        "five": "5",
        "six": "6",
        "seven": "7",
        "eight": "8",
        "nine": "9",
    }

    digits = 0
    first_digit = 0
    last_digit = 0

    previous_last_index = -1
    previous_first_index = len(text) - 1

    for num in number_values:
        first_number_index = text.find(num)
        if -1 < first_number_index < previous_first_index:
            previous_first_index = first_number_index
            first_digit = number_values[num]

        last_number_index = text.rfind(num)
        if last_number_index >= previous_last_index:
            previous_last_index = last_number_index
            last_digit = number_values[num]
    digits = get_calibration_value(first_digit, last_digit)
    return digits


def getSum():
    with open("src/input/day_1.txt") as file:
        total = 0
        for line in file:
            digits = get_digits(line)
            total += digits
        return total


if __name__ == "__main__":
    print(getSum())
