@echo off
setlocal enabledelayedexpansion

set CONDA_PATH=C:\Softwares\miniconda

:: Set the name of the Conda environment
set CONDA_ENV=base

:: Set the Python script file path
set python_script=D:/SATMET_PRODUCTS/GII_PRODUCT/SatpyIndex.py

:: Set the current date and time
python %python_script%
