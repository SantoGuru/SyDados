# py/toXLSX.py

import json
import pandas as pd

def json_to_xlsx(json_file_path, output_file_path):
    """
    Converts a JSON file to an Excel file (.xlsx).

    Args:
        json_file_path (str): Path to the JSON file to be converted.
        output_file_path (str): Path where the Excel file will be saved.

    Returns:
        None

    Example:
        >>> json_to_xlsx('input.json', 'output.xlsx')
        Conversão concluída com sucesso. Arquivo salvo em: output.xlsx
    """
    # Carrega o arquivo JSON
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Converte os dados JSON para um DataFrame do Pandas
    df = pd.json_normalize(data)

    # Salva o DataFrame em um arquivo Excel
    df.to_excel(output_file_path, index=False)

    print("Conversão concluída com sucesso. Arquivo salvo em:", output_file_path)

def main(input_file, output_file):
    """
    Main function that calls json_to_xlsx with command line arguments.

    Args:
        input_file (str): Path to the JSON file to be converted.
        output_file (str): Path where the Excel file will be saved.

    Returns:
        None

    Example:
        >>> python toXLSX.py input.json output.xlsx
        toXLSX processou o arquivo input.json e salvou o resultado em output.xlsx
    """
    json_to_xlsx(input_file, output_file)
    print(f"toXLSX processou o arquivo {input_file} e salvou o resultado em {output_file}")

if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])