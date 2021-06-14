ECHO OFF
cd  "%CD%\Scripts\" & rem #This changes the working directory to the Scripts folder, where the python script is located. This means that the script runs as though run normally.
cls & echo Great Bank ATM, A script by Sameer Sabri and Ved Dhiman & PING localhost -n 6 >NUL & rem #intro message\
:pythonrun
	cls & MODE con:cols=140 lines=40 & echo Please resize the window until it is a comfortable size. & pause
	cls & python "%CD%\main.py" & pause & rem #This uses the 'python' command to run the script, replicating manually running the script, then pauses after the program ends
	set/p again="Run the script again? " 
	if /i "%again%" == "yes" goto pythonrun
	echo Thanks for using our script! & PING localhost -n 4 >NUL & rem #Thanks message and pause