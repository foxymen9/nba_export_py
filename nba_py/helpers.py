
import os, errno
from datetime import datetime
from nba_py import constants

OUT_DIR = constants.BASE_DIR + '/data_files'

def totimestamp(dt, epoch=datetime(1970,1,1)):
  td = dt - epoch
  
  return (td.microseconds + (td.seconds + td.days * 86400) * 10**6) / 10**6 


def create_folder(path):
  try:
    os.makedirs(path)
  except OSError as e:
    if e.errno != errno.EEXIST:
      raise


def create_file(file_name, stats):
  now = datetime.now()
  date = now.strftime("%m-%d-%Y")
  time = now.strftime("%m-%d-%Y-%H-%M-%S")
  
  path_latest = OUT_DIR + '/stats/nba/' + date + '/latest/'
  path_archived = OUT_DIR + '/stats/nba/' + date + '/archived/' + time + '/'

  create_folder(path_latest)
  create_folder(path_archived)

  df = stats.overall()
  df.to_csv(path_latest + file_name + '.csv', encoding='utf-8')
  df.to_json(path_latest + file_name + '.json', orient='records')
  df.to_csv(path_archived + file_name + '.csv', encoding='utf-8')
  df.to_json(path_archived + file_name + '.json', orient='records')


def get_last_games():
  return [
    { 'name': 'Season', 'value': 0 },
    { 'name': 'L1', 'value': 1 },
    { 'name': 'L2', 'value': 2 },
    { 'name': 'L3', 'value': 3 },
    { 'name': 'L5', 'value': 5 },
    { 'name': 'L10', 'value': 10 }
  ]


def get_categories(type, section):
  if(section == 'General'):
    if(type == 'team'):
      return [
        { 'key': 'traditional', 'name': 'Base' },
        { 'key': 'advanced', 'name': 'Advanced' },
        { 'key': 'fourfactors', 'name': 'Four Factors' },
        { 'key': 'misc', 'name': 'Misc' },
        { 'key': 'scoring', 'name': 'Scoring' },
        { 'key': 'opponent', 'name': 'Opponent' },
        { 'key': 'defense', 'name': 'Defense' }
      ]
    else:
      return [
        { 'key': 'traditional', 'name': 'Base' },
        { 'key': 'advanced', 'name': 'Advanced' },
        { 'key': 'misc', 'name': 'Misc' },
        { 'key': 'scoring', 'name': 'Scoring' },
        { 'key': 'usage', 'name': 'Usage' },
        { 'key': 'opponent', 'name': 'Opponent' },
        { 'key': 'defense', 'name': 'Defense' }
      ]
  elif(section == 'Clutch'):
    if(type == 'team'):
      return [
        { 'key': 'traditional', 'name': 'Base' },
        { 'key': 'advanced', 'name': 'Advanced' },
        { 'key': 'fourfactors', 'name': 'Four Factors' },
        { 'key': 'misc', 'name': 'Misc' },
        { 'key': 'scoring', 'name': 'Scoring' },
        { 'key': 'opponent', 'name': 'Opponent' }
      ]
    else:
      return [
        { 'key': 'traditional', 'name': 'Base' },
        { 'key': 'advanced', 'name': 'Advanced' },
        { 'key': 'misc', 'name': 'Misc' },
        { 'key': 'scoring', 'name': 'Scoring' },
        { 'key': 'usage', 'name': 'Usage' }
      ]
  elif(section == 'Playtype'):
    return [
      { 'key': 'transition', 'name': 'Transition' },
      { 'key': 'isolation', 'name': 'Isolation' },
      { 'key': 'prballhandler', 'name': 'PRBallHandler' },
      { 'key': 'prrollman', 'name': 'PRRollman' },
      { 'key': 'postup', 'name': 'Postup' },
      { 'key': 'spotup', 'name': 'Spotup' },
      { 'key': 'handoff', 'name': 'Handoff' },
      { 'key': 'cut', 'name': 'Cut' },
      { 'key': 'offscreen', 'name': 'OffScreen' },
      { 'key': 'putbacks', 'name': 'OffRebound' },
      { 'key': 'misc', 'name': 'Misc' }
    ]
  elif(section == 'Tracking'):
    return [
      { 'key': 'drives', 'name': 'Drives' },
      { 'key': 'defense', 'name': 'Defense' },
      { 'key': 'catchshoot', 'name': 'CatchShoot' },
      { 'key': 'passing', 'name': 'Passing' },
      { 'key': 'touches', 'name': 'Possessions' },
      { 'key': 'rebounding', 'name': 'Rebounding' },
      { 'key': 'efficiency', 'name': 'Efficiency' },
      { 'key': 'speeddistance', 'name': 'SpeedDistance' },
      { 'key': 'elbowtouches', 'name': 'ElbowTouch' },
      { 'key': 'posttouches', 'name': 'PostTouch' },
      { 'key': 'painttouches', 'name': 'PaintTouch' },
      { 'key': 'pullupshot', 'name': 'PullUpShot' }
    ]
  elif(section == 'DefenseDashboard'):
    return [
      { 'key': 'overall', 'name': 'Overall' },
      { 'key': '3pointers', 'name': '3 Pointers' },
      { 'key': '2pointers', 'name': '2 Pointers' },
      { 'key': 'lt6ft', 'name': 'Less Than 6Ft' },
      { 'key': 'lt10ft', 'name': 'Less Than 10Ft' },
      { 'key': 'gt15ft', 'name': 'Greater Than 15Ft' }
    ]
  elif(section == 'ShotDashboard'):
    return [
      { 'key': 'general', 'name': 'Overall' },
      { 'key': 'shotclock', 'name': '24-22' },
      { 'key': 'dribbles', 'name': '0 Dribbles' },
      { 'key': 'touchtime', 'name': 'Touch < 2 Seconds' },
      { 'key': 'closestdefender', 'name': '0-2 Feet - Very Tight' },
      { 'key': 'closestdefender10p', 'name': '0-2 Feet - Very Tight' }
    ]
  elif(section == 'AdvancedBoxScores'):
    if(type == 'team'):
      return [
        { 'key': 'traditional', 'name': 'Base' },
        { 'key': 'advanced', 'name': 'Advanced' },
        { 'key': 'fourfactors', 'name': 'Four Factors' },
        { 'key': 'misc', 'name': 'Misc' },
        { 'key': 'scoring', 'name': 'Scoring' }
      ]
    else:
      return [
        { 'key': 'traditional', 'name': 'Base' },
        { 'key': 'advanced', 'name': 'Advanced' },
        { 'key': 'misc', 'name': 'Misc' },
        { 'key': 'scoring', 'name': 'Scoring' },
        { 'key': 'usage', 'name': 'Usage' }
      ]
  elif(section == 'OpponentShooting'):
    return [
      { 'key': 'opponent', 'name': 'Opponent' },
      { 'key': 'general', 'name': 'Overall' },
      { 'key': 'shotclock', 'name': '24-22' },
      { 'key': 'dribbles', 'name': '0 Dribbles' },
      { 'key': 'touchtime', 'name': 'Touch < 2 Seconds' },
      { 'key': 'closestdefender', 'name': '0-2 Feet - Very Tight' },
      { 'key': 'closestdefender10p', 'name': '0-2 Feet - Very Tight' }
    ]
  
  return []

