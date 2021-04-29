import datetime as dt
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify

#set up our database engine for the Flask application, Access the SQLite database.
engine = create_engine("sqlite:///hawaii.sqlite")

# Reflect the database into our classes
Base = automap_base()
#Reflect the tables into SQLAlchemy
Base.prepare(engine, reflect=True)

#create a variable for each of the classes
Measurement = Base.classes.measurement
Station = Base.classes.station

#create a session link from Python to our database
session = Session(engine)

# Define our flask app
app = Flask(__name__)

# Define the welcome route
@app.route('/')

#build our Flask routes, Module 9.5.2
def welcome():
    return(
    '''
    Welcome to the Climate Analysis API!
    Available Routes:
    /api/v1.0/precipitation
    /api/v1.0/stations
    /api/v1.0/tobs
    /api/v1.0/temp/start/end
    ''')

# Define the precipitation route
@app.route("/api/v1.0/precipitation")

# Create the precipitation function
def precipitation():

    # Calculate the date one year ago from the most recent date in the database
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)

    # Get the date and precip for the prev year
    precipitation = session.query(Measurement.date, Measurement.prcp).\
        filter(Measurement.date >= prev_year).all()
    
    # Define a dictionary for the data
    precip = {date: prcp for date, prcp in precipitation}
    # Create a .json file from the dictionary
    return jsonify(precip)  

# Define the stations route
@app.route('/api/v1.0/stations')

# Create the stations function
def stations():

    # Get all of the stations from the database
    results = session.query(Station.station).all()

    # Unravel results into a 1-D array and convert to list, then jsonify
    stations = list(np.ravel(results))

    return jsonify(stations=stations)

# Define the temp route
@app.route("/api/v1.0/tobs")

# Create the temperature function
def temp_monthly():

    # Query the primary station for all the temps for the prev year
    prev_year = dt.date(2017, 8, 23) - dt.timedelta(days=365)
    results = session.query(Measurement.tobs).\
        filter(Measurement.station == 'USC00519281').\
        filter(Measurement.date >= prev_year).all()

    # Unravel 1D array, array to list to json
    temps = list(np.ravel(results))
    return jsonify(temps=temps)

# Define start and end date routes for statistics
@app.route("/api/v1.0/temp/<start>")
@app.route("/api/v1.0/temp/<start>/<end>")

# Define statistics function
def stats(start=None, end=None):

    # Create list for querying database
    sel = [func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)]

    # Query database using sel, unravel results into 1-D -> list -> json
    if not end:
        results = session.query(*sel).\
            filter(Measurement.date >= start).\
            filter(Measurement.date <= end).all()
        temps = list(np.ravel(results))
        return jsonify(temps=temps)

    # Calculate temp min, avg, max
    results = session.query(*sel).\
        filter(Measurement.date >= start).\
        filter(Measurement.date <= end).all()
    temps = list(np.ravel(results))

    return jsonify(temps=temps)
    
