import chess
import chess.engine

def getMove(FEN):
    engine = chess.engine.SimpleEngine.popen_uci("/usr/games/stockfish")

    board = chess.Board(FEN)
    result = engine.play(board, chess.engine.Limit(time=0.1))
    board.push(result.move)

    engine.quit()

    return result.move

