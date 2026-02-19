from sklearn.compose import ColumnTransformer
from sklearn.preprocessing import StandardScaler


def build_preprocessor():

    numerical_features = [
        "VALOR_FATURA_lag1",
        "VALOR_FATURA_lag2",
    ]

    preprocessor = ColumnTransformer(
        transformers=[
            ("num", StandardScaler(), numerical_features),
        ]
    )

    return preprocessor
