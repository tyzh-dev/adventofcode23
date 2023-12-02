def parseGame(text):
    text = text.split(":", 1)[1]
    return text


def parseGameId(text):
    text = text.split(":")[0]
    game_id = "".join(filter(str.isdigit, text))
    return int(game_id)


def parseGameTurns(text):
    game = text.split(";")
    gameTurns = [turn.split(",") for turn in game]
    return gameTurns


def checkTurnCubeValue(turn):
    max_cubes_amount = {"red": 12, "green": 13, "blue": 14}

    turn_values = turn.split()
    turn_cube_amount = int(turn_values[0])
    turn_cube_type = turn_values[-1]

    max_cube_amount = max_cubes_amount[turn_cube_type]
    isValidTurn = turn_cube_amount <= max_cube_amount
    return isValidTurn


def gameIsValid(game):
    isValid = True
    for turns in game:
        for turn in turns:
            isValid = checkTurnCubeValue(turn)
            if isValid == False:
                break
        if isValid == False:
            break
    return isValid


def getPossibleGamesTotal():
    total = 0
    with open("src/input/input_day_two.txt") as file:
        for line in file:
            game = parseGame(line)
            game_id = parseGameId(line)
            gameTurns = parseGameTurns(game)
            if gameIsValid(gameTurns) == True:
                total += game_id
    return total


if __name__ == "__main__":
    print(getPossibleGamesTotal())
