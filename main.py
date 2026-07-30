"""
conversor.py — função que recebe um .jpg e devolve um .pdf temporário. Teste isso sozinho antes de tudo.

ocr.py — função que recebe um caminho de PDF e devolve o texto bruto de todas as páginas. 
veja a qualidade do texto extraído (isso vai definir se precisa de pré-processamento de imagem, tipo aumentar contraste/DPI).

extrator.py — a partir do texto bruto, três funções separadas:
    extrair_cnpj(texto) — regex tipo \d{2}\.?\d{3}\.?\d{3}/?\d{4}-?\d{2}
    extrair_razao_social(texto) — aqui é o mais difícil, provavelmente vai precisar de heurística (ex: linha acima/abaixo do CNPJ, ou palavra-chave "Emitente")
    extrair_numero_nota(texto) — regex perto de palavras como "NF-e", "Número", "Nº"

renomeador.py — monta a string final e faz o rename/move com tratamento de nome duplicado (o que fazer se o arquivo já existir?).

processador.py — junta os 4 passos acima num loop que varre o diretório informado.

gui/janela.py — só depois que o núcleo funciona via linha de comando, encapsula numa interface.

PyInstaller — por último, gera o .exe.
"""
'''
ENTRADA DO SISTEMA
'''