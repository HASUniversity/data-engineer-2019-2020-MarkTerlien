# Tutorial: https://www.w3schools.com/python/default.asp
# Read SHP file: https://pcjericks.github.io/py-gdalogr-cookbook/
# Make DB connection: http://www.postgresqltutorial.com/postgresql-python/connect/
# Execute insert statement: http://initd.org/psycopg/docs/usage.html
import os
import psycopg2
import ogr

SHP_FOLDER = 'C:/temp/1920/testdata/'
SHP_FILENAME = '2018_Imergis_provinciegrenzen_met_water.shp'
DATABASE_CONNECTION = "dbname=engineer1920 user=postgres password=postgres"

# Inlezen csv bestand in database
os.chdir(SHP_FOLDER)

# Stap 1: Openen bestand
driver = ogr.GetDriverByName('ESRI Shapefile')
shp_file = driver.Open(SHP_FILENAME, 0)
layer = shp_file.GetLayer()

# Stap 2: Openen database
conn = psycopg2.connect(DATABASE_CONNECTION)
cur = conn.cursor()

# Stap 3: Ophalen rij uit bestand
feature_nr = 0
feature = layer.GetNextFeature()
while feature:
    feature_nr = feature_nr + 1
    # Stap 4: Ophalen waardes uit rij
    id = feature.GetField('id')
    provincienaam = feature.GetField('Provincien')
    print(id)
    print(provincienaam)
    geom = feature.GetGeometryRef()
    # Stap 5: Samenstellen geometrie    
    # Stap 6: Opstellen insert statement
    # Stap 7: Uitvoeren insert statement
    #cur.execute("INSERT INTO public.meteo_stations(id, name, altitude, geom) VALUES (%s, %s, %s, ST_SetSRID(ST_MakePoint(%s, %s),4326) )",(id, name, alt, x, y ))
    # Commit
    #conn.commit()
    # Stap 8: Ophalen volgende rij    
    feature = layer.GetNextFeature()

# Stap 9: Print feedback

# Stap 10: Sluiten database
shp_file.Destroy()
conn.close()