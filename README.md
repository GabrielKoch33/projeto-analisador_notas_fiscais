# Projeto: Analisador de Notas Fiscais.
Sobre o Projeto: Analisa, renomeia e converte arquivos .JPGs de notas fiscais scanneadas com objetivo de agilizar o trabalho. As notas devem voltar no formato cnpj-nome-da-empresa-nf.pdf

# Use:
.\env_notas\Scripts\Activate.ps1


SCANNEIA NOTAS

    Selecionar Pasta

    ↓

    Percorrer pasta e subpastas

    ↓

    Encontrar arquivos

    ↓

    PDF?
            Sim → OCR

    JPG?
            Sim → Converter PDF → OCR

    ↓

    Extrair texto

    ↓

    Encontrar

    • CNPJ
    • Razão Social
    • Número da Nota

    ↓

    Encontrou tudo?

    Sim
            ↓

    Renomear arquivo

    Nao

    Mover para
    Erros

- Interface
    Tkinter

- OCR
    PaddleOCR

- PDFs digitalizados 
    pdf2image

- JPG 
    OCR -> texto -> Converter PDF -> Renomear -> Salvar

- Extração dos dados
    OCR -> texto -> ReGex (ex: "\d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}")

- Duplicados
    12345678000123-abcempresas-123552#1.pdf
    12345678000123-abcempresas-123552#2.pdf
    
- Erros
    Criada automaticamente dentro da pasta selecionada
    Biblioteca shutil

- JPG -> PDF
    img2pdf ou Pillow

- Leitura de subpastas
    os.walk()

- exe
    PyInstaller
---------------------------------------------------------------------------
| Biblioteca  |	Finalidade                                                |
---------------------------------------------------------------------------
| PaddleOCR   |	Converter páginas de PDF em imagens                       |
| Pillow	  |   Manipulação de imagens e conversão JPG→PDF              |
| pypdf       |	Leitura de PDFs quando necessário                         |
| OpenCV      |	Pré-processamento de imagens para melhorar o OCR          |
| regex       |   (re)	Extração de CNPJ, número da nota e outros campos  |
| unidecode   |	Remover acentos da razão social                           |
| tkinter     |	Interface gráfica                                         |      
| pathlib     |	Manipulação de arquivos e diretórios                      |
| shutil      |	Movimentação de arquivos para a pasta Erros               |
| PyInstaller |	Geração do executável                                     |
---------------------------------------------------------------------------