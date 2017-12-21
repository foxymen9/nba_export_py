
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
