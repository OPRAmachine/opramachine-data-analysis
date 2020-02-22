import pandas as pd 
import psycopg2 as pg
import pandas.io.sql as psql

# Get all OPRAmachine public bodies as they currently exist on the site
authorities = pd.read_csv("https://opramachine.com/body/all-authorities.csv", parse_dates=["Created at","Updated at"])

# Get the other data from the site's database
connection = pg.connect("dbname=alaveteli_production user=postgres")

# Users
dataframe = psql.frame_query("SELECT * FROM <tablename>", connection)

# Requests

