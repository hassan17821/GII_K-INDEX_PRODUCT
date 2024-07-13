import os
import datetime
import subprocess
import time

def main():
    while True:
        # Set the path to your Conda installation
        conda_path = r"C:\Softwares\miniconda"

        # Set the name of the Conda environment
        conda_env = "base"

        # Set the Python script file path
        python_script = r"D:/SATMET_PRODUCTS/GII_PRODUCT/GIIProduct/index.py"
        input_dir = r"//EUMETCAST-INGES/Data/XRIT/BinaryFiles/Archive"

        # Activate Conda environment
        activate_cmd = f"{conda_path}\\Scripts\\activate.bat {conda_env}"
        subprocess.run(activate_cmd, shell=True)

        # Set the current date and time
        current_time = datetime.datetime.now() - datetime.timedelta(hours=5)
        time_str = current_time.strftime("%H-%M")
        date_str = current_time.strftime("%Y-%m-%d")
        destination_folder = ""

        # Create a list to store source drive paths
        source_drives = []
        for folder in os.listdir(os.path.join(input_dir, date_str)):
            hhmm = folder
            source_drive = os.path.join(input_dir, date_str, folder, "GII.bufr")
            source_drives.append((hhmm, source_drive))

        # Sort source drives in reverse order
        source_drives.sort(reverse=True)

        # Loop over the source drive paths
        temp_count = 0
        max_bounds = 10
        for hhmm, source_drive in source_drives:
            if os.path.exists(source_drive):
                destination_folder = f"D:/server1/Archive/LRIT_Python/{date_str}/{hhmm}"
                # os.makedirs(destination_folder, exist_ok=True)
                print(f"=============== LRIT ===================")
                print(f"Processing LRIT data for {date_str} {hhmm}")
                print(f"Source drive: {source_drive}")
                print(f"Destination folder: {destination_folder}")
                print(f"=======================================")
                subprocess.run(["python", python_script, date_str, hhmm, source_drive, destination_folder])
                temp_count += 1
                if temp_count > max_bounds:
                    break

        print(f"Loop terminated because temp count = {temp_count}.")

        # Deactivate Conda environment (commented out in original script)
        # deactivate_cmd = f"{conda_path}\\Scripts\\deactivate.bat"
        # subprocess.run(deactivate_cmd, shell=True)

        # Wait for 20 seconds before the next iteration
        time.sleep(20)

if __name__ == "__main__":
    main()