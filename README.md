# NBA stats data exports

### How to run

```
  virtualenv -p python3 env

  source env/bin/activate

  pip3 install -r requirements.txt

  cd djangorest

  python3 manage.py runserver
```

After hosting on http://127.0.0.1:8000, you can send request from your local http://127.0.0.1:8000/nba/stats to export all NBA stats data.