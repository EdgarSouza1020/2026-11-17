import pandas as pd

def load_data(path: Path) -> pd.DataFrame:
    return pd.read_excel(path)
