import os
import pickle

from main import PlayerScore


SCORES_FILE = 'scores.scr'
class ScoreBoard:

    def add_results(self, score: PlayerScore) -> None:
        '''
        Adding scores
        '''
        
        if os.path.isfile(SCORES_FILE):
            player_scores = []
            with open(SCORES_FILE, mode='rb') as file:
                while True:
                    try:
                        player: PlayerScore = pickle.load(file)
                        player_scores.append(player)
                    except EOFError:
                        break
            
            for player in player_scores:
                if player.name == score.name:
                    player.total_games += score.total_games
                    player.total_wins += score.total_wins
                    player.total_loss += score.total_loss
                    break
        else:
            player_scores = [score]
        with open(SCORES_FILE, mode='wb') as file:
            for player in player_scores:
                pickle.dump(player, file)
                
    def display_scoreboard(self):
        pass
