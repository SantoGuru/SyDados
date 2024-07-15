import json
import pandas as pd
import os

# Função para dividir a lista em blocos de tamanho especificado
def chunk_list(data, chunk_size):
    for i in range(0, len(data), chunk_size):
        yield data[i:i + chunk_size]

def main(input_file, output_dir):
    # Carregar o arquivo JSON
    with open(input_file, 'r', encoding='utf-8') as file:
        clientes = json.load(file)

    if not os.path.exists(output_dir):
        os.makedirs(output_dir)

    # Dividir os clientes em blocos de 50
    chunks = chunk_list(clientes, 50)

    # Exportar cada bloco para uma planilha Excel
    for idx, chunk in enumerate(chunks):
        df = pd.DataFrame(chunk)
        output_file = os.path.join(output_dir, f'clientes_bloco_{idx + 1}.xlsx')
        df.to_excel(output_file, index=False)

    print(f"Blockzar processou o arquivo {input_file} e salvou o resultado em {output_dir}")

if __name__ == "__main__":
    import sys
    input_file = sys.argv[1]
    output_dir = sys.argv[2]
    main(input_file, output_dir)
