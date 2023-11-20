from typing import List, Optional
import os
import yaml
import pandas as pd

class DataLoader:
    def __init__(self, catalog_file: str = "catalog.yml"):
        """
        Initialize the DataLoader.

        Parameters:
        - catalog_file (str): Path to the catalog YAML file.
        """
        self._catalog_file = catalog_file
        self.catalog = self._load_catalog()

    def _load_catalog(self) -> dict:
        """
        Load the catalog from the YAML file.

        Returns:
        - dict: The loaded catalog.
        """
        with open(self._catalog_file, "r") as file:
            catalog = yaml.safe_load(file)
        return catalog

    def load(self, dataset_name: str) -> Optional[pd.DataFrame]:
        """
        Load a dataset from the catalog.

        Parameters:
        - dataset_name (str): The name of the dataset to load.

        Returns:
        - Optional[pd.DataFrame]: The loaded dataset as a Pandas DataFrame, or None if not found.
        """
        if dataset_name in self.catalog:
            file_path = self.catalog[dataset_name].get("filepath")
            data_type = self.catalog[dataset_name].get("datatype", "csv").lower()
            if file_path:
                full_path = os.path.join(os.path.dirname(self._catalog_file), file_path)
                try:
                    if data_type == "csv":
                        data = pd.read_csv(full_path)
                    elif data_type == "gzip":
                        data = pd.read_csv(full_path, compression='gzip')
                    else:
                        print(f"Error: Unsupported datatype '{data_type}' for dataset '{dataset_name}'.")
                        return None
                    return data
                except FileNotFoundError:
                    print(f"Error: File '{full_path}' not found.")
            else:
                print(f"Error: Filepath not specified for dataset '{dataset_name}'.")
        else:
            print(f"Error: Dataset '{dataset_name}' not found in the catalog.")
        return None

    def list_datasets(self) -> List[str]:
        """
        List the available datasets in the catalog.

        Returns:
        - List[str]: A list of dataset names.
        """
        return list(self.catalog.keys())

# Example usage in a notebook
# from DataLoader import DataLoader
# data_loader = DataLoader("path/to/catalog.yml")
# main_data = data_loader.load('main')
# available_datasets = data_loader.list_datasets()
# print("Available datasets:", available_datasets)
