
# Developer Notes

<br>
<br>

## Workflow (new project)
|Step|Tool|Details|
|---|---		|-----------|
| 1	|Git		|Create new project on GitHub|
| 2	|Terminal	|Clone Git Repo to local machine|
| 3	|Pipenv		|Create project folder for Virtual Environment|
| 4	|Pipenv		|Create Virtual Environment|
| 4	|Pipenv		|Set Python Version|
| 5	|Pipenv		|Add Default Packages|
| 6	|Pipenv		|Add / Delete / Maintain Packages|
| 7	|Pipenv		|Change Python Version|
| V	|Pipenv		|Activate Virtual Environment|
| X	|Pipenv		|Deactivate Virtual Environment|


<br>
<br>

## Workflow (Download project to new machine)
|Step|Tool|Details|
|---|---|-----------|
| B	|Terminal	|Clone Git Repo to local machine|
| V	|Pipenv		|Activate Virtual Environment|
| 8 |Pipenv		|Install Pipfile Packages|
| 8 |Pipenv		|Install Pipfile Dev Environment Packages|




## Workflow (Python and Pip /Pip3)
|Step|Tool|Details|
|---|---|-----------|




<br>
<br>

## Git Commands
|Step|Tasks										|Command Line (Terminal)|
|---|-----------								|-----------|
| 1 |Log into GitHub and create project			|https://www.github.com|
| 2 |Navigate to project parent folder			| cd {project parent folder}|
| 2 |Create project folder and Clone repo		|git clone https://github.com/RobHay67/Pluto_blue.git|
|   |Push Local brach to GitHub					|git push -u origin {branch name i.e master} |
|	|delete local branch						|git branch -d {branch name i.e master} |

<br>
<br>

## Pipenv 
pipenv install --python=/Library/Frameworks/Python.framework/Versions/3.13/bin/python3.13
|Link|Area			|Tasks														|Command Line (Terminal)			|example/notes|
|---|-----			|-----------												|-----------						|-------|
|	|				|Pipenv User Guide											| https://realpython.com/Pipenv-guide/|
| V |ACTIVATE		|Activate the Environment									| pipenv shell						|
| X |DEACTIVATE		|De-Activate the Environment								| exit								|
| 5 |Default Pkg	|Add Default package > Streamlit							|pipenv install streamlit|
| 5 |Default Pkg	|Add Default package > Watchdog								|pipenv install watchdog|
| 6 |Package		|Add package (latest)										|pipenv install django|
| 6 |Package		|Add package (specific version)								|pipenv install mplfinance==0.12.7a5|
| 6 |Package		|Delete package												|pipenv uninstall django|
| 6 |Packages		|Update package (latest version '*')						|pipenv update pandas|
| 6 |Packages		|Update ALL packages										|pipenv update
| 3 |Environment	|Navigate to project folder									| cd {project_folder}				|
| 3 |Environment	|Create fodler to store virtual environment locally			| see benjaminpack notes below		|
|	|Environment	|Create virtual environment (install Pipfile packages)		| pipenv install 					|
| 4	|Environment	|Create virtual environment with Specified Python version	| pipenv install --python 3.13 		|
|   |Environment	|Set the appropriate Python Version	(after creation)		| pipenv --python 3.13				| per the pipenv notes |
|	|Environment	|Delete the virtual environment								| pipenv --rm 						|
| 8 |Fresh Install	|cloned project (install Pipfile Packages)					|pipenv install						|
| 8 |Fresh Install	|cloned project (Install Dev Environement Packages)			|pipenv install --dev				|
|   |Paths			|show PATH to Virtual Environement							|pipenv --venv 						| /Users/robhay/Developer/share_screener/.venv |
|   |Paths			|show PATH to current version								|where python or pipenv --py		| /Users/robhay/Developer/share_screener/.venv/bin/python |
|   |Paths			|show Python version (for project)							|python --version 					| Python 3.13.8 |
|   |Paths			|show list of installed packages (for project)				|pip list							|

| 7 |Change python version										|pipenv install --python 3.13		| python_version = "3.13"|

<br>
<br>


## Terminal Commands (Python and Pip / Pip3)
|Step|Tasks										|Command Line (Terminal)|example|
|-------|-----------								|-----------|-----------|
|python |download python version from web			|https://www.python.org/downloads/|
|terminal|check installed python versions			|check machine Applications folder to see installed versions|
|python	|Show ALL versions and paths				|which -a python python2 python2.7 python3 python3.6 python3.13|
|python	|											|which -a python3|
|python	|											|which -a python3.13|
|python |Show Python version (system)				|python --version | Python 3.13.8 |
|python |Show PATH to current version				|where python	|/Library/Frameworks/Python.framework/Versions/3.8/bin/python3 |
|Pip   	|package list (for system)					|pip list / pip3 list|
|Pip   	|Install a package							|pip3 install {package_name}|
|Pip   	|Upgrade a package							|pip3 install --user --upgrade django|



<br>
<br>
<br>
<br>


#### Manage and Change python version within Pipenv (Need to test this)

|Tasks|What to do / Command Line (Terminal)|
|-----------|-----------|
|Check version being used|Application will show the version and path during initial load|
|Set intial version|Pipenv install --python 3.8|
Change the python version
|- manually change the version in Pipfile|python_version = "3.13"|
|- manually change the version in Pipfile|Pipenv install --python 3.13|
|- activate Pipenv |Pipenv shell|
|- install packages|Pipenv install|

Pipenv install --python=/usr/local/bin/python3.13





<br>
<br>


## Visual Studio Code (VSC)
### Set Up **Pipenv** Project to work seamlessly with VSC
https://benjaminpack.com/blog/vs-code-python-Pipenv/
|Task												|Command Line (Terminal)|
|-----------|-----------|
|CD into Project File								|cd [project_folder]|
|Ensure that Pipenv has been set up					|(see above)|
|Determine Path to Pipenv Setup File				|Pipenv --py|
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

### pip show Pipenv
##### show where the package is installed


## Template Table 
|Header_1|Header_2|
|-----------|-----------|
|text|text|
|text|text|

pip3 show pandas > will detail the package including its location (handy)

https://bilard.medium.com/change-python-version-in-pipenv-1ac7b8f9b7b9

A recent upgrade to Ubuntu 20.04 messed up one of my projects which depended on python3.7 and I had to switch over to a higher version, however, it took a lot of googling, trial and error before I figured out how to make the switch in Pipenv.
Here’s a step by step guide on how to do this:
1. Change the “python_version” variable in your Pipfile to the new version you want. In my case it was
python_version = “3.8”
2. Open your terminal and run
pipenv install --python=/path/to/your/python
This would remove the previous virtual environment and create a new one using the python version specified.
Hope this helps :)

pipenv install --python=/Library/Frameworks/Python.framework/Versions/3.13/bin/python3.13