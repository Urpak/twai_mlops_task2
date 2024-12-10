import glob
import hashlib
import os

import pandas as pd
from dagster import ConfigurableResource

from bike_share import DATA_DIRECTORY


class DataLoader(ConfigurableResource):
    data_directory:str = DATA_DIRECTORY

    def load(self) -> pd.DataFrame:
        """Loads CSV files from the specified directory and combines them into a single DataFrame."""
        # List all CSV files in the data directory

        print('datablabla:' + self.data_directory)

        csv_files = glob.glob(os.path.join(self.data_directory, "*.csv"))
        #csv_files = glob.glob(os.path.join('/home/kai/Git/twai_mlops_assignment2-main/data', "*.csv"))


        # Read each CSV file into a DataFrame
        dataframes = [pd.read_csv(f) for f in csv_files]

        # Combine DataFrames into one
        return pd.concat(dataframes, ignore_index=True)

    def hash(self) -> str:
        """Calculates a hash of the data in the data directory."""
        data = self.load()

        data_str = data.to_csv(index=False)

        sha1_hash = hashlib.new("sha1")
        sha1_hash.update(data_str.encode("utf-8"))

        return sha1_hash.hexdigest()
