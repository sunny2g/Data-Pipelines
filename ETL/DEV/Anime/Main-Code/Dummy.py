import sys
import os
# Add the path to the directory containing 'Params.py' to sys.path
sys.path.append(r'C:\Users\Metac\Downloads\python-code\Data-Pipelines\ETL\DEV\Anime\Params')
# Now you can import 'credentials' from Params.py
from credentials import MySQL_username, MySQL_password
from globals import download_path
print(download_path)
id=1
file_name=f'{download_path}\extrt{id}.json'

print(file_name)

with open( file_name, 'w') as json_file:
    pass