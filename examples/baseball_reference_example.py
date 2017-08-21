from web_crawler import WebCrawler 
from soup_request import SoupRequestHandler

class BaseballReferenceCrawler(WebCrawler):

    def __init__(self):
        self.handler = SoupRequestHandler(self)
        self.url = ""

        self.headers = {
          'USER-AGENT': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_0) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/49.0.2623.110 Safari/537.36',
        }
    
    def parse(self, soup):
        main_div = soup.find('div', class_='div_standings_NL')
        nl_east_table = main_div.find_all('table')[1]
        rows = nl_east_table.find_all('tr')
        # Skip the header row
        rows = rows[1:]

        teams = []

        for row in player_rows:
            name = None
            wins = None
            loses = None

            for col in row.find_all('td'):
                if index == 1:
                    name = col.text
                if index == 2:
                    wins = col.text
                if index == 9:
                    loses = col.text
                index = index+1

            team = {
                'name': name,
                'wins': wins,
                'loses': loses,
            }

            teams.append(team)
        return teams
