from cnn_classifier.config import ConfigurationManager
from cnn_classifier.components import DataIngestion
from cnn_classifier import logger

class DataIngestionPipeline:
    def __init__(self):
        pass
    def main(self):
        config = ConfigurationManager()
        data_ingestion_config = config.get_data_ingestion_config()
        data_ingestion = DataIngestion(data_ingestion_config)
        data_ingestion.download_file()
        data_ingestion.unzip_and_clean()
        
        