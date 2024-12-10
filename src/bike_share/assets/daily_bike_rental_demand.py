import pandas as pd
from dagster import asset

# TODO: Define the daily_bike_rental_demand asset. Use the DataLoader to load all CSV files in the data directory.

from bike_share.resources.data_loader import DataLoader

@asset()
def daily_bike_rental_demand() -> pd.DataFrame:
    """Raw daily bike rental demand dataset"""
    return DataLoader().load()

if __name__ == '__main__':
    raw_data = daily_bike_rental_demand()
    print(raw_data.head())

