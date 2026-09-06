
class ProcessHighScores():

    def __init__(self, high_scores: list) -> None:
        self.high_scores = high_scores
    
    def update(self, game_score):
        self.high_scores.append(game_score.score)
        self.high_scores.sort(reverse = True)
        if len(self.high_scores) >= 10:
            self.high_scores = self.high_scores[:9]
        print(self.high_scores)
    
    def high_score(self):
        return self.high_scores[0]