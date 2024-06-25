from ChessAnalyzer import ChessAnalyzer
import chess
import chess.engine
import csv
import pandas as pd
import os

engine_path="fairy-stockfish_x86-64-bmi2.exe"

play_time = 0.1

def list_of_Chess960_fma(to_index):
    results = []
    for i in range(to_index):
        board960 = chess.Board(chess960=True)
        board960.set_chess960_pos(i)
        Analyzer = ChessAnalyzer(engine_path, board960,10)
        fma_evaluation = Analyzer.evaluate_fma()
        print(f"FMA of Variant: {i} calculated : {fma_evaluation}")

        results.append([i,fma_evaluation])
    return results

def list_of_fen_position_fma(fen_list):
    results = []
    i = 0

    for fen_postion in fen_list:
        
        board = chess.Board()
        board.set_board_fen(fen_postion)
        Analyzer = ChessAnalyzer(engine_path, board)
        fma_evaluation = Analyzer.evaluate_fma()
        print(f"FMA of Position: {fen_postion} calculated : {fma_evaluation}")

        results.append([i,fma_evaluation])
        i =+1
    return results

def write_to_csv(results,file_name):
    file_name += ".csv"
    df = pd.DataFrame(results, columns=['Index', 'FMA Result'])
    df.to_csv(file_name,index=False)
    print(f"Data successfully written to '{file_name}'")

def import_list_of_fen_from_csv(file_name):
    result = []
    try:
        df = pd.read_csv(file_name,header=None)
        for row in df.iterrows():
            result.append(row[1])
        return result
    except FileNotFoundError:
        print(f"Error: File '{file_name}' not found.")
        return None
    except pd.errors.EmptyDataError:
        print(f"Error: File '{file_name}' is empty.")
        return None
    except pd.errors.ParserError as pe:
        print(f"Error parsing CSV: {pe}")
        return None

        

# board_custom = chess.Board()
# board_custom.set_board_fen("rnbqkbnr/8/pppppppp/8/8/PPPPPPPP/8/RNBQKBNR")

# Analyzer = ChessAnalyzer(engine_path,board_custom,20)
results = list_of_fen_position_fma(import_list_of_fen_from_csv("FENList.csv"))

write_to_csv(results,"test1")