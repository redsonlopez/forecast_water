import pandas as pd


def add_time_features(df: pd.DataFrame) -> pd.DataFrame:
    df["ANO_VENCIMENTO"] = df["DATA_VENCIMENTO"].dt.year
    df["MES_VENCIMENTO"] = df["DATA_VENCIMENTO"].dt.month
    df["TRIMESTRE"] = df["DATA_VENCIMENTO"].dt.quarter
    return df


def create_lags(df: pd.DataFrame, col: str, id_col: str, max_lag=2):

    df = df.sort_values(["MATRICULA", "DATA_VENCIMENTO"])

    for lag in range(1, max_lag + 1):
        df[f"{col}_lag{lag}"] = df.groupby(id_col)[col].shift(lag)

    return df.dropna().reset_index(drop=True)
