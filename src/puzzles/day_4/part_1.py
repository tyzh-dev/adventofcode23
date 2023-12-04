import re


def getScratchCardPoints():
    number_regex = re.compile(r"(?P<number>\d+)")
    scratch_card_points = 0
    with open("src/input/day_4.txt") as file:
        for line in file:
            line = line.strip().split(":")[1]
            scratch_cards = line.split(" | ")
            your_card_numbers = number_regex.findall(scratch_cards[0])
            winning_card_numbers = number_regex.findall(scratch_cards[1])

            matching_numbers = list(
                set(your_card_numbers).intersection(winning_card_numbers)
            )
            card_points = 0
            for i, _ in enumerate(matching_numbers):
                if i == 0:
                    card_points += 1
                    continue
                card_points = card_points * 2
            scratch_card_points += card_points
    return scratch_card_points


if __name__ == "__main__":
    print(getScratchCardPoints())
