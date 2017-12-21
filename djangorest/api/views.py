from datetime import datetime
from django.conf import settings
from rest_framework import generics
from rest_framework.response import Response
from nba_py import team, league
from . import helpers

OUT_DIR = settings.BASE_DIR + '/../files'

class NBAStatsView(generics.ListAPIView):

  def list(self, request):
    teamGeneral = TeamGeneral()
    teamClutch = TeamClutch()
    teamPlaytype = TeamPlaytype()
    teamTracking = TeamTracking()
    teamDefenseDashboard = TeamDefenseDashboard()
    teamShotDashboard = TeamShotDashboard()
    boxScores = BoxScores()
    teamAdvancedBoxScores = TeamAdvancedBoxScores()
    teamShooting = TeamShooting()
    teamOpponentShooting = TeamOpponentShooting()

    # teamGeneral.create_files()
    # teamClutch.create_files()
    # teamPlaytype.create_files()
    # teamTracking.create_files()
    # teamDefenseDashboard.create_files()
    # teamShotDashboard.create_files()
    # boxScores.create_files()
    # teamAdvancedBoxScores.create_files()
    teamShooting.create_files()
    teamOpponentShooting.create_files()

    return Response("OK", 200)

class TeamGeneral():

  def create_file(self, category, last_game):
    now = datetime.now()
    date = now.strftime("%m-%d-%Y")
    time = now.strftime("%m-%d-%Y-%H-%M-%S")
    
    file_name = 'team_general_' + category['key'] + '_' + last_game['name']
    path_latest = OUT_DIR + '/stats/nba/' + date + '/latest/'
    path_archived = OUT_DIR + '/stats/nba/' + date + '/archived/' + time + '/'

    helpers.create_folder(path_latest)
    helpers.create_folder(path_archived)

    stats = league.TeamStats(measure_type=category['name'], last_n_games=last_game['value'])
    df = stats.overall()
    df.to_csv(path_latest + file_name + '.csv', encoding='utf-8')
    df.to_json(path_latest + file_name + '.json', orient='records')
    df.to_csv(path_archived + file_name + '.csv', encoding='utf-8')
    df.to_json(path_archived + file_name + '.json', orient='records')

  def create_files(self):
    categories = helpers.get_categories('team', 'General')
    last_games = helpers.get_last_games('team', 'General')

    for category in categories:
      for last_game in last_games:
        self.create_file(category, last_game)

class TeamClutch():

  def create_file(self, category, last_game):
    now = datetime.now()
    date = now.strftime("%m-%d-%Y")
    time = now.strftime("%m-%d-%Y-%H-%M-%S")
    
    file_name = 'team_clutch_' + category['key'] + '_' + last_game['name']
    path_latest = OUT_DIR + '/stats/nba/' + date + '/latest/'
    path_archived = OUT_DIR + '/stats/nba/' + date + '/archived/' + time + '/'

    helpers.create_folder(path_latest)
    helpers.create_folder(path_archived)

    stats = league.TeamClutch(measure_type=category['name'], last_n_games=last_game['value'])
    df = stats.overall()
    df.to_csv(path_latest + file_name + '.csv', encoding='utf-8')
    df.to_json(path_latest + file_name + '.json', orient='records')
    df.to_csv(path_archived + file_name + '.csv', encoding='utf-8')
    df.to_json(path_archived + file_name + '.json', orient='records')

  def create_files(self):
    categories = helpers.get_categories('team', 'Clutch')
    last_games = helpers.get_last_games('team', 'Clutch')

    for category in categories:
      for last_game in last_games:
        self.create_file(category, last_game)

class TeamPlaytype():

  def create_file(self, category):
    now = datetime.now()
    date = now.strftime("%m-%d-%Y")
    time = now.strftime("%m-%d-%Y-%H-%M-%S")
    
    file_name = 'team_playtype_' + category['key']
    path_latest = OUT_DIR + '/stats/nba/' + date + '/latest/'
    path_archived = OUT_DIR + '/stats/nba/' + date + '/archived/' + time + '/'

    helpers.create_folder(path_latest)
    helpers.create_folder(path_archived)

    stats = league.TeamPlaytype(category=category['name'], season=now.year)
    df = stats.overall()
    df.to_csv(path_latest + file_name + '.csv', encoding='utf-8')
    df.to_json(path_latest + file_name + '.json', orient='records')
    df.to_csv(path_archived + file_name + '.csv', encoding='utf-8')
    df.to_json(path_archived + file_name + '.json', orient='records')

  def create_files(self):
    categories = helpers.get_categories('team', 'Playtype')

    for category in categories:
      self.create_file(measure_type)

class TeamTracking():
  
  def create_file(self, category, last_game):
    now = datetime.now()
    date = now.strftime("%m-%d-%Y")
    time = now.strftime("%m-%d-%Y-%H-%M-%S")
    
    file_name = 'team_tracking_' + category['key'] + '_' + last_game['name']
    path_latest = OUT_DIR + '/stats/nba/' + date + '/latest/'
    path_archived = OUT_DIR + '/stats/nba/' + date + '/archived/' + time + '/'

    helpers.create_folder(path_latest)
    helpers.create_folder(path_archived)

    stats = league._PlayerTrackingStats(player_or_team='Team', pt_measure_type=category['name'], last_n_games=last_game['value'])
    df = stats.overall()
    df.to_csv(path_latest + file_name + '.csv', encoding='utf-8')
    df.to_json(path_latest + file_name + '.json', orient='records')
    df.to_csv(path_archived + file_name + '.csv', encoding='utf-8')
    df.to_json(path_archived + file_name + '.json', orient='records')

  def create_files(self):
    categories = helpers.get_categories('team', 'Tracking')
    last_games = helpers.get_last_games('team', 'Tracking')

    for category in categories:
      for last_game in last_games:
        self.create_file(category, last_game)

class TeamDefenseDashboard():
  
  def create_file(self, category, last_game):
    now = datetime.now()
    date = now.strftime("%m-%d-%Y")
    time = now.strftime("%m-%d-%Y-%H-%M-%S")
    
    file_name = 'team_defensedashboard_' + category['key'] + '_' + last_game['name']
    path_latest = OUT_DIR + '/stats/nba/' + date + '/latest/'
    path_archived = OUT_DIR + '/stats/nba/' + date + '/archived/' + time + '/'

    helpers.create_folder(path_latest)
    helpers.create_folder(path_archived)

    stats = league.TeamDefenseDashboard(defense_category=category['name'], last_n_games=last_game['value'])
    df = stats.overall()
    df.to_csv(path_latest + file_name + '.csv', encoding='utf-8')
    df.to_json(path_latest + file_name + '.json', orient='records')
    df.to_csv(path_archived + file_name + '.csv', encoding='utf-8')
    df.to_json(path_archived + file_name + '.json', orient='records')

  def create_files(self):
    categories = helpers.get_categories('team', 'DefenseDashboard')
    last_games = helpers.get_last_games('team', 'DefenseDashboard')

    for category in categories:
      for last_game in last_games:
        self.create_file(category, last_game)

class TeamShotDashboard():
  
  def create_file(self, category, last_game):
    now = datetime.now()
    date = now.strftime("%m-%d-%Y")
    time = now.strftime("%m-%d-%Y-%H-%M-%S")
    
    file_name = 'team_shotdashboard_' + category['key'] + '_' + last_game['name']
    path_latest = OUT_DIR + '/stats/nba/' + date + '/latest/'
    path_archived = OUT_DIR + '/stats/nba/' + date + '/archived/' + time + '/'

    helpers.create_folder(path_latest)
    helpers.create_folder(path_archived)

    stats = None

    if(category['key'] == 'general'):
      stats = league.TeamShotDashboard(general_range=category['name'], last_n_games=last_game['value'])
    elif(category['key'] == 'shotclock'):
      stats = league.TeamShotDashboard(shotclock_range=category['name'], last_n_games=last_game['value'])
    elif(category['key'] == 'dribbles'):
      stats = league.TeamShotDashboard(dribbles_range=category['name'], last_n_games=last_game['value'])
    elif(category['key'] == 'touchtime'):
      stats = league.TeamShotDashboard(touchtime_range=category['name'], last_n_games=last_game['value'])
    elif(category['key'] == 'closestdefender'):
      stats = league.TeamShotDashboard(closedefdist_range=category['name'], last_n_games=last_game['value'])
    elif(category['key'] == 'closestdefender10p'):
      stats = league.TeamShotDashboard(closedefdist_range=category['name'], shotdist_range='>=10.0', last_n_games=last_game['value'])
    
    if(stats != None):
      df = stats.overall()
      df.to_csv(path_latest + file_name + '.csv', encoding='utf-8')
      df.to_json(path_latest + file_name + '.json', orient='records')
      df.to_csv(path_archived + file_name + '.csv', encoding='utf-8')
      df.to_json(path_archived + file_name + '.json', orient='records')

  def create_files(self):
    categories = helpers.get_categories('team', 'ShotDashboard')
    last_games = helpers.get_last_games('team', 'ShotDashboard')

    for category in categories:
      for last_game in last_games:
        self.create_file(category, last_game)

class BoxScores():
  
  def create_files(self):
    now = datetime.now()
    date = now.strftime("%m-%d-%Y")
    time = now.strftime("%m-%d-%Y-%H-%M-%S")
    
    file_name = 'team_boxscores'
    path_latest = OUT_DIR + '/stats/nba/' + date + '/latest/'
    path_archived = OUT_DIR + '/stats/nba/' + date + '/archived/' + time + '/'

    helpers.create_folder(path_latest)
    helpers.create_folder(path_archived)

    stats = league.GameLog()
    
    df = stats.overall()
    df.to_csv(path_latest + file_name + '.csv', encoding='utf-8')
    df.to_json(path_latest + file_name + '.json', orient='records')
    df.to_csv(path_archived + file_name + '.csv', encoding='utf-8')
    df.to_json(path_archived + file_name + '.json', orient='records')

class TeamAdvancedBoxScores():

  def create_file(self, category, last_game):
    now = datetime.now()
    date = now.strftime("%m-%d-%Y")
    time = now.strftime("%m-%d-%Y-%H-%M-%S")
    
    file_name = 'team_advancedboxscores_' + category['key'] + '_' + last_game['name']
    path_latest = OUT_DIR + '/stats/nba/' + date + '/latest/'
    path_archived = OUT_DIR + '/stats/nba/' + date + '/archived/' + time + '/'

    helpers.create_folder(path_latest)
    helpers.create_folder(path_archived)

    stats = team.TeamGameLogs(measure_type=category['name'], last_n_games=last_game['value'])
    df = stats.overall()
    df.to_csv(path_latest + file_name + '.csv', encoding='utf-8')
    df.to_json(path_latest + file_name + '.json', orient='records')
    df.to_csv(path_archived + file_name + '.csv', encoding='utf-8')
    df.to_json(path_archived + file_name + '.json', orient='records')

  def create_files(self):
    categories = helpers.get_categories('Team', 'AdvancedBoxScores')
    last_games = helpers.get_last_games('Team', 'AdvancedBoxScores')

    for category in categories:
      for last_game in last_games:
        self.create_file(category, last_game)

class TeamShooting():
  
  def create_files(self):
    now = datetime.now()
    date = now.strftime("%m-%d-%Y")
    time = now.strftime("%m-%d-%Y-%H-%M-%S")
    
    file_name = 'team_shooting'
    path_latest = OUT_DIR + '/stats/nba/' + date + '/latest/'
    path_archived = OUT_DIR + '/stats/nba/' + date + '/archived/' + time + '/'

    helpers.create_folder(path_latest)
    helpers.create_folder(path_archived)

    stats = league.TeamShooting()
    
    df = stats.overall()
    df.to_csv(path_latest + file_name + '.csv', encoding='utf-8')
    df.to_json(path_latest + file_name + '.json', orient='records')
    df.to_csv(path_archived + file_name + '.csv', encoding='utf-8')
    df.to_json(path_archived + file_name + '.json', orient='records')

class TeamOpponentShooting():
  
  def create_file(self, category):
    now = datetime.now()
    date = now.strftime("%m-%d-%Y")
    time = now.strftime("%m-%d-%Y-%H-%M-%S")
    
    file_name = 'team_opponentshooting_' + category['key']
    path_latest = OUT_DIR + '/stats/nba/' + date + '/latest/'
    path_archived = OUT_DIR + '/stats/nba/' + date + '/archived/' + time + '/'

    helpers.create_folder(path_latest)
    helpers.create_folder(path_archived)

    stats = None

    if(category['key'] == 'opponent'):
      stats = league.TeamShooting(measure_type=category['name'])
    elif(category['key'] == 'general'):
      stats = league.TeamOpponentShooting(general_range=category['name'])
    elif(category['key'] == 'shotclock'):
      stats = league.TeamOpponentShooting(shotclock_range=category['name'])
    elif(category['key'] == 'dribbles'):
      stats = league.TeamOpponentShooting(dribbles_range=category['name'])
    elif(category['key'] == 'touchtime'):
      stats = league.TeamOpponentShooting(touchtime_range=category['name'])
    elif(category['key'] == 'closestdefender'):
      stats = league.TeamOpponentShooting(closedefdist_range=category['name'])
    elif(category['key'] == 'closestdefender10p'):
      stats = league.TeamOpponentShooting(closedefdist_range=category['name'], shotdist_range='>=10.0')
    
    if(stats != None):
      df = stats.overall()
      df.to_csv(path_latest + file_name + '.csv', encoding='utf-8')
      df.to_json(path_latest + file_name + '.json', orient='records')
      df.to_csv(path_archived + file_name + '.csv', encoding='utf-8')
      df.to_json(path_archived + file_name + '.json', orient='records')

  def create_files(self):
    categories = helpers.get_categories('Team', 'OpponentShooting')

    for category in categories:
      self.create_file(category)
