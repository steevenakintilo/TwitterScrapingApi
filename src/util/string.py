from datetime import datetime, timedelta

def convert_string_to_date(date_string):
    original_date = datetime.strptime(date_string, "%Y-%m-%d %H:%M:%S")
    new_date = original_date + timedelta(hours=2)
    return (new_date)