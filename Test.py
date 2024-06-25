from ChessAnalyzer import ChessAnalyzer
import chess
import chess.engine

engine_path="fairy-stockfish_x86-64-bmi2.exe"

index= 524
time = 0.1
depth = 20
board960 = chess.Board(chess960=True)
board960.set_chess960_pos(index)

Analyzer1 =  ChessAnalyzer(engine_path,board960,time,depth)
print(Analyzer1.evaluate_fma())
# fma_array = []

# fma_array.append(Analyzer1)
# print(fma_array[0])