# The Great Bank company
This repository is a storage for the files of our SDD Preliminary Course Assignment 2 task, which is to code an ATM in Python. We have opted to construct our ATM as the property of the fictional Great Bank, which is unrelated to the existent [Greater](https://en.wikipedia.org/wiki/Greater_Bank) [Bank](https://www.greaterbank.com/). To this end, we (and [this website](https://patorjk.com/software/taag/#p=display&f=Graffiti&t=Type%20Something%20)) have made an ASCII logo.  

```
+================================================+
ǁ         GGGGGGGGGGGGG     BBBBBBBBBBBBBBBBB    ǁ
ǁ      GGG::::::::::::G     B::::::::::::::::B   ǁ
ǁ    GG:::::::::::::::G     B::::::BBBBBB:::::B  ǁ
ǁ   G:::::GGGGGGGG::::G     BB:::::B     B:::::B ǁ
ǁ  G:::::G       GGGGGG       B::::B     B:::::B ǁ
ǁ G:::::G                     B::::B     B:::::B ǁ
ǁ G:::::G                     B::::BBBBBB:::::B  ǁ
ǁ G:::::G    GGGGGGGGGG       B:::::::::::::BB   ǁ
ǁ G:::::G    G::::::::G       B::::BBBBBB:::::B  ǁ
ǁ G:::::G    GGGGG::::G       B::::B     B:::::B ǁ
ǁ G:::::G        G::::G       B::::B     B:::::B ǁ
ǁ  G:::::G       G::::G       B::::B     B:::::B ǁ
ǁ   G:::::GGGGGGGG::::G     BB:::::BBBBBB::::::B ǁ
ǁ    GG:::::::::::::::G     B:::::::::::::::::B  ǁ
ǁ      GGG::::::GGG:::G     B::::::::::::::::B   ǁ
ǁ         GGGGGG   GGGGreat BBBBBBBBBBBBBBBBBank ǁ
+================================================+
```
The logo features the large initials GB, and the full name in small text below.

# Instructions
First, [download the ZIP file from the repository](https://github.com/Vedvod/Great-Bank/archive/refs/heads/main.zip), and extract the folder inside. The folder can be extracted to any location, as long as the hierarchy is not modified for the [batch file](https://github.com/Vedvod/Great-Bank/blob/main/Run-Me!.bat) and the [Scripts folder](https://github.com/Vedvod/Great-Bank/tree/main/Scripts). Having extracted the folder, run the [Run-Me!.bat file](https://github.com/Vedvod/Great-Bank/blob/main/Run-Me!.bat). This will initiate the program. The script files can be found in the [Scripts folder](https://github.com/Vedvod/Great-Bank/tree/main/Scripts), and the documentation is within the [main directory](https://github.com/Vedvod/Great-Bank/tree/main).  
Make sure to run the [toggleclear.py file](https://github.com/Vedvod/Great-Bank/blob/main/toggleclear.py) if running the script on an IDE that does not support os.system('clear') or os.system('cls'), such as IDLE, or PyCharm. This will substitute the screen clear for newlines, which, while less effective, will function properly for these IDEs.  
Receipts from transactions can be found in the [receipts directory](https://github.com/Vedvod/Great-Bank/tree/main/Scripts/receipts) within the [Scripts folder](https://github.com/Vedvod/Great-Bank/tree/main/Scripts). Each user has three receipt slots, after which the oldest receipt will be overwritten.  
Our documentation can (will) be found on the [logbook document](https://docs.google.com/document/d/14dr7cmlmFfUxpMpVZmCA-mB59K0Lx-MyVKvaO-z-XV4/). This documentation will be updated as the project progresses.

Last updated: 10:09 21/06/21

# Changelog  

## 0.6 - Polishing Up
**21/06/21**
0.6.3.1 - Fixed up code done yesterday, yet more bugfixing.

**20/06/21**
0.6.3 - Finished delete function completely, more bugfixing and commenting.

**19/06/21**
0.6.2.1 - Commenting, bugfixing, renewal of work on delete function.

**18/06/21**  
0.6.2 - Changes to dependency installation procedure, now comes packaged with the keyboard wheel file, and installs it within start-up.  

**17/06/21**  
0.6.1 - Bugfixes, improvements to the ask function and t function.  
0.6 - Merged with main branch, updated delete to remove balances. The project now almost fully resembles the final design.

## 0.5 - Readability and Documentation

**16/06/21**  
0.5.3 - Implemented fully-automatic calibration, which uses the non-standard python modules ['keyboard'](https://pypi.org/project/keyboard/#description) and ['wxPython'](https://pypi.org/project/wxPython/), and the standard module os. The module is installed during the setup (within the batch file), so the user only needs to have internet connection.

0.5.2.1 - Fixed errors with the ask, sprint, and tinput functions. The code runs slightly smoother now.

**14/06/21**  
0.5.2 - Added auto-calibration for command prompt users. Does not work for IDEs. Also, bugfixing.

**11/06/21**  
0.5.1.3 - More bugfixing.

**10/06/21**  
0.5.1.2 - Updated documentation for universal functions.

**09/06/21**  
0.5.1.1 - Added more comments, and did more bugfixing.  
0.5.1 - Finished implementation of delete functionality, fixed up batch file to hide command prompts and pause correctly.  

**08/06/21**  
0.5 - Large-scale expansion of the README, a new dedicated branch, and an addition of a batch file to the main directory that streamlines starting the script. Additionally, the script now checks if it is running in python command prompt, and adjusts accordingly.  

## 0.4 - Menu and Access

**07/06/21**  
0.4.2 - Added delete functionality, users can now delete their profile.  
0.4.1.2 - Bugfixes, Added more comments.  

**06/06/21**  
0.4.1.1 - Added comments and spacing for readability.  
0.4.1 - Fixed some bugs.  
0.4 - Added receipts.  

## 0.3 - Framework

0.3 and prior - lacks documentation.  
