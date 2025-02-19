import os
import importlib
import sys

# Adiciona o diretório 'py' ao sys.path para permitir a importação dos scripts
sys.path.append(os.path.join(os.path.dirname(__file__), 'py'))

def execute_script(module_name, name, input_file, output_file):
    """
    Execute a script with the given module name, input file, and output file.

    Args:
        module_name (str): The name of the module to execute.
        name (str): The name of the script.
        input_file (str): The path to the input file.
        output_file (str): The path to the output file.

    Returns:
        None

    Example:
        execute_script('toJSON', 'example', 'input.json', 'output.json')
    """
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

# JSON WITH FILTER - FLUXO #
def toJSON(name, input_file):
    """
    Convert a file to JSON format.

    Args:
        name (str): The name of the output file.
        input_file (str): The path to the input file.

    Returns:
        None

    Example:
        toJSON('example', 'input.xlsx')
    """
    output_dir = f"./json/{name}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    execute_script('toJSON', name, input_file, f"./json/{name}/{name}.json")

def numberClear(name, input_file):
    """
    Clear numbers from a JSON file.

    Args:
        name (str): The name of the output file.
        input_file (str): The path to the input file.

    Returns:
        None

    Example:
        numberClear('example', 'input.json')
    """
    output_dir = f"./json/{name}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    execute_script('numberClear', name, input_file, f"./json/{name}/{name}[NC].json")

def filterByDate_Filter(name, input_file):
    """
    Filter a JSON file by date.

    Args:
        name (str): The name of the output file.
        input_file (str): The path to the input file.

    Returns:
        None

    Example:
        filterByDate_Filter('example', 'input.json')
    """
    output_dir = f"./json/{name}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    execute_script('filterByDate', name, input_file, f"./json/{name}/{name}[FDATE_FILTER].json")

# Gera um XLSX filtrado, com as numerações finais
def toXLSX_FINAL(name, input_file):
    """
    Convert a JSON file to XLSX format.

    Args:
        name (str): The name of the output file.
        input_file (str): The path to the input file.

    Returns:
        None

    Example:
        toXLSX_FINAL('example', 'input.json')
    """
    output_dir = f"./excel/{name}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    execute_script('toXLSX', name, input_file, f"./excel/{name}/{name}[FINAL].xlsx")

# Gera os blocos de 50 com o JSON final
def blockzar(name, input_file):
    """
    Split a JSON file into blocks of 50.

    Args:
        name (str): The name of the output file.
        input_file (str): The path to the input file.

    Returns:
        None

    Example:
        blockzar('example', 'input.json')
    """
    output_dir = f"./blocos/{name}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    execute_script('blockzar', name, input_file, output_dir)

# JSON NO FILTER - FLUXO #
def toJSONnoFilter(name, input_file):
    """
    Convert a file to JSON format without filtering.

    Args:
        name (str): The name of the output file.
        input_file (str): The path to the input file.

    Returns:
        None

    Example:
        toJSONnoFilter('example', 'input.xlsx')
    """
    output_dir = f"./json/{name}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    execute_script('toJSONnoFilter', name, input_file, f"./json/{name}/{name}[NOFILTER].json")

def filterByDate_NoFilter(name, input_file):
    """
    Filter a JSON file by date without filtering.

    Args:
        name (str): The name of the output file.
        input_file (str): The path to the input file.

    Returns:
        None

    Example:
        filterByDate_NoFilter('example', 'input.json')
    """
    output_dir = f"./json/{name}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    execute_script('filterByDate', name, input_file, f"./json/{name}/{name}[FDATE_NOFILTER].json")

def toXLSX_TRATADO(name, input_file):
    """
    Convert a JSON file to XLSX format without filtering.

    Args:
        name (str): The name of the output file.
        input_file (str): The path to the input file.

    Returns:
        None

    Example:
        toXLSX_TRATADO('example', 'input.json')
    """
    output_dir = f"./excel/{name}"
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    execute_script('toXLSX', name, input_file, f"./excel/{name}/{name}[TRATADO].xlsx")

def main():
    """
    Main function.

    Returns:
        None
    """
    if len(sys.argv) != 3:
        print("Usage: python process_invoices.py <name> <path_to_excel_file>")
        sys.exit(1)
    
    name = sys.argv[1]
    excel = sys.argv[2]
    
    toJSONnoFilter(name, excel)
    filterByDate_NoFilter(name, f"./json/{name}/{name}[NOFILTER].json")
    toXLSX_TRATADO(name,f"./json/{name}/{name}[FDATE_NOFILTER].json")
    
    toJSON(name, excel)
    numberClear(name, f"./json/{name}/{name}.json")
    filterByDate_Filter(name, f"./json/{name}/{name}[NC].json")
    toXLSX_FINAL(name,f"./json/{name}/{name}[FDATE_FILTER].json")
    blockzar(name, f"./json/{name}/{name}[FDATE_FILTER].json")

if __name__ == "__main__":
    main()