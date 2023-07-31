from datetime import datetime, timedelta
import os
import platform

def convert_string_to_date(date_string):
    original_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    new_date = original_date + timedelta(hours=2)
    return (new_date)

def get_absolute_picture_path(relative_path):
    current_directory = os.getcwd()    
    absolute_path = os.path.join(current_directory, relative_path)
    if os.path.exists(absolute_path) and os.path.isfile(absolute_path):
        return absolute_path
    else:
        return relative_path

def get_operating_system():
    return platform.system()
