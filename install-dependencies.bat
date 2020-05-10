@echo off
echo.
echo ##############
echo # Dependency #
echo # Installer  #
echo ##############
:start
echo.
echo Do you want to install dependencies? (y/n)?
set /p yn=""
echo.
if "%yn%"=="y" (
	pip install Pillow==7.1.2 --user
	pip install requests
	GOTO end
)
GOTO start
:end
PAUSE
