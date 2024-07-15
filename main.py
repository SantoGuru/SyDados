import os
import importlib
import sys

# Adiciona o diretório 'py' ao sys.path para permitir a importação dos scripts
sys.path.append(os.path.join(os.path.dirname(__file__), 'py'))

def execute_script(module_name, name, input_file, output_file):
    try:
        # Importa o módulo do script
        script = importlib.import_module(module_name)
        # Executa a função main(input_file, output_file) do script, se existir
        if hasattr(script, 'main'):
            script.main(input_file, output_file)
            print(f'{name} executado com sucesso.')
        else:
            print(f'{name} não possui uma função main(input_file, output_file).')
    except Exception as e:
        print(f'Erro ao executar {name}: {e}')

def toJSON(name, input_file):
    execute_script('toJSON', name, input_file, f"./json/{name}.json")

def numberClear(name, input_file):
    execute_script('numberClear', name, input_file, f"./json/{name}[NF].json")

def filterByDate(name, input_file):
    execute_script('filterByDate', name, input_file, f"./json/{name}[FDATE].json")

def blockzar(name, input_file):
    output_dir = f"./blocos/{name}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    execute_script('blockzar', name, input_file, output_dir)

def main():
    if len(sys.argv) != 3:
        print("Usage: python process_invoices.py <name> <path_to_excel_file>")
        sys.exit(1)
    
    name = sys.argv[1]
    excel = sys.argv[2]
    
    toJSON(name, excel)
    numberClear(name, f"./json/{name}.json")
    filterByDate(name, f"./json/{name}[NF].json")
    blockzar(name, f"./json/{name}[FDATE].json")

if __name__ == "__main__":
    main()
