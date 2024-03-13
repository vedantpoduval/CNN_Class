#This file specifies the logging information of the project
import os
import sys
import logging

log_fmt = "[%(asctime)s: %(levelname)s: %(module)s: %(message)s]"
log_dir = "logs"
log_filepath = os.path.join(log_dir,"running_logs.log")
os.makedirs(log_dir,exist_ok=True)

logging.basicConfig(format=log_fmt,
                    level=logging.INFO,
                    handlers=[
                        logging.FileHandler(log_filepath),
                        logging.StreamHandler(sys.stdout),
                    ])
logger = logging.getLogger("cnnClassifierLogger")
