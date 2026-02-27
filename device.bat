@echo off
setlocal

echo ===============================
echo   ASTRICK ADB QUICK CONNECT
echo ===============================

set DEVICE_IP=192.168.1.8
set ADB_PORT=5555

echo Starting ADB server if needed...
adb start-server >nul 2>&1

echo Checking existing connection...
adb devices | find "%DEVICE_IP%:%ADB_PORT%" >nul
if %errorlevel%==0 (
    echo Device already connected.
    goto :end
)

echo Attempting wireless connection...
adb connect %DEVICE_IP%:%ADB_PORT% >nul

adb devices | find "%DEVICE_IP%:%ADB_PORT%" >nul
if %errorlevel%==0 (
    echo Successfully connected to %DEVICE_IP%.
) else (
    echo WARNING: Could not connect to device.
    echo Make sure:
    echo   - Phone and PC are on same WiFi
    echo   - Wireless debugging is enabled
    echo   - You ran adb tcpip 5555 once via USB
)

:end
echo Done.
exit /b