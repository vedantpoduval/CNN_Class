from cnn_classifier.utils import read_yaml,create_directories
from cnn_classifier.constants import *
from cnn_classifier.entity import DataIngestionConfig
from pathlib import Path
import os

class ConfigurationManager:
    def __init__(self,config_path = CONFIG_FILE_PATH,param_path = PARAMS_FILE_PATH):
        self.config = read_yaml(config_path)
        self.params = read_yaml(param_path)
        create_directories([self.config.root])
    
    def get_data_ingestion_config(self):
        config = self.config.data_ingestion
        create_directories([config.root_dir])
        dataingestion = DataIngestionConfig(
            config.root_dir,
            config.source_url,
            config.local_file_path,
            config.unzip_dir
        )
        return dataingestion