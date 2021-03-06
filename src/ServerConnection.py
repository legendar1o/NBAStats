import datetime
import json
from pprint import pprint

import requests
from NoDataFoundError import NoDataFoundError


class ServerConnection:
    def __init__(self, server_name, date):
        self.server_name = server_name
        self.date = date
        self.teams_link = "/{}/teams.json".format(self.date.year)
        self.scoreboard_link = "/{}{:02d}{:02d}/scoreboard.json".format(self.date.year, self.date.month,
                                                                        self.date.day)
        self.all_standings_link = "/{}{:02d}{:02d}/standings_all.json".format(self.date.year, self.date.month,
                                                                              self.date.day)
        self.conference_standings_link = "/{}{:02d}{:02d}/standings_conference.json".format(self.date.year,
                                                                                            self.date.month,
                                                                                            self.date.day)
        self.players_link = "/{}/players.json".format(self.date.year)

    @staticmethod
    def get_web_source(link):
        try:
            return requests.get(link).content
        except requests.exceptions.ConnectionError:
            raise ConnectionError

    @staticmethod
    def get_data(web_source):
        try:
            data = json.loads(web_source)
            return data
        except json.decoder.JSONDecodeError:
            raise NoDataFoundError

    def get_teams(self):
        return self.get_data(self.get_web_source(self.server_name + self.teams_link))['league']['standard']

    def get_daily_scores(self):
        return self.get_data(self.get_web_source(self.server_name + self.scoreboard_link))['games']

    def get_all_standings(self):
        return self.get_data(self.get_web_source(self.server_name + self.all_standings_link))['league']['standard'][
            'teams']

    def get_western_standings(self):
        return \
            self.get_data(self.get_web_source(self.server_name + self.conference_standings_link))['league']['standard'][
                'conference'][
                'west']

    def get_eastern_standings(self):
        return \
            self.get_data(self.get_web_source(self.server_name + self.conference_standings_link))['league']['standard'][
                'conference'][
                'east']

    def get_players_list(self):
        return self.get_data(self.get_web_source(self.server_name + self.players_link))['league']['standard']

    def get_player_stats(self, player_id):
        return \
            self.get_data(self.get_web_source(
                self.server_name + "/{}/players/{}_profile.json".format(self.date.year, player_id)))['league'][
                'standard']

    def get_date(self):
        return self.date


server_name = "http://data.nba.net/data/10s/prod/v1"
date = datetime.date(2017, 12, 12)
serv = ServerConnection(server_name, date)
print(serv.get_web_source(serv.server_name + serv.teams_link))
#print(serv.get_data(serv.get_web_source(serv.server_name + serv.teams_link)))
