from ChessAnalyzer import ChessAnalyzer
import chess
import chess.engine
import csv
import os

engine_path="fairy-stockfish_x86-64-bmi2.exe"

play_time = 0.1

def list_of_Chess960_fma(to_index):
    results = []
    for i in range(to_index):
        board960 = chess.Board(chess960=True)
        board960.set_chess960_pos(i)
        Analyzer = ChessAnalyzer(engine_path, board960)
        fma_evaluation = Analyzer.evaluate_fma()
        print(f"FMA of Variant: {i} calculated : {fma_evaluation}")

        results.append([i,fma_evaluation])
    return results
def write_to_csv(results,file_name):
    file_name += ".csv"
    with open(file_name, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Index', 'FMA Result'])  
        writer.writerows(results)

write_to_csv(list_of_Chess960_fma(3),"test1")