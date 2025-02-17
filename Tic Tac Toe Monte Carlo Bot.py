"""
Monte Carlo Tic-Tac-Toe Player
"""

import random
import poc_ttt_gui
import poc_ttt_provided as provided


# Constants for Monte Carlo simulator
# You may change the values of these constants as desired, but
#  do not change their names.
NTRIALS = 1000        # Number of trials to run
SCORE_CURRENT = 1.0 # Score for squares played by the current player
SCORE_OTHER = 1.0   # Score for squares played by the other player



# Add your functions here.

#For Square Method, 2 is PLAYERX and 3 is PLAYERO
#For Check_win() Method 4 is draw, 2 is PLAYERX and 3 is PLAYERO

def mc_trial(board, player):
    """
    Function for performing a trial for the monte carlo simulation.
    """
    while board.check_win() is None:
        row = random.randint(0, board.get_dim()-1)
        col = random.randint(0, board.get_dim()-1)
        if board.square(row, col) == provided.EMPTY:
            player = provided.switch_player(player)
            board.move(row, col, player)

    return None

def mc_update_scores(scores, board, player):
    """
    Updates the score in the score grid for a trial in the
    monte carlo simulation
    """

    game_outcome = board.check_win()

    if game_outcome == 4:
        return None
    elif game_outcome == 2 or game_outcome == 3:
        for row in range(board.get_dim()):
            for col in range(board.get_dim()):
                if game_outcome == 2 and board.square(row, col) == 2:
                    scores[row][col] += 1
                elif game_outcome == 3 and board.square(row, col) == 2:
                    scores[row][col] -= 1
                elif game_outcome == 2 and board.square(row, col) == 3:
                    scores[row][col] -= 1
                elif game_outcome == 3 and board.square(row, col) == 3:
                    scores[row][col] += 1

    return None

def get_best_move(board, scores):
    """
    Function uses the mc trail and score update functions
    to find the best move from the score total from all
    trials.
    """
    empty_squares = board.get_empty_squares()

    if empty_squares == []:
        return
    """
    Below creates a list of lists the size of the board that is all zeros
    where values of empty squares can be added
    """
    rows, cols = board.get_dim(), board.get_dim()
    empty_scores = [[0 for _ in range(cols)] for _ in range(rows)]

    """
    The below conditions create the empty_scores list of lists with 
    values in the empty spaces
    """
    if len(empty_squares) > 1:
        for index, square in enumerate(empty_squares):
            empty_scores[int(square[0])][int(square[1])] = scores[int(square[0])][int(square[1])]
    elif len(empty_squares) == 1:
        return empty_squares[0]

    """
    Below creates the list of empty value.
    """
    empty_score_values = []
    if len(empty_squares) > 1:
        for index, square in enumerate(empty_squares):
            empty_score_values.append(scores[int(square[0])][int(square[1])])
    """
    The below finds the max value of the empty squares using a list'''
    """
    max_score = 0
    if len(empty_squares) > 1:
        max_score = max(empty_score_values)
    else:
        return empty_squares[0]
    """    
    The below creates a matrix of tuples where the maximum value is
    located for empty spaces. A list of lists with values that include only
    maximum values is being used for the condition of creating the tuples.'''
    """
    max_empty_score_locations = []
    for row_index, row in enumerate(empty_scores):
        for col_index, score in enumerate(row):
            if score == max_score and (row_index, col_index) in empty_squares:
                max_empty_score_locations.append((row_index, col_index))

    if len(max_empty_score_locations) > 1:
        random_move_num = random.randint(0, len(max_empty_score_locations)-1)
        random_move = max_empty_score_locations[random_move_num]
        return random_move
    else:
        return max_empty_score_locations[0]


def mc_move(board, player, trials):
    """
    Uses the mc trial, update score, and find best move
    functions to determine the move the bot will play in
    the next move.
    """
    rows, cols = board.get_dim(), board.get_dim()
    scores = [[0 for _ in range(cols)] for _ in range(rows)]

    for games in range(trials):
        trial_board = board.clone()
        mc_trial(trial_board, player)
        mc_update_scores(scores, trial_board, player)
    best_move = get_best_move(board, scores)

    return best_move

# Test game with the console or the GUI.  Uncomment whichever
# you prefer.  Both should be commented out when you submit
# for testing to save time.

#provided.play_game(mc_move, NTRIALS, False)
#poc_ttt_gui.run_gui(3, provided.PLAYERX, mc_move, NTRIALS, False)


