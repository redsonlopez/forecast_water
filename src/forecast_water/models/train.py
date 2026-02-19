import joblib
from sklearn.pipeline import Pipeline
from sklearn.ensemble import RandomForestRegressor

from forecast_water.pipelines.preprocessing import build_preprocessor


def train_model(X_train, y_train, model_path):

    preprocessor = build_preprocessor()

    model = RandomForestRegressor(random_state=42)

    pipeline = Pipeline([
        ("preprocessing", preprocessor),
        ("model", model)
    ])

    pipeline.fit(X_train, y_train)

    joblib.dump(pipeline, model_path)

    return pipeline
