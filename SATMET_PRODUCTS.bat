@echo off
setlocal enabledelayedexpansion

:: Set the path to your Conda installation
set CONDA_PATH=C:\Softwares\miniconda

:: Set the name of the Conda environment
set CONDA_ENV=base

:: Set the Python script file path
set python_script=D:/SATMET_PRODUCTS/GII_PRODUCT/SatpyProduct/index.py

:: Set the current date and time
for /f "delims=" %%b in ('"powershell [DateTime]::Now.AddHours(-5).ToString('HH-mm')"') do set mytime=%%b
set time=%mytime%
for /f "delims=" %%a in ('"powershell [DateTime]::Now.AddHours(-5).ToString('yyyy-MM-dd')"') do set mydate=%%a
set date=%mydate%
set "destination_folder=D:/server1/Archive/%mydate%"
if not exist "!destination_folder!" mkdir "!destination_folder!"

:: Create an array to store source drive paths
set /a count=0
for /d %%D in ("Z:/Data/XRIT/Archive/MSG2_IODC/%mydate%/*") do (
    for /f "tokens=1,* delims=-" %%X in ("%%~nxD") do (
        set "hhmm=%%X-%%Y"
        set "source_drive[!count!]=Z:/Data/XRIT/Archive/MSG2_IODC/%mydate%/!hhmm!"
        set /a count+=1
    )
)

:: Loop over the source drive paths in reverse order
for /l %%i in (%count%,-1,0) do (
    set "source_drive=!source_drive[%%i]!"
    if exist "!source_drive!" (
        python %python_script% "!date!" "!hhmm!" "!source_drive!" "!destination_folder!"
    )
)

:: Deactivate Conda environment
:: call "%CONDA_PATH%\Scripts\deactivate.bat"

:: Wait for 5 minutes before the next iteration
timeout /t 300 /nobreak
goto :EOF
