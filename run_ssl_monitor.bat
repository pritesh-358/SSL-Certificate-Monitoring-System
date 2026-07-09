@echo off

REM ==========================================================
REM SSL Certificate Monitoring System
REM Author : Pritesh Thamke
REM ==========================================================

set PROJECT_DIR=C:\Users\my\Downloads\ssl-certificate-monitor

cd /d "%PROJECT_DIR%"

echo.
echo ===============================================
echo SSL Certificate Monitoring System
echo ===============================================
echo.

REM Activate Virtual Environment
call raj\Scripts\activate.bat

echo Virtual Environment Activated
echo.

python -u app\main.py

echo.
echo ===============================================
echo Monitoring Completed
echo ===============================================

pause