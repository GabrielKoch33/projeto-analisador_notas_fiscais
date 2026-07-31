class Nota:
      
    # ------ CONSTRUTOR ------#
    def __init__(self, arquivo_original):

        self.arquivo_original = arquivo_original # Nome do arquivo 'nota-compras.pdf'

        self.tipo = arquivo_original.suffix # Extensão '.pdf', '.jpg' ou '.jpeg'

        # Adicionados pelo leitor de arquivo
        self.texto_ocr        = ""  # Texto extraído do OCR
        self.imagens_paginas  = []  # Como o OCR trabalha em cima de Imagens, para toda página PDF iremos transformar em imagem e anexar nessa lista

        # Adicionados pelo extrator
        self.cnpj         = ""  # Campo CNPJ extraído usando OCR
        self.razao_social = ""  # Campo NOME DA EMPRESA extraído usando OCR
        self.num_nota     = ""  # Campo Nº NF extraído usando OCR

    # ------ SETTERS ------#
    def set_arq_original(self, arquivo_original):
        self.arquivo_original = arquivo_original

    def set_tipo(self, tipo):
        self.tipo = tipo

    def set_texto_ocr(self, texto_ocr):
        self.texto_ocr = texto_ocr

    def set_imagens_paginas(self, imagens_paginas):
        self.imagens_paginas = imagens_paginas

    def set_cnpj(self, cnpj):
        self.cnpj = cnpj

    def set_razao_social(self, razao_social):
        self.razao_social = razao_social

    def set_num_nf(self, num_nota):
        self.num_nota = num_nota

    # ------ GETTERS ------#
    def get_arq_original(self):
        return self.arquivo_original

    def get_tipo(self):
        return self.tipo

    def get_texto_ocr(self):
        return self.texto_ocr

    def get_imagens_paginas(self):
        return self.imagens_paginas

    def get_cnpj(self):
        return self.cnpj

    def get_razao_social(self):
        return self.razao_social

    def get_num_nf(self):
        return self.num_nota
