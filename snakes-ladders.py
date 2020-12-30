class SnakesLadders():

    def __init__(self):
        self.p1_square = 0
        self.p2_square = 0
        self.player_turn = 1
        self.gameover = False
        self.ladders_dict = {2:38, 7:14, 8:31, 15:26, 21:42, 28:84, 36:44, 51:67, 71:91, 78:98, 87:94}
        self.snakes_dict = {16:6, 46:25, 49:11, 62:19, 64:60, 74:53, 89:68, 92:88, 95:75, 99:80}

    
    
    
    def play(self, die1, die2):
        self.die1 = die1
        self.die2 = die2
        self.current_turn = 1 if self.player_turn == 1 else 2
        self.same_dice = self.die1 == self.die2
        self.roll = die1 + die2
        current_player = self.current_turn
        
        def get_new_position(roll):
            previous_square = self.p1_square if self.player_turn == 1 else self.p2_square
            return previous_square + roll
        
        def update_square(new_position, current_player):
            current_player = self.current_turn
            if current_player == 1:
                self.p1_square = new_position
            elif current_player == 2:
                self.p2_square = new_position
        
        def switch_player():
            if self.current_turn == 1:
                self.player_turn = 2
            else:
                self.player_turn = 1
                
        def winner():
            winner = self.current_turn
            self.gameover = True
            return (f'Player {winner} Wins!')
            

        def show_square(current_player):
            return self.p1_square if self.current_turn == 1 else self.p2_square
        
        if not self.gameover:
            new_position = get_new_position(self.roll)
            update_square(new_position, current_player)

            if new_position == 100:
                return winner()

            if new_position > 100:
                new_position = 100 - (new_position - 100)
                print(f'You passed 100! Your new position is {new_position}')
                update_square(new_position, current_player)

            if new_position in self.ladders_dict:
                print(f'You hit a ladder at position {new_position}')
                new_position = self.ladders_dict[new_position]
                print(f'Player {self.current_turn}, your new position is: {new_position}')
                update_square(new_position, current_player)

            elif new_position in self.snakes_dict:
                print(f'You hit a snake at position {new_position}')
                new_position = self.snakes_dict[new_position]
                print(f'Player {self.current_turn}, your new position is {new_position}')
                update_square(new_position, current_player)

            else:
                update_square(new_position, current_player)

            if not self.same_dice:
                switch_player()

            return f'Player {self.current_turn} is on square {show_square(self.current_turn)}'
        else:
            return 'Game over!'