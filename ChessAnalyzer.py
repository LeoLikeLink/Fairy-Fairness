import chess
import chess.engine
import chess.variant
import copy

class ChessAnalyzer:
    def __init__(self, engine_path,board: chess.Board,play_time,depth):
        self.engine_path = engine_path
        self.board = copy.deepcopy(board)
        self.play_time = play_time
        self.depth = depth
        self.engine = chess.engine.SimpleEngine.popen_uci(engine_path)
    
    def evaluate_fma(self):
        with chess.engine.SimpleEngine.popen_uci(self.engine_path) as engine:
            result = engine.analyse(self.board, chess.engine.Limit(depth=self.depth))
            return result['score'].relative

    def evaluate_score(self):
        return self.board.result()
        
    def engine_play(self):
        with chess.engine.SimpleEngine.popen_uci(self.engine_path) as engine:

            while not self.board.is_game_over():
                result = engine.play(self.board, chess.engine.Limit(time=self.play_time))
                self.board.push(result.move)
                
                
            engine.quit()
            print("Game Finished")



