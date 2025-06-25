import os
from src.datascience import logger
from src.datascience.entity.config_entity import  DataTransformationConfig
import pandas as pd
from sklearn.model_selection import train_test_split


class DataTransformation:
    def __init__(self, config: DataTransformationConfig):
        self.config = config
    
    def split_data(self):
        data = pd.read_csv(self.config.data_path)
        train, test = train_test_split(data, test_size=0.2, random_state=42)
        train.to_csv(os.path.join(self.config.root_dir, 'train.csv'), index=False)
        test.to_csv(os.path.join(self.config.root_dir, 'test.csv'), index=False)

        logger.info("Data split into train and test sets.")
        logger.info(f"Train set shape: {train.shape}")
        logger.info(f"Test set shape: {test.shape}")

        print(f"Train set shape: {train.shape}")
        print(f"Test set shape: {test.shape}")