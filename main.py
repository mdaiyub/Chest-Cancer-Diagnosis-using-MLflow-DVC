from ChestDiagnosisClassifier import logger
from ChestDiagnosisClassifier.pipeline.stage_1_data_ingestion import DataIngestionTrainingPipeline

#logger.info("Welcome to Chest Diagnosis Classifier!")


STAGE_NAME = "Data Ingestion stage"

try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<\n\nx==========x")
except Exception as e:
    logger.exception(e)
    raise e


