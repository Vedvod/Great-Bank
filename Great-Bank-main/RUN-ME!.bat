ECHO OFF
cd  "%CD%\Scripts\" & rem #This changes the working directory to the Scripts folder, where the python script is located. This means that the script runs as though run normally.
cls & echo Great Bank ATM & PING localhost -n 1 >NUL & echo A script by Sameer Sabri and Ved Dhiman & PING localhost -n 4 >NUL & rem #intro message
cls & py -m pip install "%CD%/keyboard-0.13.5-py3-none-any.whl" & py -m pip install "%CD%/wxPython-4.1.1-cp39-cp39-win_amd64.whl" & rem This installs the keybaord module dependency
:pythonrun
	cls & python "%CD%\main.py" & pause & rem #This uses the 'python' command to run the script, replicating manually running the script, then pauses after the program ends
	set/p again="Run the script again? " 
	if /i "%again%" == "yes" goto pythonrun
	if /i "%again%" == "y" goto pythonrun
	echo Thanks for using our script! & PING localhost -n 4 >NUL & rem #Thanks message and pause