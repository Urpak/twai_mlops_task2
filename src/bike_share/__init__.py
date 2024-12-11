from dagster import Definitions

from bike_share.assets.models import linear_regression, xgboost_regressor
from bike_share.config import (
    DATA_DIRECTORY,
    MLFLOW_EXPERIMENT,
    MLFLOW_TRACKING_URL,
    XBG_LEARNING_RATE,
    XBG_MAX_DEPTH,
    XGB_COLSAMPLE_BYTREE,
    XGB_N_ESTIMATORS,
    XGB_SUBSAMPLE,
)
from bike_share.resources.data_loader import DataLoader
from bike_share.resources.mlflow_session import MlflowSession
from bike_share.assets.daily_bike_rental_demand import daily_bike_rental_demand
from bike_share.assets.bike_rental_features import bike_rental_features
from bike_share.assets.train_test import train_test_data


definitions = Definitions(
    assets=[
        daily_bike_rental_demand,
        bike_rental_features,
        train_test_data,
        linear_regression,
        xgboost_regressor
    ],
    resources={
        "data_loader": DataLoader(
            data_directory=DATA_DIRECTORY,
        ),
        "mlflow_session": MlflowSession(
            tracking_url=MLFLOW_TRACKING_URL,
            experiment=MLFLOW_EXPERIMENT,
        ),
    },
)
