import pandas as pd
from dagster import AssetOut, AutomationCondition, multi_asset
from sklearn.model_selection import train_test_split

from bike_share.config import RANDOM_STATE


# TODO: Define the train_test_data asset here. Instead of using @asset, use @multi_asset.

@multi_asset(
    outs={
        'train_data': AssetOut(
            automation_condition=AutomationCondition.eager(),
        ),
        'test_data': AssetOut(
            automation_condition=AutomationCondition.eager(),
        ),
    }
)
def train_test_data(
        bike_rental_features: pd.DataFrame,
) ->tuple[pd.DataFrame, pd.DataFrame]:
    """Split the data set in training and testing subset."""
    train_data, test_data = train_test_split(
        bike_rental_features, random_state=RANDOM_STATE
    )
    return train_data, test_data