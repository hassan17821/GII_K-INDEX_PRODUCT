import os
import datetime
import subprocess
import time
import schedule

# Constants
PYTHON_SCRIPT = os.path.join(os.path.dirname(__file__), "index.py")
BASE_ARCHIVE_PATH = r"D:/server1/Archive/HRIT_Python"
BASE_DATA_PATH = r"Z:/Data/XRIT/Archive/MSG2_IODC"
TIME_DELTA_HOURS = 5
TIME_DELTA_MINUTES = 20
PROCESS_TIME_DELTA_HOURS = 3

def process_data(end_time, start_time):
    print(f"Processing data for {end_time.strftime('%Y-%m-%d')} {end_time.strftime('%H-%M')}")
    
    destination_folder = os.path.join(BASE_ARCHIVE_PATH, end_time.strftime('%Y-%m-%d'))
    os.makedirs(destination_folder, exist_ok=True)

    base_path = os.path.join(BASE_DATA_PATH, end_time.strftime('%Y-%m-%d'))
    
    source_drives = []
    if os.path.exists(base_path):
        for folder in os.listdir(base_path):
            if os.path.isdir(os.path.join(base_path, folder)):
                folder_time = folder  # Use the folder name directly as the time
                if start_time.strftime('%H-%M') <= folder_time <= end_time.strftime('%H-%M'):
                    source_drives.append((folder_time, os.path.join(base_path, folder)))
    
    # Sort source drives in reverse chronological order
    source_drives.sort(reverse=True)
    
    # Skip the first (most recent) time slot
    if source_drives:
        source_drives = source_drives[1:]
    
    print("source_drives:", source_drives)

    # Process the files
    for hhmm, source_drive in source_drives:
        if os.path.exists(source_drive):
            destination_folder = os.path.join(BASE_ARCHIVE_PATH, end_time.strftime('%Y-%m-%d'), hhmm)
            os.makedirs(destination_folder, exist_ok=True)
            subprocess.run(["python", PYTHON_SCRIPT, end_time.strftime('%Y-%m-%d'), hhmm, source_drive, destination_folder])
    
    print(f"Processed data from {end_time.strftime('%H:%M')} to {start_time.strftime('%H:%M')}, skipping the most recent time slot")

def job():
    current_time = datetime.datetime.now() - datetime.timedelta(hours=TIME_DELTA_HOURS)
    end_time = current_time - datetime.timedelta(minutes=TIME_DELTA_MINUTES)
    start_time = current_time - datetime.timedelta(hours=PROCESS_TIME_DELTA_HOURS)

    # Round down to the nearest 15-minute interval
    end_time = end_time - datetime.timedelta(minutes=end_time.minute % 15, seconds=end_time.second, microseconds=end_time.microsecond)
    start_time = start_time - datetime.timedelta(minutes=start_time.minute % 15, seconds=start_time.second, microseconds=start_time.microsecond)

    process_data(end_time, start_time)

def main():
    print("SatpyIndex.py started")
    job()
    # Schedule the job to run every 5 minutes
    schedule.every(5).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
