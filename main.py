"""importacoes"""
from app import extract
from app import config
from app import load


def main() -> None:
    
    """Chamando a função load_data"""
    df = extract.load_data(config.INPUT_DIR / "2026.xlsx")
    
    
    # Chamando a função de save_data
    load.save_data(df, config.OUTPUT_DIR/"extracao-2026.xlsx")
    print(f"Arquivo gerado na pasta: {config.OUTPUT_DIR}/extracao-2026")
    
    # print(df.head(10))
    
if __name__ == "__main__":
    main()


