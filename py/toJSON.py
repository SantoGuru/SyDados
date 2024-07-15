import pandas as pd
import json
import os
import re

def validate_phone(phone):
    phone_pattern = re.compile(r'^55\d{2}9\d{8}$')
    return bool(phone_pattern.match(phone))

def verificar_digitos_iguais(numero):
    # Converta o número para string para facilitar a iteração pelos dígitos
    str_numero = str(numero)
    
    # Verifique se todos os dígitos são iguais ao primeiro dígito
    primeiro_digito = str_numero[0]
    for digito in str_numero:
        if digito != primeiro_digito:
            return False
    return True
# Função para formatar o número de telefone
def format_phone(phone):
    phone = ''.join(filter(str.isdigit, str(phone)))
    if not phone.startswith('55'):
        phone = '55' + phone
    if not validate_phone(phone):
        phone = phone[:4] + '9' + phone[4:] 
    return phone

# Função para converter o Excel para JSON
def convert_excel_to_json(excel_path, json_path):
    df = pd.read_excel(excel_path, sheet_name='Planilha1')
    
    grouped = df.groupby('NUMERO')
    invoices = []
    
    for numero, group in grouped:
        if verificar_digitos_iguais(numero):
           print(f"Todos os dígitos do número {numero} são iguais.")
        else:
            print(f"Nem todos os dígitos do número {numero} são iguais.")
            invoice = {
            "data": group['DATA'].iloc[0].strftime('%Y-%m-%d') if not pd.isna(group['DATA'].iloc[0]) else "no-date",
            "nome": group['NOME'].iloc[0] if not pd.isna(group['NOME'].iloc[0]) else "Cliente ("+format_phone(numero)+")",
            "numero": format_phone(numero),
            "e-mail": group["E-MAIL"].iloc[0] if not pd.isna(group['E-MAIL'].iloc[0]) else "no-email@teste.com",
            }
            invoices.append(invoice)
    with open(json_path, 'w') as json_file:
        json.dump(invoices, json_file, ensure_ascii=False, indent=4)

    print("Conversão concluída com sucesso")


def main(input_file, output_file):
    convert_excel_to_json(input_file, output_file)
    print(f"toJSON processou o arquivo {input_file} e salvou o resultado em {output_file}")

if __name__ == "__main__":
    import sys
    main(sys.argv[1], sys.argv[2])
    excel_path = sys.argv[1]
    json_path = sys.argv[2]
    
    # Certifique-se de que o diretório de saída exista
    os.makedirs(os.path.dirname(json_path), exist_ok=True)

    # Carregar e exibir o conteúdo do JSON gerado para o usuário
    with open(json_path, 'r') as file:
        json_data = json.load(file)

    json_data
