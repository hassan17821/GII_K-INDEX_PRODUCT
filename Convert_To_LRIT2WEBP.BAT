@echo off
setlocal enabledelayedexpansion

:: Set the Python script file path
set python_script=T:/Mohsin/SATMET_PRODUCTS/GII_PRODUCT/plot_kIndex.py

:: Set the current date and time
for /f "delims=" %%b in ('"powershell [DateTime]::Now.AddHours(-5).ToString('HH-mm')"') do set mytime=%%b
set time=%mytime%
for /f "delims=" %%a in ('"powershell [DateTime]::Now.AddHours(-5).ToString('yyyy-MM-dd')"') do set mydate=%%a
set date=%mydate%
set "destination_folder=T:/Mohsin/SATMET_PRODUCTS/GII_PRODUCT/%mydate%"
if not exist "!destination_folder!" mkdir "!destination_folder!"

echo "%mydate%"
:: Iterate over HH-mm folders within the specified date
for /d %%D in ("S:/Archive/%mydate%/*") do (
    :: Check if the folder name is in the format of HH-mm
    for /f "tokens=1,* delims=-" %%X in ("%%~nxD") do (
        set "hhmm=%%X-%%Y"
        echo "!hhmm!"
        set "source_drive=S:/Archive/%mydate%/!hhmm!/GII.bufr"
        set "destination_drive=T:/Mohsin/SATMET_PRODUCTS/GII_PRODUCT/%mydate%/LRIT_GII_KINDEX [!hhmm!].webp"
        echo "!source_drive!"
        if not exist "!destination_drive!" if exist "!source_drive!" (
            python %python_script% "!date!" "!time!" "!source_drive!" "!destination_drive!"
        )
    )
)

endlocal