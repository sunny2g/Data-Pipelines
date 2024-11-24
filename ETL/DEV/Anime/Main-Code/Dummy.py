import sys
import os
# Add the path to the directory containing 'Params.py' to sys.path
sys.path.append(r'C:\Users\Metac\Downloads\python-code\Data-Pipelines\ETL\DEV\Anime\Params')
# Now you can import 'credentials' from Params.py
from credentials import MySQL_username, MySQL_password


from globals import current_mal_id, Param_path
from include import automate_global_tasks

automate_global_tasks.var_change('current_mal_id',5,f"{Param_path}globals.py",current_mal_id)








from globals import current_mal_id, Param_path

def var_change(var_name,limiter,param_file,var_value):
    id=var_value
    limit = var_value + limiter
    print(f"the current mal_id is {var_name}")
    while id < limit:
        print(f"the current sequence number is {id}")
        # Open the file to read
        with open(param_file, 'r') as file:
            file_content = file.readlines()
        # Modify the line with the current_mal_id
        for i, line in enumerate(file_content):
            if line.startswith(var_name):
                file_content[i] = f"{var_name} = {id}"
        # Write the updated content back to the file
        with open(param_file, 'w') as file:
            file.writelines(file_content)
        print("Parameter updated successfully!")
        id=id + 1
var_change('current_mal_id',4,f"{Param_path}globals.py",current_mal_id)














####### print(current_mal_id)
####### id=1
####### file_name=f'{download_path}\extrt{id}.json'
####### 
####### print(file_name)
####### 
####### with open( file_name, 'w') as json_file:
#######     pass
####### 
####### 

