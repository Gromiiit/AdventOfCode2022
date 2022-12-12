from enum import Enum

ROCK, PAPER, SCISSORS = "ROCK", "PAPER", "SCISSORS"
GESTURES = { ROCK: 1, PAPER: 2, SCISSORS: 3}
OPONENT_GESTURES = {'A': ROCK, 'B': PAPER, 'C': SCISSORS}
MINE_GESTURES = {'X': ROCK, 'Y': PAPER, 'Z': SCISSORS}
STRATEGY = {'X': 0, 'Y': 3, 'Z': 6}

class rock_paper_scissors(object):
    def __init__(self, gesture):
        self.gesture = gesture

    def __sub__(self, other_gesture):
        if self.gesture == ROCK and other_gesture.gesture == PAPER:
            return 0
        elif self.gesture == PAPER and other_gesture.gesture == ROCK:
            return 6
        elif self.gesture == SCISSORS and other_gesture.gesture == ROCK:
            return 0
        elif self.gesture == ROCK and other_gesture.gesture == SCISSORS:
            return 6
        elif self.gesture == PAPER and other_gesture.gesture == SCISSORS:
            return 0
        elif self.gesture == SCISSORS and other_gesture.gesture == PAPER:
            return 6

        return 3


if __name__ == "__main__":
    points = 0
    with open("day_2_input.txt", 'r') as file:
        for line in file:
            mine, oponent = MINE_GESTURES[line[2]], OPONENT_GESTURES[line[0]]
            if (rock_paper_scissors(ROCK) - rock_paper_scissors(oponent)) == STRATEGY[line[2]]:
                points += rock_paper_scissors(ROCK) - rock_paper_scissors(oponent) + GESTURES[ROCK]
                continue
            elif (rock_paper_scissors(PAPER) - rock_paper_scissors(oponent)) == STRATEGY[line[2]]:
                points += rock_paper_scissors(PAPER) - rock_paper_scissors(oponent) + GESTURES[PAPER]
                continue
            else:
                points += rock_paper_scissors(SCISSORS) - rock_paper_scissors(oponent) + GESTURES[SCISSORS]
            # print(f"{mine} vs {oponent} => {rock_paper_scissors(mine) - rock_paper_scissors(oponent)}")

    print(f"{points}")