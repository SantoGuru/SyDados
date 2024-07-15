# py/toXLSX.py


import json
import pandas as pd

def json_to_xlsx(json_file_path, output_file_path):
    # Carrega o arquivo JSON
    with open(json_file_path, 'r') as file:
        data = json.load(file)

    # Converte os dados JSON para um DataFrame do Pandas
    df = pd.json_normalize(data)

    # Salva o DataFrame em um arquivo Excel
    df.to_excel(output_file_path, index=False)

    print("Conversão concluída com sucesso. Arquivo salvo em:", output_file_path)

def main(input_file, output_file):
    json_to_xlsx(input_file, output_file)
    print(f"toXLSX processou o arquivo {input_file} e salvou o resultado em {output_file}")

if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])
