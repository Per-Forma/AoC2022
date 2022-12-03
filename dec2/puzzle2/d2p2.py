# Key column1 opponent choice: A = rock, B = paper, C = scissor
# Key comumn2 how round should end: X = lose, Y = draw, Z = win
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
        sel_points = 0
        player_choice = ''
        choices = play_round.split()
        opponent_choice = choices[0]
        round_outcome = choices[1]
        # Convert opponent choice code to txt for easier decoding
        if opponent_choice == 'A':
            opponent_choice = 'rock'
        elif opponent_choice == 'B':
            opponent_choice = 'paper'
        elif opponent_choice == 'C':
            opponent_choice = 'scissor'
        else:
            sys.exit("Bad opponent choice in input file. Round is " + play_round)

        # Convert outcome code to readable word
        if round_outcome == 'X':
            round_outcome = 'lose'
        elif round_outcome == 'Y':
            round_outcome = 'draw'
        elif round_outcome == 'Z':
            round_outcome = 'win'

        # Determine the player's choice necessary to result in key's outcome
        if round_outcome == 'draw':
            player_choice = opponent_choice
        elif round_outcome == 'lose':
            if opponent_choice == 'rock':
                player_choice = 'scissor'
            elif opponent_choice == 'paper':
                player_choice = 'rock'
            elif opponent_choice == 'scissor':
                player_choice = 'paper'
        elif round_outcome == 'win':
            if opponent_choice == 'rock':
                player_choice = 'paper'
            if opponent_choice == 'paper':
                player_choice = 'scissor'
            if opponent_choice == 'scissor':
                player_choice = 'rock'

        # Assign selection points for player's choice. Could be done above, but this exists from puzzle 1 already
        if player_choice == 'rock':
            sel_points = play_points_rock
        elif player_choice == 'paper':
            sel_points = play_points_paper
        elif player_choice == 'scissor':
            sel_points = play_points_scissor
        else:
            sys.exit("Bad player choice in input file. Round is " + play_round)

        # Determine winner
        # Note: This still works, but could be refactored due to knowing round outcome due to key column 2 input
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
