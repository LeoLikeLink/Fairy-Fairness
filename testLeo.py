import chess
import chess.engine
import chess.variant
import copy

engine_path = "fairy-stockfish_x86-64-bmi2.exe"


def evaluate_fma(board, depth, time):
    with chess.engine.SimpleEngine.popen_uci(engine_path) as engine:
        result = engine.analyse(board, chess.engine.Limit(time=time,depth=depth))
        return result['score'].relative

def evaluate_score(board: chess.Board, depth, time):
    with chess.engine.SimpleEngine.popen_uci(engine_path) as engine:
        result = engine.analyse(board, chess.engine.Limit(time=time,depth=depth))
        print(result['score'])
        print(board.result())
        
    
    
def engine_play(board: chess.Board,time):
    with chess.engine.SimpleEngine.popen_uci(engine_path) as engine:
        copy_board = copy.deepcopy(board)

        while not copy_board.is_game_over():
            result = engine.play(copy_board, chess.engine.Limit(time=time))
            copy_board.push(result.move)
        engine.quit()
    return copy_board


    
#Example Chess960
classicboard = chess.Board()

# Transposed Pieces
# index= 524
# board960 = chess.Board(chess960=True)
# board960.set_chess960_pos(index)

# Example Atomic
boardatomic = chess.variant.AtomicBoard()

# Example Antichess

boardanti = chess.variant.AntichessBoard()

time = 0.1
depth = 20

evaluate_score(engine_play(classicboard,0.1),time,depth)

# print(evaluate_board(boardatomic,depth,time))




