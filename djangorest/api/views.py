from datetime import datetime
from rest_framework import generics
from rest_framework.response import Response
from nba_py import league
from . import helpers


class NBAStatsView(generics.ListAPIView):

  def list(self, request):
    teamGeneral = TeamGeneral()
    teamClutch = TeamClutch()
    teamPlaytype = TeamPlaytype()
    teamTracking = TeamTracking()
    teamDefenseDashboard = TeamDefenseDashboard()
    teamShotDashboard = TeamShotDashboard()
    teamBoxScores = TeamBoxScores()
    teamAdvancedBoxScores = TeamAdvancedBoxScores()
    teamShooting = TeamShooting()
    teamOpponentShooting = TeamOpponentShooting()
    teamHustle = TeamHustle()
    playerGeneral = PlayerGeneral()
    playerClutch = PlayerClutch()
    playerPlaytype = PlayerPlaytype()
    playerTracking = PlayerTracking()
    playerDefenseDashboard = PlayerDefenseDashboard()
    playerShotDashboard = PlayerShotDashboard()
    playerBoxScores = PlayerBoxScores()
    playerAdvancedBoxScores = PlayerAdvancedBoxScores()
    playerShooting = PlayerShooting()
    playerOpponentShooting = PlayerOpponentShooting()
    playerHustle = PlayerHustle()
    
    teamGeneral.create_files()
    teamClutch.create_files()
    teamPlaytype.create_files()
    teamTracking.create_files()
    teamDefenseDashboard.create_files()
    teamShotDashboard.create_files()
    teamBoxScores.create_files()
    teamAdvancedBoxScores.create_files()
    teamShooting.create_files()
    teamOpponentShooting.create_files()
    teamHustle.create_files()
    playerGeneral.create_files()
    playerClutch.create_files()
    playerPlaytype.create_files()
    playerTracking.create_files()
    playerDefenseDashboard.create_files()
    playerShotDashboard.create_files()
    playerBoxScores.create_files()
    playerAdvancedBoxScores.create_files()
    playerShooting.create_files()
    playerOpponentShooting.create_files()
    playerHustle.create_files()
    
    print('All Done!')

    return Response("OK", 200)


class TeamGeneral():

  def create_files(self):
    categories = helpers.get_categories('team', 'General')
    last_games = helpers.get_last_games()

    print('Export files of TeamGeneral')

    for category in categories:
      for last_game in last_games:
        file_name = 'team_general_' + category['key'] + '_' + last_game['name']
        stats = league.TeamStats(measure_type=category['name'], last_n_games=last_game['value'])

        helpers.create_file(file_name, stats)


class PlayerGeneral():

  def create_files(self):
    categories = helpers.get_categories('player', 'General')
    last_games = helpers.get_last_games()

    print('Export files of PlayerGeneral')

    for category in categories:
      for last_game in last_games:
        file_name = 'player_general_' + category['key'] + '_' + last_game['name']
        stats = None

        if category['key'] == 'opponent':
          stats = league.PlayerDetails(measure_type=category['name'], last_n_games=last_game['value'])
        else:
          stats = league.PlayerStats(measure_type=category['name'], last_n_games=last_game['value'])

        helpers.create_file(file_name, stats)


class TeamClutch():

  def create_files(self):
    categories = helpers.get_categories('team', 'Clutch')
    last_games = helpers.get_last_games()

    print('Export files of TeamClutch')

    for category in categories:
      for last_game in last_games:
        file_name = 'team_clutch_' + category['key'] + '_' + last_game['name']
        stats = league.TeamClutch(measure_type=category['name'], last_n_games=last_game['value'])
        helpers.create_file(file_name, stats)


class PlayerClutch():

  def create_files(self):
    categories = helpers.get_categories('player', 'Clutch')
    last_games = helpers.get_last_games()

    print('Export files of PlayerClutch')

    for category in categories:
      for last_game in last_games:
        file_name = 'player_clutch_' + category['key'] + '_' + last_game['name']
        stats = league.PlayerClutch(measure_type=category['name'], last_n_games=last_game['value'])
        helpers.create_file(file_name, stats)


class TeamPlaytype():

  def create_files(self):
    now = datetime.now()
    categories = helpers.get_categories('team', 'Playtype')

    print('Export files of TeamPlaytype')

    for category in categories:
      file_name = 'team_playtype_' + category['key']
      stats = league.TeamPlaytype(category=category['name'], season=now.year)
      helpers.create_file(file_name, stats)


class PlayerPlaytype():

  def create_files(self):
    now = datetime.now()
    categories = helpers.get_categories('player', 'Playtype')

    print('Export files of PlayerPlaytype')

    for category in categories:
      file_name = 'player_playtype_' + category['key']
      stats = league.PlayerPlaytype(category=category['name'], season=now.year)
      helpers.create_file(file_name, stats)


class TeamTracking():

  def create_files(self):
    categories = helpers.get_categories('team', 'Tracking')
    last_games = helpers.get_last_games()

    print('Export files of TeamTracking')

    for category in categories:
      for last_game in last_games:
        file_name = 'team_tracking_' + category['key'] + '_' + last_game['name']
        stats = league._PlayerTrackingStats(player_or_team='Team', pt_measure_type=category['name'], last_n_games=last_game['value'])
        helpers.create_file(file_name, stats)


class PlayerTracking():

  def create_files(self):
    categories = helpers.get_categories('player', 'Tracking')
    last_games = helpers.get_last_games()

    print('Export files of PlayerTracking')

    for category in categories:
      for last_game in last_games:
        file_name = 'player_tracking_' + category['key'] + '_' + last_game['name']
        stats = league._PlayerTrackingStats(player_or_team='Player', pt_measure_type=category['name'], last_n_games=last_game['value'])
        helpers.create_file(file_name, stats)


class TeamDefenseDashboard():

  def create_files(self):
    categories = helpers.get_categories('team', 'DefenseDashboard')
    last_games = helpers.get_last_games()

    print('Export files of TeamDefenseDashboard')

    for category in categories:
      for last_game in last_games:
        file_name = 'team_defensedashboard_' + category['key'] + '_' + last_game['name']
        stats = league.TeamDefenseDashboard(defense_category=category['name'], last_n_games=last_game['value'])
        helpers.create_file(file_name, stats)


class PlayerDefenseDashboard():

  def create_files(self):
    categories = helpers.get_categories('player', 'DefenseDashboard')
    last_games = helpers.get_last_games()

    print('Export files of PlayerDefenseDashboard')

    for category in categories:
      for last_game in last_games:
        file_name = 'player_defensedashboard_' + category['key'] + '_' + last_game['name']
        stats = league.PlayerDefenseDashboard(defense_category=category['name'], last_n_games=last_game['value'])
        helpers.create_file(file_name, stats)


class TeamShotDashboard():

  def create_files(self):
    categories = helpers.get_categories('team', 'ShotDashboard')
    last_games = helpers.get_last_games()

    print('Export files of TeamShotDashboard')

    for category in categories:
      for last_game in last_games:
        file_name = 'team_shotdashboard_' + category['key'] + '_' + last_game['name']
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
          helpers.create_file(file_name, stats)


class PlayerShotDashboard():

  def create_files(self):
    categories = helpers.get_categories('player', 'ShotDashboard')

    print('Export files of PlayerShotDashboard')

    for category in categories:
      file_name = 'player_shotdashboard_' + category['key']
      stats = None

      if(category['key'] == 'general'):
        stats = league.PlayerShotDashboard(general_range=category['name'])
      elif(category['key'] == 'shotclock'):
        stats = league.PlayerShotDashboard(shotclock_range=category['name'])
      elif(category['key'] == 'dribbles'):
        stats = league.PlayerShotDashboard(dribbles_range=category['name'])
      elif(category['key'] == 'touchtime'):
        stats = league.PlayerShotDashboard(touchtime_range=category['name'])
      elif(category['key'] == 'closestdefender'):
        stats = league.PlayerShotDashboard(closedefdist_range=category['name'])
      elif(category['key'] == 'closestdefender10p'):
        stats = league.PlayerShotDashboard(closedefdist_range=category['name'], shotdist_range='>=10.0')
      
      if(stats != None):
        helpers.create_file(file_name, stats)


class TeamBoxScores():
  
  def create_files(self):
    file_name = 'team_boxscores'
    stats = league.GameLog(player_or_team='T')

    print('Export files of TeamBoxScores')
    helpers.create_file(file_name, stats)


class PlayerBoxScores():
  
  def create_files(self):
    file_name = 'player_boxscores'
    stats = league.GameLog(player_or_team='P')

    print('Export files of PlayerBoxScores')
    helpers.create_file(file_name, stats)


class TeamAdvancedBoxScores():

  def create_files(self):
    categories = helpers.get_categories('team', 'AdvancedBoxScores')
    last_games = helpers.get_last_games()

    print('Export files of TeamAdvancedBoxScores')

    for category in categories:
      for last_game in last_games:
        file_name = 'team_advancedboxscores_' + category['key'] + '_' + last_game['name']
        stats = league.GameLogs(endpoint='teamgamelogs', measure_type=category['name'], last_n_games=last_game['value'])
        helpers.create_file(file_name, stats)


class PlayerAdvancedBoxScores():

  def create_files(self):
    categories = helpers.get_categories('player', 'AdvancedBoxScores')
    last_games = helpers.get_last_games()

    print('Export files of PlayerAdvancedBoxScores')

    for category in categories:
      for last_game in last_games:
        file_name = 'player_advancedboxscores_' + category['key'] + '_' + last_game['name']
        stats = league.GameLogs(endpoint='playergamelogs', measure_type=category['name'], last_n_games=last_game['value'])
        helpers.create_file(file_name, stats)


class TeamShooting():
  
  def create_files(self):
    file_name = 'team_shooting'
    stats = league.TeamShooting()

    print('Export files of TeamShooting')
    helpers.create_file(file_name, stats)


class PlayerShooting():

  def create_files(self):
    print('Export files of PlayerShooting')

    file_name = 'player_shooting'
    stats = league.PlayerShooting()
    helpers.create_file(file_name, stats)


class TeamOpponentShooting():

  def create_files(self):
    categories = helpers.get_categories('team', 'OpponentShooting')

    print('Export files of TeamOpponentShooting')

    for category in categories:
      file_name = 'team_opponentshooting_' + category['key']
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
        helpers.create_file(file_name, stats)


class PlayerOpponentShooting():

  def create_files(self):
    print('Export files of PlayerOpponentShooting')

    file_name = 'player_opponentshooting'
    stats = league.PlayerShooting(measure_type='Opponent')
    helpers.create_file(file_name, stats)


class TeamHustle():

  def create_files(self):
    last_games = helpers.get_last_games()

    print('Export files of TeamHustle')

    for last_game in last_games:
      file_name = 'team_hustle_' + last_game['name']
      stats = league.TeamHustle(last_n_games=last_game['value'])
      helpers.create_file(file_name, stats)


class PlayerHustle():
  
  def create_files(self):
    last_games = helpers.get_last_games()

    print('Export files of PlayerHustle')

    for last_game in last_games:
      file_name = 'player_hustle_' + last_game['name']
      stats = league.PlayerHustle(last_n_games=last_game['value'])
      helpers.create_file(file_name, stats)
