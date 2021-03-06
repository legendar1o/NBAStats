class NBATeams:
    def __init__(self, server):
        self.teams = server.get_teams()

    def get_team(self, name):
        if type(name) is int:
            for item in self.teams:
                if item['teamId'] == str(name):
                    return item
            else:
                raise NameError("Wrong team ID\n")
        if len(name) == 3:
            for item in self.teams:
                if item['tricode'] == name:
                    return item
            else:
                raise NameError("Wrong team Tricode\n")
        else:
            for item in self.teams:
                if item['fullName'] == name:
                    return item
            else:
                raise NameError("Wrong team FullName\n")

    def get_team_tricode_from_id(self, team_id):
        if type(team_id) is int:
            for item in self.teams:
                if int(item['teamId']) == team_id:
                    return item['tricode']
            else:
                raise NameError("Wrong team ID\n")
        else:
            raise AttributeError("ID has to be int\n")
