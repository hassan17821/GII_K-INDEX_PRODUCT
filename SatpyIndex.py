import os
import datetime
import subprocess
import time
import schedule

def collect_sort_pick_files(folder_path):
    # Collect all files in the folder
    all_files = []
    for root, dirs, files in os.walk(folder_path):
        for file in files:
            file_path = os.path.join(root, file)
            all_files.append(file_path)

    # Sort files by modification time (newest first)
    sorted_files = sorted(all_files, key=os.path.getmtime, reverse=True)

    # Pick files (in this case, all except the most recent)
    picked_files = sorted_files[1:]

    return picked_files

def process_data(end_time, start_time):
    print(f"Processing data for {end_time.strftime('%Y-%m-%d')} {end_time.strftime('%H-%M')}")
    python_script = r"D:/SATMET_PRODUCTS/GII_PRODUCT/SatpyProduct/index.py"
    
    destination_folder = rf"D:/server1/Archive/HRIT_Python/{end_time.strftime('%Y-%m-%d')}"
    os.makedirs(destination_folder, exist_ok=True)

    base_path = rf"Z:/Data/XRIT/Archive/MSG2_IODC/{end_time.strftime('%Y-%m-%d')}"
    
    if os.path.exists(base_path):
        files_to_process = collect_sort_pick_files(base_path)
        
        print(f"Files to process: {files_to_process}")

        # Process the files
        for file_path in files_to_process:
            file_time = os.path.basename(os.path.dirname(file_path))
            if start_time.strftime('%H-%M') <= file_time <= end_time.strftime('%H-%M'):
                subprocess.run(["python", python_script, end_time.strftime('%Y-%m-%d'), file_time, os.path.dirname(file_path), destination_folder])
    
    print(f"Processed data from {end_time.strftime('%H:%M')} to {start_time.strftime('%H:%M')}, skipping the most recent file")

def job():
    current_time = datetime.datetime.now() - datetime.timedelta(hours=5)
    end_time = current_time - datetime.timedelta(minutes=20)
    start_time = current_time - datetime.timedelta(hours=3)

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