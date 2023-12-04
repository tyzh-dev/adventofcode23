from functools import cache
import re


def get_card_score(your_card_numbers, winning_card_numbers):
    matching_card_numbers = len(
        set(your_card_numbers).intersection(winning_card_numbers)
    )
    return matching_card_numbers


def getScratchCardScores(file):
    scratch_card_scores = []
    number_regex = re.compile(r"(?P<number>\d+)")
    for line in file:
        line = line.strip().split(":")[1]
        scratch_cards = line.split(" | ")
        your_card_numbers = number_regex.findall(scratch_cards[0])
        winning_card_numbers = number_regex.findall(scratch_cards[1])
        score = get_card_score(your_card_numbers, winning_card_numbers)
        scratch_card_scores.append(score)
    return scratch_card_scores


def getScratchCardCount():
    scratch_card_scores = []
    with open("src/input/day_4.txt") as file:
        scratch_card_scores = getScratchCardScores(file)

    @cache
    def count_scratch_cards(idx):
        score = scratch_card_scores[idx]
        if score == 0:
            return 1
        count = 1
        for i in range(score):
            count += count_scratch_cards(idx + i + 1)
        return count

    count = sum(count_scratch_cards(j) for j in range(len(scratch_card_scores)))
    return count


if __name__ == "__main__":
    print(getScratchCardCount())
