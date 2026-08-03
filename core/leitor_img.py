'''
Abrirá:

JPG
JPEG

Depois enviará ao OCR.
'''
from PIL import Image #pillow
from core.classes.nota import Nota

def leitor_img(objeto_nota: Nota) -> Nota:
    """
    Responsável por abrir imagens (JPEGS e JPGS)

    Vai receber um Objeto e devolverá o mesmo, só que com o atributo imagens_pagina preenchido

    """
    if objeto_nota.tipo not in {".jpg",".jpeg"}:
        raise TypeError("[ERRO] O Arquivo não é do tipo IMAGEM (jpg/jpeg)")

    with Image.open(objeto_nota.arquivo_original) as imagem:
        img = imagem.convert("RGB")
        objeto_nota.imagens_paginas.append(img)

    return objeto_nota
    
if __name__ == '__main__':
    pass
