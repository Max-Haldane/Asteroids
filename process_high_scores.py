import pygame
from constants import *

class ProcessHighScores():

    def __init__(self, high_scores_file: list, screen) -> None:
        self.high_scores_file = high_scores_file
        self.screen = screen
        self.font = pygame.font.Font(None, 36)
    
    def read_file(self):
        try:
            with open(self.high_scores_file, 'r') as file:
                return file.read()
        except FileNotFoundError:
            return f"Error: the file '{self.high_scores_file}' does not exist"

    def file_to_list(self) -> list:
        high_scores = []
        for score in self.read_file().split(','):
            if score != '' and score != None:
                high_scores.append(int(score))
        return high_scores
    
    def update(self, game_score):
        high_scores = self.file_to_list()
        high_scores.append(game_score.score)
        high_scores.sort(reverse = True)
        if len(high_scores) >= 10:
            high_scores = high_scores[:10]
        return high_scores
    
    def write(self, game_score):
        high_scores = self.update(game_score)
        high_score_string = ','.join(str(score) for score in high_scores)
        with open(self.high_scores_file, 'w') as file:
            file.write(high_score_string)


    def draw(self):
        high_scores = self.file_to_list()
        for i in range(len(high_scores)):
            score_index_text = self.font.render(f"{i + 1}:", True, "white")
            score_text = self.font.render(f"{high_scores[i]}", True, "white")
            score_index_rect = score_text.get_rect(topleft=(SCREEN_WIDTH / 2 - 80, SCREEN_HEIGHT / 2 + 50 + 25 * (i + 1)))
            score_rect = score_text.get_rect(topleft=(SCREEN_WIDTH / 2 + 80, SCREEN_HEIGHT / 2 + 50 + 25 * (i + 1)))
            self.screen.blit(score_index_text, score_index_rect)
            self.screen.blit(score_text, score_rect)