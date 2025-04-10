class TennisGame2:
    def __init__(self, player1_name, player2_name):
        self.player1_name = player1_name
        self.player2_name = player2_name
        self.p1points = 0
        self.p2points = 0

    def won_point(self, player_name):
        if player_name == self.player1_name:
            self.p1_score()
        else:
            self.p2_score()

    def result_points_equal(self, result):
        if self.p1points > 2:
            return "Deuce"

        if self.p1points < 3:
            match self.p1points:
                case 0:
                    result = "Love"
                case 1:
                    result = "Fifteen"
                case 2:
                    result = "Thirty"
            result += "-All"

        return result
    
    def res23_less_4(self, points, res):
        if points == 2:
            return "Thirty"
        if points == 3:
            return "Forty"
        return res
    
    def res12_less_4(self, points, res):
        if points == 1:
            return "Fifteen" 
        if points == 2:
            return "Thirty"
        return res

    
    def result_p1_more_p2(self, p1res, p2res):
        if self.p2points >= 3:
            return f"Advantage {self.player1_name}"
        
        if self.p1points < 4:
            p1res = self.res23_less_4(self.p1points, p1res)
            p2res = self.res12_less_4(self.p2points, p2res)
            return p1res + "-" + p2res

        
    def result_p2_more_p1(self, p1res, p2res):
        if self.p1points >= 3:
            return f"Advantage {self.player2_name}"
        
        if self.p2points < 4:
            p2res = self.res23_less_4(self.p2points, p2res)
            p1res = self.res12_less_4(self.p1points, p1res)
            return p1res + "-" + p2res

        
    def score(self):
        if (
            self.p1points >= 4
            and (self.p1points - self.p2points) >= 2
        ):
            return "Win for player1"
        if (
            self.p2points >= 4
            and (self.p2points - self.p1points) >= 2
        ):
            return "Win for player2"

        result = ""
        if self.p1points == self.p2points:
            result = self.result_points_equal(result)

        p1res = ""
        p2res = ""
        if self.p1points > 0 and self.p2points == 0:
            match self.p1points:
                case 1:
                    p1res = "Fifteen"
                case 2:
                    p1res = "Thirty"
                case 3:
                    p1res = "Forty"
            p2res = "Love"
            result = p1res + "-" + p2res

        elif self.p2points > 0 and self.p1points == 0:
            match self.p2points:
                case 1:
                    p2res = "Fifteen"
                case 2:
                    p2res = "Thirty"
                case 3:
                    p2res = "Forty"
            p1res = "Love"
            result = p1res + "-" + p2res

        if self.p1points > self.p2points:
            result = self.result_p1_more_p2(p1res, p2res)

        elif self.p2points > self.p1points:
            result = self.result_p2_more_p1(p1res, p2res)           
        
        return result

    def set_p1_score(self, number):
        for i in range(number):
            self.p1_score()

    def set_p2_score(self, number):
        for i in range(number):
            self.p2_score()

    def p1_score(self):
        self.p1points += 1

    def p2_score(self):
        self.p2points += 1
