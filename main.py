"""importacoes"""
from app import extract
from app import config


def main() -> None:
    
    df = extract.load_data(config.INPUT_DIR / "2026.xlsx")
    print(df.head(10))
    
if __name__ == "__main__":
    main()
