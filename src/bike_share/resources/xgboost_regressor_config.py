from dagster import ConfigurableResource

# TODO: Define the XGBRegressorGridSearchConfig resource here.
"""Model Hyperparameters"""
class XGBRegressorGridSearchConfig:
    def grid_hyperparameters(self) -> dict:
        param_grid = {
        'estimator__n_estimators': [100, 200, 300],
        'estimator__learning_rate': [0.01, 0.1, 0.2],
        'estimator__max_depth': [3, 5, 7],
        'estimator__subsample': [0.8, 1.0],
        'estimator__colsample_bytree': [0.8, 1.0]
        }
        return param_grid