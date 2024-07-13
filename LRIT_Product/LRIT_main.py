import os
import datetime
import subprocess
import time

# Constants
CONDA_PATH = r"C:\Softwares\miniconda"
CONDA_ENV = "base"
PYTHON_SCRIPT = os.path.join(os.path.dirname(__file__), "index.py")
INPUT_DIR = r"//EUMETCAST-INGES/Data/XRIT/BinaryFiles/Archive"
MAX_BOUNDS = 10
TIME_DELTA_HOURS = 5
SLEEP_DURATION = 20

def main():
    while True:
        # Activate Conda environment
        activate_cmd = f"{CONDA_PATH}\\Scripts\\activate.bat {CONDA_ENV}"
        subprocess.run(activate_cmd, shell=True)

        # Set the current date and time
        current_time = datetime.datetime.now() - datetime.timedelta(hours=TIME_DELTA_HOURS)
        time_str = current_time.strftime("%H-%M")
        date_str = current_time.strftime("%Y-%m-%d")
        destination_folder = ""

        # Create a list to store source drive paths
        source_drives = []
        for folder in os.listdir(os.path.join(INPUT_DIR, date_str)):
            hhmm = folder
            source_drive = os.path.join(INPUT_DIR, date_str, folder, "GII.bufr")
            source_drives.append((hhmm, source_drive))

        # Sort source drives in reverse order
        source_drives.sort(reverse=True)

        # Loop over the source drive paths
        temp_count = 0
        for hhmm, source_drive in source_drives:
            if os.path.exists(source_drive):
                destination_folder = f"D:/server1/Archive/LRIT_Python/{date_str}/{hhmm}"
                print(f"=============== LRIT ===================")
                print(f"Processing LRIT data for {date_str} {hhmm}")
                print(f"Source drive: {source_drive}")
                print(f"Destination folder: {destination_folder}")
                print(f"=======================================")
                subprocess.run(["python", PYTHON_SCRIPT, date_str, hhmm, source_drive, destination_folder])
                temp_count += 1
                if temp_count > MAX_BOUNDS:
                    break

        print(f"Loop terminated because temp count = {temp_count}.")

        # Deactivate Conda environment (commented out in original script)
        # deactivate_cmd = f"{conda_path}\\Scripts\\deactivate.bat"
        # subprocess.run(deactivate_cmd, shell=True)

        # Wait for the next iteration
        time.sleep(SLEEP_DURATION)

if __name__ == "__main__":
    main()
