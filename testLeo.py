import chess
import chess.engine

engine_path = "fairy-stockfish_x86-64-bmi2.exe"


def evaluate_board(board, depth, time):
    with chess.engine.SimpleEngine.popen_uci(engine_path) as engine:
        result = engine.analyse(board, chess.engine.Limit(time=time,depth=depth))
        return result['score'].relative
    
board = chess.Board() 
time = 20
depth = 20
print(evaluate_board(board,depth,time))



