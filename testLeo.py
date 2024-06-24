import chess
import chess.engine

engine_path = "fairy-stockfish_x86-64-bmi2.exe"


def evaluate_board(board: chess.Board):
    with chess.engine.SimpleEngine.popen_uci(engine_path) as engine:
        result = engine.analyse(board, chess.engine.Limit(time=0.1))
        return result['score'].relative
    
board = chess.Board() 
print(evaluate_board(board))




