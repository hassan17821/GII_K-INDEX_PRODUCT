@echo off
setlocal

:: Set the Python script file path
set python_script=T:/Mohsin/SATMET_PRODUCTS/GII_PRODUCT/plot_kIndex.py

:: Set the command-line arguments
set date=%date:~-4%-%date:~4,2%-%date:~7,2%
set time=%time:~0,5%
for /f "delims=" %%b in ('"powershell [DateTime]::Now.AddHours(-5).ToString('HH-mm')"') do set mytime=%%b
set time=%mytime%
for /f "delims=" %%a in ('"powershell [DateTime]::Now.AddHours(-5).ToString('yyyy-MM-dd')"') do set mydate=%%a
set date=%mydate%

set source_drive="C:\Users\Administrator\Downloads\GII_09-45__2024-02-02.bufr"
set destination_drive="T:/Mohsin/SATMET_PRODUCTS/GII_PRODUCT/%mydate%/LRIT_GII_KINDEX [%time%].webp"

set "directory=T:/Mohsin/SATMET_PRODUCTS/GII_PRODUCT/%date:/=_%"
set "mydate=%date:/=_%"

:: Check if directory exists
if not exist "%directory%" (
    mkdir "%directory%"
    echo Directory created: %directory%
) else (
    echo Directory already exists: %directory%
)

:: Activate the Python environment
:: call activate my_python_env

:: Run the Python script with the command-line arguments
python %python_script% %date% %time% %source_drive% %destination_drive%

endlocal