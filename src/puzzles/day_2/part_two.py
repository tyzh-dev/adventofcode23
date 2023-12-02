def parseGame(text):
    text = text.split(":", 1)[1]
    return text


def parseGameTurns(text):
    game = text.split(";")
    gameTurns = [turn.split(",") for turn in game]
    return gameTurns


def getCubeValues(cube):
    cube_values = cube.split()
    cube_amount = int(cube_values[0])
    cube_type = cube_values[-1]
    return cube_amount, cube_type


def getMinimumPowerSet(turns):
    min_cubes_powerset = {}
    for turn in turns:
        for cube in turn:
            cube_amount, cube_type = getCubeValues(cube)
            if cube_type not in min_cubes_powerset:
                min_cubes_powerset[cube_type] = cube_amount
            elif cube_amount > min_cubes_powerset[cube_type]:
                min_cubes_powerset[cube_type] = cube_amount
    return (
        min_cubes_powerset["red"]
        * min_cubes_powerset["green"]
        * min_cubes_powerset["blue"]
    )


def getMinimumCubePowerSet():
    total = 0
    with open("src/input/input_day_two.txt") as file:
        for line in file:
            game = parseGame(line)
            game_turns = parseGameTurns(game)
            minimum_game_cube_powerset = getMinimumPowerSet(game_turns)
            total += minimum_game_cube_powerset
    return total


if __name__ == "__main__":
    print(getMinimumCubePowerSet())
