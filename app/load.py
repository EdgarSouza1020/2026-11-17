import pandas as pd


def save_data(df: pd.DataFrame, path: Path) -> None:
    """Salva um Dataframe em uma pasta informada no Path"""
    path.parent.mkdir(parents=True, exist_ok=True)
    df.to_excel(path, index=False)
