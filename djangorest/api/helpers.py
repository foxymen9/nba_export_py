
import os, errno

def create_folder(path):
  try:
    os.makedirs(path)
  except OSError as e:
    if e.errno != errno.EEXIST:
      raise

def get_measure_types(type, section):
  if(section == 'General'):
    return [
      { 'key': 'traditional', 'name': 'Base' },
      { 'key': 'advanced', 'name': 'Advanced' },
      { 'key': 'fourfactors', 'name': 'Four Factors' },
      { 'key': 'misc', 'name': 'Misc' },
      { 'key': 'scoring', 'name': 'Scoring' },
      { 'key': 'opponent', 'name': 'Opponent' },
      { 'key': 'defense', 'name': 'Defense' }
    ]
  elif(section == 'Clutch'):
    return [
      { 'key': 'traditional', 'name': 'Base' },
      { 'key': 'advanced', 'name': 'Advanced' },
      { 'key': 'fourfactors', 'name': 'Four Factors' },
      { 'key': 'misc', 'name': 'Misc' },
      { 'key': 'scoring', 'name': 'Scoring' },
      { 'key': 'opponent', 'name': 'Opponent' }
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
      { 'key': 'possessions', 'name': 'Possessions' },
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
  
  return []

def get_last_games(type, section):
  return [
    { 'name': 'Season', 'value': 0 },
    { 'name': 'L1', 'value': 1 },
    { 'name': 'L2', 'value': 2 },
    { 'name': 'L3', 'value': 3 },
    { 'name': 'L5', 'value': 5 },
    { 'name': 'L10', 'value': 10 }
  ]
