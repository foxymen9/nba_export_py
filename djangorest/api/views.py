from datetime import datetime
from django.conf import settings
from rest_framework import generics
from rest_framework.response import Response
from nba_py import team, league
from . import helpers

OUT_DIR = settings.BASE_DIR + '/../files'

class NBAStatsView(generics.ListAPIView):

  def list(self, request):
    teamGeneral = TeamGeneral();
    teamClutch = TeamClutch();
    teamPlaytype = TeamPlaytype();
    teamTracking = TeamTracking();
    teamDefenseDashboard = TeamDefenseDashboard();

    # teamGeneral.create_files();
    # teamClutch.create_files();
    # teamPlaytype.create_files();
    # teamTracking.create_files();
    teamDefenseDashboard.create_files();

    return Response("OK", 200)

class TeamGeneral():

  def create_file(self, measure_type, last_game):
    now = datetime.now()
    date = now.strftime("%m-%d-%Y")
    time = now.strftime("%m-%d-%Y-%H-%M-%S")
    
    file_name = 'team_general_' + measure_type['key'] + '_' + last_game['name']
    path_latest = OUT_DIR + '/stats/nba/' + date + '/latest/'
    path_archived = OUT_DIR + '/stats/nba/' + date + '/archived/' + time + '/'

    helpers.create_folder(path_latest)
    helpers.create_folder(path_archived)

    stats = league.TeamStats(measure_type=measure_type['name'], last_n_games=last_game['value'])
    df = stats.overall()
    df.to_csv(path_latest + file_name + '.csv', encoding='utf-8')
    df.to_json(path_latest + file_name + '.json', orient='records')
    df.to_csv(path_archived + file_name + '.csv', encoding='utf-8')
    df.to_json(path_archived + file_name + '.json', orient='records')

  def create_files(self):
    measure_types = helpers.get_measure_types('team', 'General')
    last_games = helpers.get_last_games('team', 'General')

    for measure_type in measure_types:
      for last_game in last_games:
        self.create_file(measure_type, last_game)

class TeamClutch():

  def create_file(self, measure_type, last_game):
    now = datetime.now()
    date = now.strftime("%m-%d-%Y")
    time = now.strftime("%m-%d-%Y-%H-%M-%S")
    
    file_name = 'team_clutch_' + measure_type['key'] + '_' + last_game['name']
    path_latest = OUT_DIR + '/stats/nba/' + date + '/latest/'
    path_archived = OUT_DIR + '/stats/nba/' + date + '/archived/' + time + '/'

    helpers.create_folder(path_latest)
    helpers.create_folder(path_archived)

    stats = league.TeamClutch(measure_type=measure_type['name'], last_n_games=last_game['value'])
    df = stats.overall()
    df.to_csv(path_latest + file_name + '.csv', encoding='utf-8')
    df.to_json(path_latest + file_name + '.json', orient='records')
    df.to_csv(path_archived + file_name + '.csv', encoding='utf-8')
    df.to_json(path_archived + file_name + '.json', orient='records')

  def create_files(self):
    measure_types = helpers.get_measure_types('team', 'Clutch')
    last_games = helpers.get_last_games('team', 'Clutch')

    for measure_type in measure_types:
      for last_game in last_games:
        self.create_file(measure_type, last_game)

class TeamPlaytype():

  def create_file(self, measure_type):
    now = datetime.now()
    date = now.strftime("%m-%d-%Y")
    time = now.strftime("%m-%d-%Y-%H-%M-%S")
    
    file_name = 'team_playtype_' + measure_type['key']
    path_latest = OUT_DIR + '/stats/nba/' + date + '/latest/'
    path_archived = OUT_DIR + '/stats/nba/' + date + '/archived/' + time + '/'

    helpers.create_folder(path_latest)
    helpers.create_folder(path_archived)

    stats = league.TeamPlaytype(category=measure_type['name'], season=now.year)
    df = stats.overall()
    df.to_csv(path_latest + file_name + '.csv', encoding='utf-8')
    df.to_json(path_latest + file_name + '.json', orient='records')
    df.to_csv(path_archived + file_name + '.csv', encoding='utf-8')
    df.to_json(path_archived + file_name + '.json', orient='records')

  def create_files(self):
    measure_types = helpers.get_measure_types('team', 'Playtype')

    for measure_type in measure_types:
      self.create_file(measure_type)

class TeamTracking():
  
  def create_file(self, measure_type, last_game):
    now = datetime.now()
    date = now.strftime("%m-%d-%Y")
    time = now.strftime("%m-%d-%Y-%H-%M-%S")
    
    file_name = 'team_tracking_' + measure_type['key'] + '_' + last_game['name']
    path_latest = OUT_DIR + '/stats/nba/' + date + '/latest/'
    path_archived = OUT_DIR + '/stats/nba/' + date + '/archived/' + time + '/'

    helpers.create_folder(path_latest)
    helpers.create_folder(path_archived)

    stats = league._PlayerTrackingStats(player_or_team='Team', pt_measure_type=measure_type['name'], last_n_games=last_game['value'])
    df = stats.overall()
    df.to_csv(path_latest + file_name + '.csv', encoding='utf-8')
    df.to_json(path_latest + file_name + '.json', orient='records')
    df.to_csv(path_archived + file_name + '.csv', encoding='utf-8')
    df.to_json(path_archived + file_name + '.json', orient='records')

  def create_files(self):
    measure_types = helpers.get_measure_types('team', 'Tracking')
    last_games = helpers.get_last_games('team', 'Tracking')

    for measure_type in measure_types:
      for last_game in last_games:
        self.create_file(measure_type, last_game)

class TeamDefenseDashboard():
  
  def create_file(self, measure_type, last_game):
    now = datetime.now()
    date = now.strftime("%m-%d-%Y")
    time = now.strftime("%m-%d-%Y-%H-%M-%S")
    
    file_name = 'team_defensedashboard_' + measure_type['key'] + '_' + last_game['name']
    path_latest = OUT_DIR + '/stats/nba/' + date + '/latest/'
    path_archived = OUT_DIR + '/stats/nba/' + date + '/archived/' + time + '/'

    helpers.create_folder(path_latest)
    helpers.create_folder(path_archived)

    stats = league.TeamDefenseDashboard(defense_category=measure_type['name'], last_n_games=last_game['value'])
    df = stats.overall()
    df.to_csv(path_latest + file_name + '.csv', encoding='utf-8')
    df.to_json(path_latest + file_name + '.json', orient='records')
    df.to_csv(path_archived + file_name + '.csv', encoding='utf-8')
    df.to_json(path_archived + file_name + '.json', orient='records')

  def create_files(self):
    measure_types = helpers.get_measure_types('team', 'DefenseDashboard')
    last_games = helpers.get_last_games('team', 'DefenseDashboard')

    for measure_type in measure_types:
      for last_game in last_games:
        self.create_file(measure_type, last_game)
