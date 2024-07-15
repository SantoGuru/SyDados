# Sistema de Analise de Dados
Trabalha com o conceito de analise dos dados dos clientes filtrando por dados válidos, removendo duplicatas e exportando planilhas com os dados em blocos.
## Depedências 
> pip install pandas
## Código de execução
> python main.py "NOME DA EMPRESA" "PATH/arquivo.xlsx"
### Parâmetros:
1. Passe o nome da empresa para ser utilizado como identificação
2. Passe o PATH, pro arquivo e o arquivo.
### Execução
- Recebimento do arquivo xlsx com filtro inicial manual (data,nome,numero,e-mail)
- Processamento do xlsx para JSON.
- Processamento do filtro de números.
- Processamento do filtro de data, para eliminar duplicatas mantendo a versão mais recente.
- Processamento do dados dividos em blocos de 50 em formato xlsx.
