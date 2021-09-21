from page_parser import PageParser
from settings import TEAM_NAME


class TeamInfo(PageParser):

    def __init__(self):
        super().__init__()
        self._index = self._get_team_index()
        print(self._index)

    def _get_team_index(self) -> int:
        for team in self.stats:
            if team[1] == TEAM_NAME:
                return self.stats.index(team)

    def create_small_table(self) -> list:
        if self._index in [0, 1, 2]:
            return [self.stats[x] for x in range(5)]
        elif self._index in [len(self.stats) - 1, len(self.stats) - 2, len(self.stats) - 3]:
            return [self.stats[self._index - x] for x in range(4, -1, -1)]
        else:
            return [self.stats[self._index - x] for x in range(2, -3, -1)]
