@echo off
setlocal enabledelayedexpansion

set CONDA_PATH=C:\Softwares\miniconda

:: Set the name of the Conda environment
set CONDA_ENV=base

:: Set the Python script file path
set python_script=D:/SATMET_PRODUCTS/MSG_PYTHON_PRODUCT/LRIT_Product/LRIT_main.py

:: Activate Conda environment
call "%CONDA_PATH%\Scripts\activate.bat" %CONDA_ENV%

:: Set the current date and time
python %python_script%
