from datetime import datetime
from rest_framework import generics
from rest_framework.response import Response
from nba_py import team, league
from . import helpers


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
    teamHustle = TeamHustle()
    playerGeneral = PlayerGeneral()

    # teamGeneral.create_files()
    # teamClutch.create_files()
    # teamPlaytype.create_files()
    # teamTracking.create_files()
    # teamDefenseDashboard.create_files()
    # teamShotDashboard.create_files()
    # boxScores.create_files()
    # teamAdvancedBoxScores.create_files()
    # teamShooting.create_files()
    # teamOpponentShooting.create_files()
    # teamHustle.create_files()
    playerGeneral.create_files()

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


class TeamPlaytype():

  def create_files(self):
    now = datetime.now()
    categories = helpers.get_categories('team', 'Playtype')

    print('Export files of TeamPlaytype')

    for category in categories:
      file_name = 'team_playtype_' + category['key']
      stats = league.TeamPlaytype(category=category['name'], season=now.year)
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


class BoxScores():
  
  def create_files(self):
    file_name = 'team_boxscores'
    stats = league.GameLog()

    print('Export files of BoxScores')
    helpers.create_file(file_name, stats)


class TeamAdvancedBoxScores():

  def create_files(self):
    categories = helpers.get_categories('Team', 'AdvancedBoxScores')
    last_games = helpers.get_last_games()

    print('Export files of TeamAdvancedBoxScores')

    for category in categories:
      for last_game in last_games:
        file_name = 'team_advancedboxscores_' + category['key'] + '_' + last_game['name']
        stats = team.TeamGameLogs(measure_type=category['name'], last_n_games=last_game['value'])
        helpers.create_file(file_name, stats)


class TeamShooting():
  
  def create_files(self):
    file_name = 'team_shooting'
    stats = league.TeamShooting()

    print('Export files of TeamShooting')
    helpers.create_file(file_name, stats)


class TeamOpponentShooting():

  def create_files(self):
    categories = helpers.get_categories('Team', 'OpponentShooting')

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


class TeamHustle():

  def create_files(self):
    last_games = helpers.get_last_games()

    print('Export files of TeamHustle')

    for last_game in last_games:
      file_name = 'team_hustle_' + last_game['name']
      stats = league.TeamHustle(last_n_games=last_game['value'])
      helpers.create_file(file_name, stats)

