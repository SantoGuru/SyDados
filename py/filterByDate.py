import json
from datetime import datetime

def process_json(file_path, output_file_path):
    # Carrega o arquivo JSON
    with open(file_path, 'r') as file:
        data = json.load(file)

    # Dicionário para armazenar a entrada mais recente para cada nome
    latest_entries = {}
    for entry in data:
        name = entry['nome']
        date_str = entry['data']
        date = datetime.strptime(date_str, '%Y-%m-%d')  # Supondo que a data esteja no formato 'YYYY-MM-DD'

        if name not in latest_entries:
            latest_entries[name] = entry
        else:
            current_latest_date = datetime.strptime(latest_entries[name]['data'], '%Y-%m-%d')
            if date > current_latest_date:
                latest_entries[name] = entry

    # Extrai as entradas mais recentes e remove a coluna 'data'
    result = [{k: v for k, v in entry.items() if k != 'data'} for entry in latest_entries.values()]

    # Salva o resultado em um novo arquivo JSON
    with open(output_file_path, 'w') as file:
        json.dump(result, file, indent=4)

    print("filterByDate: Processamento concluído com sucesso. Arquivo salvo em:", output_file_path)


def main(input_file, output_file):
    process_json(input_file, output_file)
    print(f"filterByDate processou o arquivo {input_file} e salvou o resultado em {output_file}")

if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])
