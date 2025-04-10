class TennisGame1:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1points += 1
        else:
            self.p2points += 1

    def result_points_more_than_four(self):
        minus_result = self.p1points - self.p2points

        if minus_result == 1:
            return f"Advantage {self.player1_name}"
        
        if minus_result == -1:
            return f"Advantage {self.player2_name}"
        
        if minus_result >= 2:
            return f"Win for {self.player1_name}"
        
        return f"Win for {self.player2_name}"
    
    def result_points_inequal_less_than_four(self):
        result = ""
        for i in range(1, 3):
            if i != 1:
                result += "-"
            result += {
                0: "Love",
                1: "Fifteen",
                2: "Thirty",
                3: "Forty",
            }[self.p1points if i == 1 else self.p2points]
        return result

    def score(self):
        if self.p1points == self.p2points:
            return {
                0: "Love-All",
                1: "Fifteen-All",
                2: "Thirty-All",
            }.get(self.p1points, "Deuce")

        if self.p1points >= 4 or self.p2points >= 4:
            return self.result_points_more_than_four()

        return self.result_points_inequal_less_than_four()
