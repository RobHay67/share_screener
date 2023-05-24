

# Developer Notes

<br>
<br>
<br>


## Git Commands
|Order of Operations						|Command Line (Terminal)|
|-----------|-----------|
|Log into GitHub to create project			||
|On Dev Computer - folder above project		|git clone https://github.com/RobHay67/Pluto_blue.git|
|Push Local brach to GitHub					|git push -u origin [branch]|
|delete local branch						|git branch -d <branch] |

<br>
<br>

## Pipenv - Create Initial Environment
### https://realpython.com/pipenv-guide/

|Order of Operations							|Command Line (Terminal)|
|-----------|-----------|
|Ensure you are in the project folder			|cd [project_folder]	|
|Create pipenv Environement	(Creates Pipfile)	|pipenv shell|
|Set the appropriate Python Version				|pipenv install --python 3.8|
|Add Streamlit package							|pipenv install streamlit|
|Add Watchdog package							|pipenv install watchdog|

<br>
<br>

## Pipenv - Primary Commands
|Order of Operations									|Command Line (Terminal)|
|-----------|-----------|
|Activate the Environment								|pipenv shell|
|De-Activate the Environment							|exit|
|Downloaded Pipenv Project (install Pipfile Packages)	|pipenv install|
|Downloaded Project (Install Dev Environement Packages)	|pipenv install --dev|

<br>
<br>

## Pipenv - Package Management
|Pipenv Task							|Command Line (Terminal)|
|-----------|-----------|
|add a package							|pipenv install django|
|upgrade package						|??|
|specify a particular package version	|pipenv install mplfinance==0.12.7a5|
|Update '*' package to latest version	|pipenv update pandas|
|Delete / Remove package				|pipenv uninstall django|

<br>
<br>

## PIP / Pip3 Package Management
|Pip Task|Command Line (Terminal)|
|-----------|-----------|
|Install a package		|pip3 install [package_name]|
|Upgrade a package		|pip3 install --user --upgrade django|

<br>
<br>

## Visual Studio Code (VSC)
### Set Up **PIPENV** Project to work seamlessly with VSC
https://benjaminpack.com/blog/vs-code-python-pipenv/
|Task												|Command Line (Terminal)|
|-----------|-----------|
|CD into Project File								|cd [project_folder]|
|Ensure that Pipenv has been set up					|(see above)|
|Determine Path to PipEnv Setup File				|pipenv --py|
|Create project settings file fo VS Code to use		|mkdir .vscode && touch .vscode/settings.json|
|Open the Settings File and paste in the following	|Change the VirtualENV path to yours|
```
	{
    "files.exclude": {
        "**/.git": true,
        "**/.svn": true,
        "**/.hg": true,
        "**/CVS": true,
        "**/.DS_Store": true,
        "**/*.pyc": true,
        "**/__pycache__": true
    },
    "python.pythonPath": "<VIRTUALENV_PYTHON_PATH_HERE>",
	"python.defaultInterpreterPath": "<VIRTUALENV_PYTHON_PATH_HERE>",
	}
```
Restart VSC Project by File/Open Folder/[choose your project]

<br>
<br>

### pip show pipenv
##### show where the package is installed


## Template Table 
|Header_1|Header_2|
|-----------|-----------|
|text|text|
|text|text|