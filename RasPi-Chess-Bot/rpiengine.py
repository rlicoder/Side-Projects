import chess
import chess.engine

def getMove(FEN, limit):
    engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")

    board = chess.Board(FEN)
    result = engine.play(board, chess.engine.Limit(time=limit))
    board.push(result.move)

    engine.quit()

    return result.move

