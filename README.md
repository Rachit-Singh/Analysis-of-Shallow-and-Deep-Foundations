# Analysis-of-Shallow-and-Deep-Foundations

Prerequisites :-
These all are required just for Windows. Linux and Mac come pre-cooked with python and pip. But in Mac, it's better to upgrade it.
Latest version of python installed. Python 3.8.x
While installing, don't forget to click on Add to PATH, which will appear in the installation wizard.
Make sure you can access python from the Command Prompt. Type python --version and see if that outputs the current version of python installed
Make sure pip works fine. run pip --version and see if that outputs the current version of pip.

Running the program :-
MAKE SURE YOUR INTERNET IS TURNED ON WHEN RUNNING FOR THE FIRST TIME.
The program installs 3 packages, namely numpy, pandas and openpyxl, in case they are not already present in the system.

WINDOWS
Easy method :-
Copy the file to the desired location and double click. The script will do the rest.

Second method :-
Copy the file to the desired location.
Open the cmd and change the working directory to the one where the script is saved.
Type python piles.py and Enter. Shebang doesn't work in windows, so python interpreter needs to be called, everytime running a python script from cmd.
OR
If your system is configured correctly, you can drag and drop your script from Explorer onto the Command Line window and press enter.

Side note:- If possible, download the latest Windows Terminal, freely available on Microsoft Store and use that for running the script. It is truly magical. It supports windows, ubuntu, opensuse and many more terminals in a single package. Bash scripting can be done from Windows easily. Pretty amazing.
Plus it supports emojis as well. On running in the normal command prompt, weird symbols will be visible in place of sweet emojis ☹️.(that are present in the program). 
Linux and Mac support emojis from way back. 

LINUX 
This code was originally built on linux, so it takes full advantage of the OS. Colorful emojis render correctly and perfectly 😀.
Go to the folder where the script is saved. Right click and select Open in Terminal.
Make the script executable. The script contains shebang, so can be directly run from the terminal without calling the interpreter everytime.
$ chmod +x piles.py
Now just run 
$ ./piles.py

If the automatic installation of packages is causing any problem (especially in Windows), install the packages manually using pip. Just run 
pip install numpy pandas openpyxl
Internet must be kept on during package installation.
Then run the program again.

NOTE:- Must read the instructions given inside the program (option 3). It has some points that must be known before using the Load bearing capacity calculation facility. Read all the points.
