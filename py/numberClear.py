import json
import re

def is_valid_phone(phone):
    # Definindo um número de telefone válido como contendo exatamente 13 dígitos e começando com '55'
    return re.fullmatch(r'55\d{11}', phone) is not None

def process_json(input_path, output_path):
    with open(input_path, 'r', encoding='utf-8', errors='ignore') as file:
        data = json.load(file)
    
    valid_clients = []
    for invoice in data:
        client_phone = invoice.get('numero', '')
        if is_valid_phone(client_phone):
            valid_clients.append(invoice)
    
    with open(output_path, 'w', encoding='utf-8') as file:
        json.dump(valid_clients, file, ensure_ascii=False, indent=4)
    
    print("numberClear: Arquivo processado com sucesso.")



def main(input_file, output_file):
    process_json(input_file, output_file)
    print(f"numberClear processou o arquivo {input_file} e salvou o resultado em {output_file}")

if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])
