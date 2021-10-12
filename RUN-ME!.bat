ECHO OFF
cd  "%CD%\Scripts\" & rem #This changes the working directory to the Scripts folder, where the python script is located. This means that the script runs as though run normally.
cls & echo Great Bank ATM & PING localhost -n 2 >NUL & echo A script by Sameer and Vedvod & PING localhost -n 3 >NUL & rem #intro message
cls & py -m pip install "%CD%/six-1.16.0-py2.py3-none-any.whl" "%CD%/keyboard-0.13.5-py3-none-any.whl" "%CD%/colorama-0.4.4-py2.py3-none-any.whl" & rem #This installs the module dependencies

cls & py -m pip install "%CD%/Pillow-8.2.0-cp39-cp39-win_amd64.whl" "%CD%/wxPython-4.1.1-cp39-cp39-win_amd64.whl" "%CD%/numpy-1.20.3-cp39-cp39-win_amd64.whl" & rem #This is for 64 bit
cls & py -m pip install "%CD%/Pillow-8.2.0-cp39-cp39-win32.whl" "%CD%/wxPython-4.1.1-cp39-cp39-win32.whl" "%CD%/numpy-1.21.0-cp39-cp39-win32.whl" & rem #This is for 32 bit
:pythonrun
	cls & python "%CD%\main.py" & pause & rem #This uses the 'python' command to run the script, replicating manually running the script, then pauses after the program ends
	set/p again="Run the script again? " 
	if /i "%again%" == "yes" goto pythonrun
	if /i "%again%" == "y" goto pythonrun
	echo Thanks for using our script! & PING localhost -n 4 >NUL & rem #Thanks message and pause
