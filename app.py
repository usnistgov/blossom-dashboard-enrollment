## This script creates a CLI-style application
## Run `python app.py` for available command-line options.
## See README for the recommended use.

#%% Load Libraries
import fire
from action import Action

if __name__ == '__main__':
    respond = Action()
    fire.Fire(respond)