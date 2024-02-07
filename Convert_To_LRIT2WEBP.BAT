@echo off
setlocal enabledelayedexpansion

:: Set the path to your Conda installation
set CONDA_PATH=C:\Softwares\miniconda

:: Set the name of the Conda environment
set CONDA_ENV=base

:: Set the Python script file path
set python_script=T:/Mohsin/SATMET_PRODUCTS/GII_PRODUCT/plot_kIndex.py

:LOOP
:: Activate Conda environment
call "%CONDA_PATH%\Scripts\activate.bat" %CONDA_ENV%

:: Set the current date and time
for /f "delims=" %%b in ('"powershell [DateTime]::Now.AddHours(-5).ToString('HH-mm')"') do set mytime=%%b
set time=%mytime%
for /f "delims=" %%a in ('"powershell [DateTime]::Now.AddHours(-5).ToString('yyyy-MM-dd')"') do set mydate=%%a
set date=%mydate%
set "destination_folder=D:/server1/Archive/%mydate%"
if not exist "!destination_folder!" mkdir "!destination_folder!"

:: Iterate over HH-mm folders within the specified date
for /d %%D in ("S:/Archive/%mydate%/*") do (
    :: Check if the folder name is in the format of HH-mm
    for /f "tokens=1,* delims=-" %%X in ("%%~nxD") do (
        set "hhmm=%%X-%%Y"
        set "source_drive=S:/Archive/%mydate%/!hhmm!/GII.bufr"
        if exist "!source_drive!" (
            python %python_script% "!date!" "!hhmm!" "!source_drive!" "!destination_folder!"
        )
    )
)

:: Deactivate Conda environment
call "%CONDA_PATH%\Scripts\deactivate.bat"

:: Wait for 5 minutes before the next iteration
timeout /t 300 /nobreak
goto LOOP
