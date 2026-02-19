import pandas as pd


def clean_raw_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, low_memory=False)

    df['VOLUME_MEDIDO_AGUA'] = (
        df['VOLUME_MEDIDO_AGUA']
        .astype(str)
        .str.rstrip('L')
    )

    df['VOLUME_MEDIDO_ESGOTO'] = (
        df['VOLUME_MEDIDO_ESGOTO']
        .astype(str)
        .str.rstrip('L')
    )

    df['VOLUME_MEDIDO_AGUA'] = pd.to_numeric(df['VOLUME_MEDIDO_AGUA'], errors='coerce')
    df['VOLUME_MEDIDO_ESGOTO'] = pd.to_numeric(df['VOLUME_MEDIDO_ESGOTO'], errors='coerce')

    df['VALOR_FATURA'] = (
        df['VALOR_FATURA']
        .str.replace('.', '', regex=False)
        .str.replace(',', '.', regex=False)
    )

    df['VALOR_FATURA'] = pd.to_numeric(df['VALOR_FATURA'])

    df["DATA_VENCIMENTO"] = (
        df["DATA_VENCIMENTO"]
        .astype(str)
        .str.strip()
    )

    df["DATA_VENCIMENTO"] = pd.to_datetime(
        df["DATA_VENCIMENTO"],
        dayfirst=True,
        errors="coerce"
    )

    df["BAIRRO"] = df["BAIRRO"].str.strip()

    return df
