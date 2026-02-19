from forecast_water.pipelines.data_cleaning import clean_raw_data
from forecast_water.pipelines.feature_engineering import add_time_features, create_lags
from forecast_water.data.split import split_data
from forecast_water.models.train import train_model

def main():

    df = clean_raw_data("data/raw/water.csv")

    df = add_time_features(df)
    df = create_lags(df, col="VALOR_FATURA", id_col="MATRICULA")

    X_train, X_val, X_test, y_train, y_val, y_test = split_data(df)

    train_model(X_train, y_train, "models/random_forest.joblib")


if __name__ == "__main__":
    main()
