import pandas as pd
from pathlib import Path


def load_data(path: Path) -> pd.DataFrame:
    """Carrega um arquivo em Excel"""
    return pd.read_excel(path)



