class Game:
    def __init__(self, title):
        self.title = title
        self._results = []
        self._players = []

    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self,title):
        if hasattr(self, 'title'):
            raise Exception
        else:
            if isinstance(title, str) and len(title) > 0:
                self._title = title
            else:
                raise Exception

    def results(self, new_result=None):
        from classes.result import Result
        if new_result and isinstance(new_result, Result):
            self._results.append(new_result)
        return self._results
    
    def players(self, new_player=None):
        from classes.player import Player
        if new_player and isinstance(new_player, Player):
            self._players.append(new_player)
        return self._players
    
    def average_score(self, player):
        player_results = []
        for each in self._results:
            if each.player == player:
                player_results.append(each.score)

        return sum(player_results) / len(player_results)
    
