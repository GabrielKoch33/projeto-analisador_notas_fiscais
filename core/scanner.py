"""
Primeiro módulo que desenvolveremos.

Responsabilidades:

    percorrer diretórios
    entrar em subpastas
    localizar PDFs
    localizar JPG
    retornar uma lista de arquivos encontrados

Ele não abre arquivos.

Não faz OCR.

Não renomeia.

Apenas encontra arquivos.
"""
from pathlib import Path 

arquivos_pdf    = []
arquivos_jpg    = []
arquivos_random = []

'entrada_user = input("Insira o caminho completo da pasta aqui").strip()'
# Futuramente será o campo que o user informar

caminho = Path(r"C:\\Users\Terminal\Desktop\pessoal\pastas_nota_projeto")
# Torna o caminho um Objeto, permitindo acessar métodos unicos da biblioteca

if not caminho.exists():
    raise FileNotFoundError("[ERRO] O caminho informado não existe.")

elif not caminho.is_dir():
    raise NotADirectoryError("[ERRO] O caminho informado não é uma pasta.")

else:
    for arquivo in caminho.rglob('*'): # percorre a arvore de arquivos (caso haja muitas subpastas)

        if not arquivo.is_file():
            continue

        extensao = arquivo.suffix.lower()
        if extensao == '.pdf':
            arquivos_pdf.append(arquivo)

        elif extensao in {".jpg",".jpeg"}:
            arquivos_jpg.append(arquivo)

        else:
            arquivos_random.append(arquivo)

print(f"\nPDFs encontrados: {len(arquivos_pdf)}")
for arquivo in arquivos_pdf:
    print(arquivo)

print(f"\nJPGs encontrados: {len(arquivos_jpg)}")
for arquivo in arquivos_jpg:
    print(arquivo)
