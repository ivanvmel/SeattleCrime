import csv
import datetime
from database import db_session
from database import init_db
from models import Crime

file = open('Seattle_Police_Department_911_Incident_Response.csv')
csv_file = csv.reader(file)
init_db()

def is_number(s):
    try:
        float(s)
        return True
    except ValueError:
        return False

def is_date(d):
    try:
        datetime.datetime.strptime(d, '%m/%d/%Y %I:%M:%S %p')
        return True
    except ValueError:
        print("Fucked up!")
        return False

def is_string(s):
    return s and s != 'NULL'

counter = 0
for row in csv_file:
    description = row[4].strip()
    date = row[7].strip()
    longitude = row[12].strip()
    latitude = row[13].strip()

    if is_string(description) and is_date(date) and is_number(longitude) and is_number(latitude):
        c = Crime(description, datetime.datetime.strptime(date, '%m/%d/%Y %I:%M:%S %p'), longitude, latitude)
        db_session.add(c)
        counter += 1

    if counter % 1000 == 0:
        db_session.commit()
        print(counter)

db_session.commit()
db_session.remove()