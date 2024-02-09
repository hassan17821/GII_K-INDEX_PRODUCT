@echo off
setlocal enabledelayedexpansion

:: Set the path to your Conda installation
set CONDA_PATH=C:\Softwares\miniconda

:: Set the name of the Conda environment
set CONDA_ENV=base

:: Set the Python script file path
set python_script=T:/Mohsin/SATMET_PRODUCTS/GII_PRODUCT/plot_kIndex.py

:: Activate Conda environment
call "%CONDA_PATH%\Scripts\activate.bat" %CONDA_ENV%

:: Set the current date and time
for /f "delims=" %%b in ('"powershell [DateTime]::Now.AddHours(-5).ToString('HH-mm')"') do set mytime=%%b
set time=%mytime%
for /f "delims=" %%a in ('"powershell [DateTime]::Now.AddHours(-5).ToString('yyyy-MM-dd')"') do set mydate=%%a
set date=%mydate%
set "destination_folder=D:/server1/Archive/%mydate%"
if not exist "!destination_folder!" mkdir "!destination_folder!"

set "source_drive=S:/Archive/%mydate%/09-30/GII.bufr"
if exist "!source_drive!" (
    python %python_script% "!date!" "09-30" "!source_drive!" "!destination_folder!"
)

:: Deactivate Conda environment
call "%CONDA_PATH%\Scripts\deactivate.bat"