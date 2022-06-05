class Track:
    def __init__(self, size, players) -> None:
        self.size = size
        self.players = players
        self.scores = [0 for _ in players]

    def move(self, player, dice):
        new_pos = (self.players[player] + sum(dice) - 1) % self.size + 1
        
        self.players[player] = new_pos
        self.scores[player] += new_pos

    def hasWon(self, target=1000):
        return max(self.scores) >= target


    def get2nd(self):
        temp = [score for score in self.scores]
        temp.sort()

        return temp[-2]