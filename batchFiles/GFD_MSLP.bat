@echo off
setlocal enabledelayedexpansion

set CONDA_PATH=C:\Softwares\miniconda

:: Set the name of the Conda environment
set CONDA_ENV=base

:: Set the Python script file path
set python_script=D:/SATMET_PRODUCTS/MSG_PYTHON_PRODUCT/GFS/mslp/index.py

:: Set the current date and time
python %python_script%
