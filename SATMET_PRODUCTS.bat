@echo off
setlocal enabledelayedexpansion

:START_POINT
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
        set "hhmm[!count!]=%%X-%%Y"
        set "source_drive[!count!]=Z:/Data/XRIT/Archive/MSG2_IODC/%mydate%/%%X-%%Y"
        set /a count+=1
    )
)

:: Loop over the source drive paths in reverse order
set "temp_count=0"
set "max_bounds=10"
for /l %%i in (%count%,-1,0) do (
    echo "i = %%i"
    set "source_drive=!source_drive[%%i]!"
    set "hhmm=!hhmm[%%i]!"
    if exist "!source_drive!" (
        python %python_script% "!date!" "!hhmm!" "!source_drive!" "!destination_folder!"
        set /a temp_count+=1
        if !temp_count! gtr !max_bounds! (
            goto :break_loop
        )
    )
)
:break_loop
echo "Loop terminated because temp count = %temp_count%." 

:: Deactivate Conda environment
:: call "%CONDA_PATH%\Scripts\deactivate.bat"

:: Wait for 5 minutes before the next iteration
timeout /t 20 /nobreak
goto :START_POINT
