ECHO OFF
cd  "%CD%\Scripts\" & rem #This changes the working directory to the Scripts folder, where the python script is located. This means that the script runs as though run normally.
cls & echo Great Bank ATM & PING localhost -n 1 >NUL & echo A script by Sameer Sabri and Ved Dhiman & PING localhost -n 4 >NUL & rem #intro message
cls & echo This script requires the module keyboard. If you continue, this will be installed, if not already installed. & pause
cls & py -m pip install keyboard
:pythonrun
	cls & python "%CD%\main.py" & pause & rem #This uses the 'python' command to run the script, replicating manually running the script, then pauses after the program ends
	set/p again="Run the script again? " 
	if /i "%again%" == "yes" goto pythonrun
	if /i "%again%" == "y" goto pythonrun
	echo Thanks for using our script! & PING localhost -n 4 >NUL & rem #Thanks message and pause