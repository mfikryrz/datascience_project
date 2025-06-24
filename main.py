from src.datascience import logger
from src.datascience.pipelines.data_ingestion_pipeline import DataIngestionTrainingPipeline
from src.datascience.pipelines.data_validation_pipeline import DataValidationTrainingPipeline

STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    data_ingestion_pipeline = DataIngestionTrainingPipeline()
    data_ingestion_pipeline.initiate_data_ingestion()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")  

except Exception as e:
    logger.exception(e)
    raise e

STAGE_NAME = "Data Validation stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    from src.datascience.pipelines.data_validation_pipeline import DataValidationTrainingPipeline
    data_validation_pipeline = DataValidationTrainingPipeline()
    data_validation_pipeline.initiate_data_validation()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<")

except Exception as e:
    logger.exception(e)
    raise e