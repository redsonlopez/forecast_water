from sklearn.model_selection import train_test_split


def split_data(df, target="VALOR_FATURA"):

    X = df.drop(columns=[target])
    y = df[target]

    X_train_val, X_test, y_train_val, y_test = train_test_split(
        X, y, test_size=0.2, random_state=42
    )

    X_train, X_val, y_train, y_val = train_test_split(
        X_train_val, y_train_val, test_size=0.25, random_state=42
    )

    return X_train, X_val, X_test, y_train, y_val, y_test
