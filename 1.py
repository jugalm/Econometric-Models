import pandas as pd
import psycopg2
from sqlalchemy import create_engine

df = pd.read_table('/Users/jugalmarfatia/Downloads/Bhavnani India State Election Dataset v 3.0.tab')

engine = create_engine('postgresql+psycopg2://jugal1:jugal1@localhost/postgres')

df = pd.read_csv('/Users/jugalmarfatia/Documents/summer2018/RA Work/wage_gap/Wage_Gap/data/ipumsi_00004.csv')
df.to_sql('india_wage', con=engine, index=False, if_exists='replace', chunksize=100)
