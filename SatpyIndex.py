import os
import datetime
import subprocess
import time
import schedule

def process_data(end_time, start_time):

    print(f"Processing data for {end_time.strftime('%Y-%m-%d')} {end_time.strftime('%H-%M')}")
    python_script = r"D:/SATMET_PRODUCTS/GII_PRODUCT/SatpyProduct/index.py"
    
    # destination_folder = os.path.join(r"D:/server1/Archive/HRIT_Python", end_time.strftime('%Y-%m-%d'))
    destination_folder = rf"D:/server1/Archive/HRIT_Python/{end_time.strftime('%Y-%m-%d')}"
    
    os.makedirs(destination_folder, exist_ok=True)

    base_path = rf"Z:/Data/XRIT/Archive/MSG2_IODC/{end_time.strftime('%Y-%m-%d')}"
    
    source_drives = []
    if os.path.exists(base_path):
        for folder in os.listdir(base_path):
            if os.path.isdir(os.path.join(base_path, folder)):
                folder_time = folder  # Use the folder name directly as the time
                if start_time.strftime('%H-%M') <= folder_time <= end_time.strftime('%H-%M'):
                    source_drives.append((folder_time, base_path + "/" + folder))
    
    # Sort source drives in reverse chronological order
    source_drives.sort(reverse=True)
    
    # Skip the first (most recent) time slot
    if source_drives:
        source_drives = source_drives[1:]
    
    print("source_drives:", source_drives)

    # Process the files
    for hhmm, source_drive in source_drives:
        if os.path.exists(source_drive):
            subprocess.run(["python", python_script, end_time.strftime('%Y-%m-%d'), hhmm, source_drive, destination_folder])
    
    print(f"Processed data from {end_time.strftime('%H:%M')} to {start_time.strftime('%H:%M')}, skipping the most recent time slot")

def job():
    current_time = datetime.datetime.now() - datetime.timedelta(hours=5)
    end_time = current_time - datetime.timedelta(minutes=20)
    start_time = current_time - datetime.timedelta(hours=3)

    # Round down to the nearest 15-minute interval
    end_time = end_time - datetime.timedelta(minutes=end_time.minute % 15, seconds=end_time.second, microseconds=end_time.microsecond)
    start_time = start_time - datetime.timedelta(minutes=start_time.minute % 15, seconds=start_time.second, microseconds=start_time.microsecond)

    process_data(end_time, start_time)

def main():
    print ("SatpyIndex.py started")
    job()
    # Schedule the job to run every 5 minutes
    schedule.every(5).minutes.do(job)

    while True:
        schedule.run_pending()
        time.sleep(1)

if __name__ == "__main__":
    main()
