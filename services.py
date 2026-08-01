import time
import io
import tiktoken as tik
import pypdf
import docx
from g4f.client import Client
from groq import Groq
from config import MODELO_DEFAULT_G4F, MODELO_DEFAULT_GROQ

def calcular_tokens(texto, modelo = "gpt-4o-mini"):
    try:
        # Puxar o codificador ofical da OpenIA
        # configurado para o modelo
        codificador = tik.encoding_for_model(modelo)
    
    except KeyError:
        # Caso o modelo seja genérico,
        # uso o padrão do GPT-4
        codificador = tik.encoding_for_model("cl100k_base")
        
    # O método .encode() transformar o texto puro
    # em uma lista de números (IDs dos tokens)
    lista_de_tokens = codificador.encode(texto)
    
    # Retornar o tamanho dessa lista
    # que é a quantidade extra de tokens
    return len(lista_de_tokens)

## Função para ler PDF/DOCX
def extrair_texto_de_arquivo(uploaded_file):
    if uploaded_file is None:
        return ""
    if uploaded_file.name.endswith('.txt'):
        return uploaded_file.getvalue().decode("utf-8")
    
    ## Fazer o if com .docx 
    elif uploaded_file.name.endswith('.docx'):
        doc = docx.Document(uploaded_file)
        return "\n".join([p.text for p in doc.paragraphs if p.text])
    
    ## Fazer o if com .pdf
    
    elif uploaded_file.name.endswith('.pdf'):
        leitor_pdf = pypdf.PdfReader(uploaded_file)
        textoextraido = ""
        for pagina in leitor_pdf.pages:
            t = pagina.extract_text()
            if t:
                textoextraido += t + "\n"
                
        return textoextraido
    
    return ""

# Função que gera um texto pronto
def gerar_template_word_bytes():
    doc = docx.Document()
    doc.add_heading("Base de dados oficial - Cursos Senai")
    
    # Salvar em um espaço na memória em bytes (buffer)
    buffer = io.BytesIO()
    
    
    # Salva o documento no buffer
    doc.save(buffer)
    
    # ponteiro volta na posição inicial
    buffer.seek(0)
    
    return buffer
    
# Função que vai gerar a resposta do bot
def gerar_resposta_ia(provedor, mensagens, groq_key = None, temperatura = 0.2):
    inicio = time.time()
    
    if provedor == "GPT-4o Mini (Via G4F)":
        client = Client()
        resposta = client.chat.completions.create(
            model = MODELO_DEFAULT_G4F,
            messages = mensagens,
            temperature = temperatura
        )
        texto = resposta.choices[0].message.content
    
    elif provedor == "Llama 3.3 (Via Groq)":
        if not groq_key:
            raise ValueError("GROQ_API_KEY não configurada no secrets.toml")
        
        client_groq = Groq(api_key = groq_key)
        resposta = client_groq.chat.completions.create(
            model = MODELO_DEFAULT_GROQ,
            messages = mensagens,
            temperature = temperatura
        )
    
    else:
        ValueError("Provedor inválido.")
        
    tempo = round(time.time() - inicio, 2)
    return texto, tempo