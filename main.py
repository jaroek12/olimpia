import requests
from bs4 import BeautifulSoup

# page = "http://www.90minut.pl/liga/1/liga11907.html"
# # tr 17 poczatek tabeli
# download_html = requests.get(page)
# soup = BeautifulSoup(download_html.text, "html.parser") #Parsowanie strony
# tab = soup.find_all('table')[1].find_all('table')[1].find_all('tr')[4:20]
# nazwa = (str(tab[0])).split('\n')[2] # tabela
# print(tab[0])

# def get_team_name(tab):
#     for team in tab:
#         print((str(team)).split('\n')[2].split(';')[1][13:-9])
#
# get_team_name(tab)

# from page_parser import PageParser
#
# parser = PageParser()
# print(parser.stats)

from team_info import TeamInfo

ti = TeamInfo()
print(ti.create_small_table())