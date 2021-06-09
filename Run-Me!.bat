cd  "%CD%\Scripts\" & rem #This changes the working directory to the Scripts folder, where the python script is located. This means that the script runs as though run normally.
cls & rem #This clears the screen, so that the previous command is hidden
cls & echo Great Bank ATM, A script by Sameer Sabri and Ved Dhiman & PING localhost -n 6 >NUL & rem #intro message
cls & python "%CD%\Ved_Dhiman_Sameer_Sabri_Prelim_Task2_2021.py" & pause & rem #This uses the 'python' command to run the script, replicating manually running the script
cls & echo Thanks for using our script! & PING localhost -n 4 >NUL & rem #Thanks message and pause