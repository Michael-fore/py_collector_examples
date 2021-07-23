from db_models import ErcotLMP, session
from py_collector import Collector, Scheduler
from datetime import datetime
import requests

app = Collector()
app.start_time = datetime.now()#to start immediatly
app.scheduler = Scheduler(minutes=5, 
                    count=5, 
                    separator=10,
                    start_time = datetime.now())

def upload():
        ''' Runs on schedule, and will only run if is_new 
            returns true'''
        r = requests.get('https://api.weather.gov/gridpoints/FWD/59,23/forecast')
        data = r.json()['properties']['periods']
        points = []
        for i in data:
            data_point = ErcotLMP(
                settlement_point = 'test',
                lmp = 1,
                five_min = 1
            )
            points.append(data_point)

        session.add_all(points)
        session.commit()  

def is_new():
    '''Evaluates if the data should be uploaded,
    if it only returns True, then it will just upload 
    on schedule.'''
    return True

app.upload = upload

app.is_new = is_new

if __name__ =='__main__':
    app.monitor()