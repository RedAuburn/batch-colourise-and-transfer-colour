@echo off
echo.
echo ##############
echo # Dependency #
echo # Installer  #
echo ##############
:start
echo.
echo Do you want to install dependencies? (y/n)
set /p yn=""
echo.
if "%yn%"=="y" (
	pip install Pillow==7.1.2
	pip install PySimpleGUI==4.19.0
	GOTO end
)
GOTO start
:end
PAUSE
