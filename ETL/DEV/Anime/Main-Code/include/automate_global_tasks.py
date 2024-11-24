from globals import current_mal_id, Param_path

# var_change is a function build to auto increment integer store in a param file.
# it requires 4 inputs Variable Name(var_name), Limiting number to increase(limiter), file name to read/change and store the value(param_file), current variable value(var_value) 
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


