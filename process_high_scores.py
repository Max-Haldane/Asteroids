
class ProcessHighScores():

    def __init__(self, high_scores_file: list) -> None:
        self.high_scores_file = high_scores_file
    
    def read(self):
        try:
            with open(self.high_scores_file, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return f"Error: the file '{self.high_scores_file}' does not exist"

    
    def update(self, game_score):
        high_scores = []
        for score in self.read().split(','):
            if score != '':
                high_scores.append(int(score))
        high_scores.append(game_score.score)
        high_scores.sort(reverse = True)
        if len(high_scores) >= 10:
            high_scores = high_scores[:10]
        high_score_string = ','.join(str(score) for score in high_scores)
        with open(self.high_scores_file, 'w') as file:
            file.write(high_score_string)
        return high_scores
    
    def high_score(self):
        high_score = self.read()[0]
        return high_score