import requests
from bs4 import BeautifulSoup
from settings import URL


class PageParser:
    """
    Module responsible for parsing page
    """

    def __init__(self):
        self.page = BeautifulSoup(requests.get(URL).text, "html.parser")
        self.stats = []
        self._create_teams_stats_list()
        print(self.stats)

    def _get_score_table(self) -> list:
        score_table = self.page.find_all('table')[1].find_all('table')[1].find_all('tr')[4:20]
        return score_table

    def _get_team_stats(self, team: str) -> list:
        team = team.split('\n')
        team_stats = []
        position = team[1].split('.')[0][7:]
        name = team[2].split(';')[1][13:-9]
        points = team[4].split('</b>')[0][7:]
        team_stats.append(position)
        team_stats.append(name)
        team_stats.append(points)

        self.stats.append(team_stats)

    def _create_teams_stats_list(self) -> list:
        score_table = self._get_score_table()
        for team in score_table:
            self._get_team_stats(str(team))

