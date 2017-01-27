import chess, chess.uci

class Simulation:
    def __init__(self, engine, start_position_id, time_limit, time_increment):
        self.engine = engine
        self.engine.uci()
        self.engine.setoption({"UCI_Chess960": True})

        #info_handler is used to obtain how long the engine spent thinking
        self.info_handler = chess.uci.InfoHandler()
        self.engine.info_handlers.append(self.info_handler)

        self.board = chess.Board.from_chess960_pos(start_position_id)

        #the number of milliseconds that each player is allotted at the start of the game
        self.white_time = time_limit
        self.black_time = time_limit

        #the number of milliseconds added to a player's remaining time after making a move
        self.time_increment = time_increment

    def get_move(self): #gets the best move in the position according to the engine
        self.engine.position(self.board)

        return self.engine.go(
            wtime=self.white_time,
            btime=self.black_time,
            winc=self.time_increment,
            binc=self.time_increment).bestmove

    def run(self): #plays out the game until the finish
        while not self.board.is_game_over(True):
            move = self.get_move()

            time_change = self.time_increment - self.info_handler.info["time"] #how much to add to the player making the move's time
            if self.board.turn == chess.WHITE:
                self.white_time += time_change
            else:
                self.black_time += time_change

            self.board.push(move)