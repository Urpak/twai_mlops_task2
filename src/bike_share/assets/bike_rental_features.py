import pandas as pd
from dagster import AutomationCondition, asset
from sqlalchemy.dialects.mssql.information_schema import columns

from bike_share.config import CATEGORICAL_FEATURES, NUMERIC_FEATURES, TARGET
from bike_share.resources.data_loader import DataLoader

# TODO: Define the bike_rental_features asset here. Use the daily_bike_rental_demand as input to this asset.

@asset(automation_condition=AutomationCondition.eager())
def bike_rental_features(daily_bike_rental_demand: pd.DataFrame) -> pd.DataFrame:
    """Select features and target column from the raw features."""
    columns = (
        CATEGORICAL_FEATURES + NUMERIC_FEATURES + [TARGET]
    )
    data = daily_bike_rental_demand
    data["cnt_lag_1"] = data["cnt"].shift(1)
    data["cnt_lag_2"] = data["cnt"].shift(2)
    data["cnt_lag_3"] = data["cnt"].shift(3)
    data["cnt_lag_4"] = data["cnt"].shift(4)
    data["cnt_lag_5"] = data["cnt"].shift(5)
    data["cnt_lag_6"] = data["cnt"].shift(6)
    #drop missing data
    data= data.dropna()

    return data[columns]

if __name__ == '__main__':
    raw_data = DataLoader().load()
    features = bike_rental_features(raw_data)

    print(features.head())