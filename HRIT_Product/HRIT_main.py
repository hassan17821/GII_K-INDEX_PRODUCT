import os
import datetime
import subprocess
import time
import schedule
from collections import deque

# Constants
PYTHON_SCRIPT = os.path.join(os.path.dirname(__file__), "index.py")
DESTINATION_PATH = r"D:/server1/Archive/HRIT_Python"
SOURCE_DRIVE_PATH = r"//EUMETCAST-INGES/Dartcom/Data/XRIT/Archive/MSG2_IODC"
TIME_DELTA_HOURS = 5
TIME_DELTA_MINUTES = 20
PROCESS_TIME_DELTA_HOURS = 3
MAX_RETRIES = 3  # Check current period and one previous 5-hour period

# Cache to store processed time slots
processed_cache = deque(maxlen=1000)  # Store last 1000 processed time slots

def get_source_drives(date):
    source_drive_path = os.path.join(SOURCE_DRIVE_PATH, date.strftime('%Y-%m-%d'))
    if not os.path.exists(source_drive_path):
        return []

    source_drives = [
        (folder, os.path.join(source_drive_path, folder))
        for folder in os.listdir(source_drive_path)
        if os.path.isdir(os.path.join(source_drive_path, folder))
    ]
    
    # Sort source drives in reverse chronological order and skip the most recent
    return sorted(source_drives, reverse=True)[1:]

def process_data(end_time, start_time):
    print(f"Processing data for {end_time.strftime('%Y-%m-%d %H-%M')}")
    
    source_drives = get_source_drives(end_time)
    
    if not source_drives:
        print(f"No source drives found for {end_time.strftime('%Y-%m-%d')}. Skipping processing.")
        return False

    destination_base = os.path.join(DESTINATION_PATH, end_time.strftime('%Y-%m-%d'))
    os.makedirs(destination_base, exist_ok=True)

    processed_any = False
    for hhmm, source_drive in source_drives:
        # update the source drives if new data comes
        if os.path.exists(source_drive):
        # if os.path.exists(source_drive) and hhmm not in processed_cache:

            destination_folder = os.path.join(destination_base, hhmm)
            os.makedirs(destination_folder, exist_ok=True)
            subprocess.run(["python", PYTHON_SCRIPT, end_time.strftime('%Y-%m-%d'), hhmm, source_drive, destination_folder])
            processed_cache.append(hhmm)
            processed_any = True

    if processed_any:
        print(f"Processed data from {end_time.strftime('%Y-%m-%d %H:%M')} to {start_time.strftime('%Y-%m-%d %H:%M')}, skipping the most recent time slot")
    return processed_any

def job():
    current_time = datetime.datetime.now()
    
    for i in range(MAX_RETRIES):
        adjusted_time = current_time - datetime.timedelta(hours=TIME_DELTA_HOURS * (i + 1))
        end_time = adjusted_time - datetime.timedelta(minutes=TIME_DELTA_MINUTES)
        start_time = adjusted_time - datetime.timedelta(hours=PROCESS_TIME_DELTA_HOURS)

        # Round down to the nearest 15-minute interval
        end_time = end_time.replace(minute=end_time.minute - end_time.minute % 15, second=0, microsecond=0)
        start_time = start_time.replace(minute=start_time.minute - start_time.minute % 15, second=0, microsecond=0)

        if process_data(end_time, start_time):
            break
        else:
            print(f"No data found for period ending at {end_time.strftime('%Y-%m-%d %H:%M')}. Checking previous 5-hour period.")

def main():
    print("SatpyIndex.py started")
    job()
    schedule.every(1).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()