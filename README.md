This project is for utilizing a variety of google api's to transcribe and translate foreign video. Usage of these scripts and tools will require the inclusion of a set of google api keys that have access to writing to google cloud storage, calling the speech api, and calling the translation api. Such credentials should be placed in a credentials.json file

Reccomended to use a virtual environment and PyCharm IDE, follow https://www.jetbrains.com/help/pycharm/creating-virtual-environment.html with regards to making a project venv. I go with defaults and then activate in terminal via source venv/bin/activate, then install requirements via pip install -r requirements.txt

system requires ffmpeg and a shell. TODO add a docker container setup