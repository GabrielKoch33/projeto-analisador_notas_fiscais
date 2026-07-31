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
from classes.nota import Nota
from leitor_pdf import leitor_pdf
from leitor_img import leitor_img


def localiza_arquivos(diretorio: str) -> object:
    """
    Percorre um diretório e suas subpastas procurando PDFs e JPGS/JPEGS

    Args:
        Diretorio: str do caminho fornecido pelo usuário

    Returns:
        Gerador: Para evitar sobrecarga de memória irei usar Generator
        Cada Objeto Nota criada é manipulada e é liberada logo em seguida, evitando guardar tudo na memória

    Raises:
        FileNotFoundError: Quando o caminho não existe.
        NotADirectoryError: Quando o caminho não é uma pasta.
    """
    caminho = Path(diretorio)
    # Torna o caminho um Objeto, permitindo acessar métodos unicos da biblioteca

    if not caminho.exists():
        raise FileNotFoundError("[ERRO] O caminho informado não existe.")

    elif not caminho.is_dir():
        raise NotADirectoryError("[ERRO] O caminho informado não é uma pasta.")

    for arquivo in caminho.rglob('*'): # percorre a arvore de arquivos (caso haja muitas subpastas)

        if not arquivo.is_file():
            continue

        yield Nota(arquivo)

if __name__ == '__main__':
    diretorio_analise = input("Insira o caminho completo da pasta aqui").strip()
    # Hardcode = r"C:\Users\Terminal\Desktop\pessoal\pastas_nota_projeto\Caixa-1"
    for nota in localiza_arquivos(diretorio_analise):

        if Nota.tipo == '.pdf':
            leitor_pdf(Nota)
        elif Nota.tipo in {".jpg",".jpeg"}:
            leitor_img(Nota)

        # ocr()
        # extrator()
        # renomeia()
