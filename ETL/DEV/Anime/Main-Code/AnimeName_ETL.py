import requests
import json 
# import mysql.connector
import sys
import os

# Add the path to the directory containing 'Params.py' to sys.path
sys.path.append(r'C:\Users\Metac\Downloads\python-code\Data-Pipelines\ETL\DEV\Anime\Params')
# Now you can import 'credentials' from Params.py
from credentials import MySQL_username, MySQL_password
from globals import download_path


## Actual code

# Part 1 - EXTRACT 

for i in range(10):
    id=i
    url_value=f'https://api.jikan.moe/v4/anime/{id}/full'
    print(url_value)
    url = url_value
    
    response = requests.get(url)
    data = response.json()

    file_name=f'{download_path}extrt{id}.json'
    with open( file_name, 'w') as json_file:
        json.dump(data, json_file, indent=4)




"""
# Create a connection object
cnx = mysql.connector.connect(
    user=username,
    password=password,
    host=host,
    database=database
)

# Create a cursor object
cursor = cnx.cursor()

# Execute the MySQL command
cursor.execute("SELECT * FROM your_table")

# Fetch the results
results = cursor.fetchall()

# Print the results
for row in results:
    print(row)
    
    
# Close the cursor and connection
cursor.close()
cnx.close()

"""