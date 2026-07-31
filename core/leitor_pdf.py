import pymupdf
from PIL import Image
from classes.nota import Nota

def leitor_pdf(objeto_nota: Nota) -> Nota:
    """
    Responsável por abrir PDFs.

    Vai receber uma lista de objetos, cada objeto representará um arquivo analisado pelo scanner
    Nesse caso será apenas para PDFs, mas há o módulo 'leitor_img' que se encarregará de analisar JPG ou JPEG

    Analisa uma Nota -> Abre o PDF -> Converte cada página com o PyMuPDF -> Armazena em Nota.imagens_paginas -> Retorna Nota atualizada
    """
    if objeto_nota.tipo != ".pdf":
        raise TypeError("[ERRO] O Arquivo não é do tipo PDF")

    # Abre o PDF
    with pymupdf.open(objeto_nota.arquivo_original) as pdf:
        # pdf é um objeto da classe Document, o qual contem todas as páginas do arquivo original
        for index_pagina in range(pdf.page_count):
            # Percorre as páginas desse PDF abertp
            
            pagina = pdf[index_pagina]
            # pagina vira um objeto Page sempre que acessamos um Document por indice
            pix = pagina.get_pixmap() 
            # pixmap traz atributos como altura, largura, e outros metadados

            mode = "RGBA" if pix.alpha else "RGB"

            imagem = Image.frombytes(mode,(pix.width,pix.height),pix.samples)
            # Para cada página criamos uma imagem do conteúdo

            objeto_nota.imagens_paginas.append(imagem)
            # Adicionamos à lista uma Imagem, cada Imagem representa uma página do PDF

    return objeto_nota # Retorna o Objeto Nota com o campo de páginas preenchidas
if __name__ == '__main__':
    pass
# Métodos Document:
# pdf.page_count
# pdf[0] ou pdf.load_page(0) retorna um objeto da classe Page, permitindo extrair dados de uma página especifíca

