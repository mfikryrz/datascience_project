from src.datascience.config.configuration import ConfigurationManager
from src.datascience.components.data_transformation import DataTransformation
from src.datascience import logger
from pathlib import Path

STAGE_NAME = "Data Transformation stage"

class DataTransformationTrainingPipeline:
    def __init__(self):
        pass
    
    def initiate_data_transformation(self):
        try:
            with open(Path("artifacts\data_validation\status.txt"), "r") as f:
                status = f.read().split(" ")[-1].strip()
            if status == "True":
                config = ConfigurationManager()
                data_transformation_config = config.get_data_transformation_config()
                data_transformation = DataTransformation(config=data_transformation_config)
                data_transformation.split_data()
            else:
                logger.info("Data validation failed. Your data scheme is not valid.")
        except Exception as e:
            logger.exception(e)
            raise e
