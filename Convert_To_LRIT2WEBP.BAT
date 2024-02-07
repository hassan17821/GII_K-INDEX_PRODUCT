@echo off
setlocal enabledelayedexpansion

:: Set the Python script file path
set python_script=T:/Mohsin/SATMET_PRODUCTS/GII_PRODUCT/plot_kIndex.py

:: Set the current date and time
for /f "delims=" %%b in ('"powershell [DateTime]::Now.AddHours(-5).ToString('HH-mm')"') do set mytime=%%b
set time=%mytime%
for /f "delims=" %%a in ('"powershell [DateTime]::Now.AddHours(-5).ToString('yyyy-MM-dd')"') do set mydate=%%a
set date=%mydate%

echo "%mydate%"
:: Iterate over HH-mm folders within the specified date
for /d %%D in ("S:/Archive/%mydate%/*") do (
    :: Check if the folder name is in the format of HH-mm
    for /f "tokens=1,* delims=-" %%X in ("%%~nxD") do (
        set "hhmm=%%X-%%Y"
        echo "!hhmm!"
        set "source_drive=S:/Archive/%mydate%/!hhmm!/GII.bufr"
        
        echo "!source_drive!"

        :: Check if GII.bufr file exists inside the current folder
        if exist "!source_drive!" (
            set "destination_drive=T:/Mohsin/SATMET_PRODUCTS/GII_PRODUCT/%mydate%/LRIT_GII_KINDEX [!hhmm!].webp"
            
            :::: Check if the destination directory exists, create if not
            ::set "directory=T:/Mohsin/SATMET_PRODUCTS/GII_PRODUCT/%mydate%"
            ::if not exist "%directory%" (
            ::    mkdir "%directory%"
            ::    echo Directory created: %directory%
            ::) else (
            ::    echo Directory already exists: %directory%
            ::)

            :: Activate the Python environment if needed
            :: call activate my_python_env

            :: Run the Python script with the command-line arguments
            if not exist "!destination_drive!" (
               python %python_script% "!date!" "!time!" "!source_drive!" "!destination_drive!"
            )
        )
    )
)

endlocal