# Key column1 opponent choice: A = rock, B = paper, C = scissor
# Key comumn2 player choice: X = rock, Y = paper, Z = scissor
# Scoring: Sum of player score all rounds. Rock = 1, Paper = 2, Scisors = 3 plus 3 if player draw or 6 if player win
import sys

play_points_rock = 1
play_points_paper = 2
play_points_scissor = 3
def ingestdata(data):
    ingesteddata = []
    player_points = 0
    for play_round in data:
        if play_round == '\n':
            continue
        play_round = play_round.strip('\n')  # Remove newline char from input line
        choices = play_round.split()
        opponent_choice = choices[0]
        player_choice = choices[1]
        # Convert opponent choice code to txt for easier decoding
        if opponent_choice == 'A':
            opponent_choice = 'rock'
        elif opponent_choice == 'B':
            opponent_choice = 'paper'
        elif opponent_choice == 'C':
            opponent_choice = 'scissor'
        else:
            sys.exit("Bad opponent choice in input file. Round is " + play_round)

        # Convert player choice code to txt for easier decoding and to more easily deal with assumptions
        # Also assign selection points for player's choice
        sel_points = 0  # Initialize selection points value
        if player_choice == 'X':
            player_choice = 'rock'
            sel_points = play_points_rock
        elif player_choice == 'Y':
            player_choice = 'paper'
            sel_points = play_points_paper
        elif player_choice == 'Z':
            player_choice = 'scissor'
            sel_points = play_points_scissor
        else:
            sys.exit("Bad player choice in input file. Round is " + play_round)

        # Determine winner
        winner = ''
        if opponent_choice == player_choice:
            winner = 'draw'
            win_points = 3
        elif opponent_choice == 'rock':
            if player_choice == 'paper':
                winner = 'player'
            else:
                winner = 'opponent'
        elif opponent_choice == 'paper':
            if player_choice == 'scissor':
                winner = 'player'
            else:
                winner = 'opponent'
        elif opponent_choice == 'scissor':
            if player_choice == 'rock':
                winner = 'player'
            else:
                winner = 'opponent'

        # Test for failed logic
        if winner == '':
            sys.exit("Winner was not determined. Error in logic")

        if winner == 'player':
            win_points = 6
        elif winner == 'opponent':
            win_points = 0
        round_points = win_points + sel_points
        player_points += round_points
    return player_points


if __name__ == '__main__':
    inputdata = open('input', 'r')
    ingested = ingestdata(inputdata)
    print(ingested)
