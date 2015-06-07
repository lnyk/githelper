# githelper
A simple python script to operate GIT in a short hand.

# Requirement
* A *nix like system, cygwin and mingw not tested yet.
* Python version >= 2.7
* git in $PATH

# Usage
Just put the main script file (githelper.py) in your $PATH and call it.

## Options
* -a           : git add --all
* -c <comment> : git commit -m "comment"
* -p           : git push
* -s           : git status
* -C <comment> : run all the 4 commands above for you.

## Known Issues
* Option order matters!
In current version of this script, the git operation flow is built by the order of options appeared in the command line, so DO NOT put -c before -a, you know why!

* Not tested in cygwin and mingw yet!
If you really want to use git on windows without GUI tools like Github for Windows, I think you know what to do with this python script.
