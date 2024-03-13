# Note : This is a python script for creating directories and workflow for a typical deep learning project.
# Note : Empty directories are not pushed by github
import os
from pathlib import Path
import logging

#This is the format of logging which we expect
logging.basicConfig(level = logging.INFO,format = '[%(asctime)s]: %(message)s:')

proj_name = "cnn_classifier"
files = [
    ".github/workflows/.gitkeep", #This is for implementing the github actions
    f"src/{proj_name}/__init__.py",
    f"src/{proj_name}/utils/__init__.py",
    f"src/{proj_name}/components/__init__.py",
    f"src/{proj_name}/config/__init__.py",
    f"src/{proj_name}/pipeline/__init__.py",
    f"src/{proj_name}/entity/__init__.py",
    f"src/{proj_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",
    "requirements.txt",
    "setup.py",
    "research/trials.ipynb"
]

for file in files:
    dir,dir_file = os.path.split(file)

    if dir != "":
        os.makedirs(dir,exist_ok=True)
        logging.info(f"Creating the directory: {dir} for file: {dir_file}")
    if (not os.path.exists(file)) or (os.path.getsize(file) == 0):
        with open(file,'w') as f:
            pass
            logging.info(f"Creating empty file {dir_file}")
    else:
        logging.info(f"{dir_file} already exists")

