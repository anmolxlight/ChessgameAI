import random
from math import inf
from piece import *


def random_move(board):
    """
    Selects a random move from the valid moves for the current players turn
    :param board: the current board being used for the game (Board)
    :return: tuple representing move; format: ((sourceX, sourceY), (destX, destY))
    """
    moves = board.get_moves()
    if moves:
        return random.choice(moves)


def evaluate(board, maximizing_color):
    """
    Provides a number representing the value of the board at a given state
    :param board: the current board being used for the game (Board)
    :param maximizing_color: color associated with maximizing player (tuple)
    :return: integer representing boards value
    """
    score = 0
    # Piece values: pawn=1, knight/bishop=3, rook=5, queen=9
    piece_values = {Pawn: 1, Knight: 3, Bishop: 3, Rook: 5, Queen: 9, King: 0}
    
    for row in range(8):
        for col in range(8):
            piece = board.tilemap[col][row].piece
            if piece:
                # Get the value of the piece
                value = piece_values[type(piece)]
                # Add value if piece belongs to maximizing player, subtract if opponent's
                if piece.color == maximizing_color:
                    score += value
                else:
                    score -= value
    
    return score


def minimax(board, depth, alpha, beta, maximizing_player, maximizing_color):
    """
    Minimax algorithm used to find best move for the AI
    :param board: the current board being used for the game (Board)
    :param depth: controls how deep to search the tree of possible moves (int)
    :param alpha: the best value that the maximizer currently can guarantee at that level or above (int)
    :param beta: the best value that the minimizer currently can guarantee at that level or above (int)
    :param maximizing_player: True if current player is maximizing player (bool)
    :param maximizing_color: color of the AI using this function to determine a move (tuple)
    :return: tuple representing move and eval; format: (move, eval)
    """
    # Base case: if depth is 0
    if depth == 0:
        return None, evaluate(board, maximizing_color)
    
    moves = board.get_moves()
    if not moves:  # If no moves available
        return None, evaluate(board, maximizing_color)
    
    best_move = None
    
    if maximizing_player:
        max_eval = -inf
        for move in moves:
            # Make move (unpack the source and destination from move tuple)
            source, dest = move
            board.make_move(source, dest)
            # Recursive call
            current_eval = minimax(board, depth - 1, alpha, beta, False, maximizing_color)[1]
            # Undo move
            board.unmake_move()
            
            if current_eval > max_eval:
                max_eval = current_eval
                best_move = move
            
            alpha = max(alpha, current_eval)
            if beta <= alpha:
                break
        
        return best_move, max_eval
    
    else:  # Minimizing player
        min_eval = inf
        for move in moves:
            # Make move (unpack the source and destination from move tuple)
            source, dest = move
            board.make_move(source, dest)
            # Recursive call
            current_eval = minimax(board, depth - 1, alpha, beta, True, maximizing_color)[1]
            # Undo move
            board.unmake_move()
            
            if current_eval < min_eval:
                min_eval = current_eval
                best_move = move
            
            beta = min(beta, current_eval)
            if beta <= alpha:
                break
        
        return best_move, min_eval
